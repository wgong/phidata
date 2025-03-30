"""
https://docs.agno.com/examples/concepts/rag/agentic-rag-pgvector
"""
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.sql import SQLTools

from utils_u8hi import *

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

model_id = "qwen2.5"
agent = Agent(
        model=Ollama(id=model_id),
        tools=[SQLTools(db_url=db_url)],
    )

topic = """
    List the tables in the database. 
    Tell me about contents of recipes table if found
"""
agent.print_response(
    markdown=True,
)
