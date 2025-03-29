from agno.agent import Agent, RunResponse  # noqa
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools

model_id = "qwen2.5"
agent = Agent(
    model=Ollama(id=model_id), 
    tools=[DuckDuckGoTools()], 
    markdown=True,
)

# Print the response in the terminal
prompt = "Show me top 5 news in AI in past week"
agent.print_response(prompt)
