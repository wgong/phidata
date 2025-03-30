from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.embedder.ollama import OllamaEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama
from agno.playground import Playground, serve_playground_app
from agno.storage.agent.postgres import PostgresAgentStorage
from agno.vectordb.pgvector import PgVector, SearchType

from utils_u8hi import * 

# model_id = "qwen2.5"
# model_obj = Ollama(id=model_id)

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
# Create a knowledge base of PDFs from URLs
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    # Use PgVector as the vector database and store embeddings in the `ai.recipes` table
    vector_db=PgVector(
        table_name="recipes",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
        # embedder=OllamaEmbedder(id="nomic-embed-text"),
    ),
)

rag_agent = Agent(
    name="RAG Agent",
    agent_id="rag-agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    knowledge=knowledge_base,
    # Add a tool to search the knowledge base which enables agentic RAG.
    # This is enabled by default when `knowledge` is provided to the Agent.
    search_knowledge=True,
    # Add a tool to read chat history.
    read_chat_history=True,
    # Store the agent sessions in the `ai.rag_agent_sessions` table
    storage=PostgresAgentStorage(table_name="rag_agent_sessions", db_url=db_url),
    instructions=[
        "Always search your knowledge base first and use it if available.",
        "Share the page number or source URL of the information you used in your response.",
        "If health benefits are mentioned, include them in the response.",
        "Important: Use tables where possible.",
    ],
    markdown=True,
)

app = Playground(agents=[rag_agent]).get_app()

if __name__ == "__main__":
    # Load the knowledge base: Comment after first run as the knowledge base is already loaded
    knowledge_base.load(upsert=True)

    serve_playground_app("agentic_rag_agent_playground_u8hi:app", reload=True)