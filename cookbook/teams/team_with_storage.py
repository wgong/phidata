from uuid import uuid4

from agno.agent.agent import Agent
from agno.memory.db.postgres import PgMemoryDb
from agno.memory.team import TeamMemory
from agno.models.anthropic.claude import Claude
from agno.models.mistral.mistral import MistralChat
from agno.models.openai.chat import OpenAIChat
from agno.storage.postgres import PostgresStorage
from agno.team import Team
from sqlalchemy import create_engine

french_agent = Agent(
    name="French Agent",
    role="You can only answer in French",
    model=MistralChat(id="mistral-large-latest"),
    instructions=[
        "You must only respond in French",
    ],
)

english_agent = Agent(
    name="English Agent",
    role="You can only answer in English",
    model=OpenAIChat("gpt-4o"),
    instructions=[
        "You must only respond in English",
    ],
)
user_id = str(uuid4())

multi_language_team = Team(
    name="Multi Language Team",
    mode="route",
    team_id=str(uuid4()),
    user_id=user_id,
    model=OpenAIChat("gpt-4o"),
    members=[
        french_agent,
        english_agent,
    ],
    storage=PostgresStorage(
        table_name="agent_team_sessions",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
    ),
    memory=TeamMemory(
        db=PgMemoryDb(
            table_name="agent_team_memory",
            db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
        ),
        user_id=user_id,
        create_user_memories=True,
        update_user_memories_after_run=True,
    ),
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "You are a language router that directs questions to the appropriate language agent.",
        "If the user asks in a language whose agent is not a team member, respond in English with:",
        "'I can only answer in the following languages: English, Spanish, Japanese, French and German. Please ask your question in one of these languages.'",
        "Always check the language of the user's input before routing to an agent.",
        "For unsupported languages like Italian, respond in English with the above message.",
    ],
    show_members_responses=True,
    enable_team_history=True,
)

multi_language_team.print_response(
    "Comment allez-vous?",
    stream=True,
)
multi_language_team.print_response(
    "Qu'est-ce que je viens de dire?",
    stream=True,
)
