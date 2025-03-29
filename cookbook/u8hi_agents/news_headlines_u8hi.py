from agno.agent import Agent, RunResponse  # noqa
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

from utils_u8hi import * 

# setup tools
tools=[DuckDuckGoTools()]

# setup topics
topics = [
    "Show top 5 journals in US that publish compuational linquistics research",
    # "Show me top 5 news in AI in past week", 
    # "Show me top 5 papers on AI agents published at arxiv.org in past week",   
]

# setup models
models = []
# use cloud model
model_id = "gpt-4o-mini"
model_obj = OpenAIChat(id=model_id)
models.append((model_id, model_obj))

# use open source model
model_id = "qwen2.5"
model_obj = Ollama(id=model_id)
models.append((model_id, model_obj))

# loop over topics
for topic in topics: 
    # loop over models
    for model_id, model_obj in models:
        agent = Agent(
            model=model_obj, 
            tools=tools, 
            markdown=True,
        )

        invoke_agent(agent, 
                     topic, 
                     model_id = model_id, 
                     file_log=__file__)
