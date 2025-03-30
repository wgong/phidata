"""
see URL = https://docs.agno.com/examples/concepts/rag/agentic-rag-pgvector

```bash
./cookbook/scripts/run_pgvector.sh  # to start a postgres container with pgvector
pip install openai sqlalchemy 'psycopg[binary]' pgvector agno # to install the dependencies
cd cookbook/agent_concepts/rag
python agentic_rag_pgvector_zinets_u8hi.py  # to run the agent
```

"""

from agno.agent import Agent
from agno.embedder.openai import OpenAIEmbedder
# from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.models.openai import OpenAIChat
from agno.vectordb.pgvector import PgVector, SearchType

# my helper to set API Keys
from utils_u8hi import *

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
# Create a knowledge base of PDFs from URLs

# ZiNets paper PDF can be found at https://arxiv.org/pdf/2502.19428
knowledge_base = PDFKnowledgeBase(
    path="ZiNets_2502.19428v1.pdf",
    # Use PgVector as the vector database and store embeddings in the `ai.recipes` table
    vector_db=PgVector(
        table_name="zinets",
        db_url=db_url,
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id="text-embedding-3-small"),
    ),
    reader=PDFReader(chunk=True),
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
agent.knowledge.load(recreate=False)

agent.print_response(
    "Explain what elemental character is and why it is a useful concept", 
    stream=True
)

