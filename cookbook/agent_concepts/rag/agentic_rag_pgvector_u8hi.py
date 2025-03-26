"""
see URL = https://docs.agno.com/examples/concepts/rag/agentic-rag-pgvector

```bash
./cookbook/scripts/run_pgvector.sh  # to start a postgres container with pgvector
pip install openai sqlalchemy 'psycopg[binary]' pgvector agno # to install the dependencies
cd cookbook/agent_concepts/rag
python agentic_rag_pgvector_u8hi.py  # to run the agent
```

"""

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType

from utils_u8hi import *

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
    ),
)
# Load the knowledge base: Comment after first run as the knowledge base is already loaded
knowledge_base.load(upsert=True)

model_id = "gpt-4o-mini"  # "gpt-4o"
agent = Agent(
    model=OpenAIChat(id=model_id),
    knowledge=knowledge_base,
    # Add a tool to search the knowledge base which enables agentic RAG.
    # This is enabled by default when `knowledge` is provided to the Agent.
    search_knowledge=True,
    show_tool_calls=True,
    markdown=True,
)
agent.print_response(
    "How do I make chicken and galangal in coconut milk soup", stream=True
)
# agent.print_response(
#     "Hi, i want to make a 3 course meal. Can you recommend some recipes. "
#     "I'd like to start with a soup, then im thinking a thai curry for the main course and finish with a dessert",
#     stream=True,
# )
