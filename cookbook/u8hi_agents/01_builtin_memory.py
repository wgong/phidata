from agno.agent import Agent
from agno.models.openai import OpenAIChat
from rich.pretty import pprint

from utils_u8hi import *  

print(f"model_id = {model_id}")

agent = Agent(
    model=OpenAIChat(id=model_id),
    # Set add_history_to_messages=true to add the previous chat history to the messages sent to the Model.
    add_history_to_messages=True,
    # Number of historical responses to add to the messages.
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

# -*- Create a run
agent.print_response("Share a 2 sentence jokes", stream=True)
# -*- Print the messages in the memory
pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])

# -*- Ask a follow up question that continues the conversation
agent.print_response("What was my first message?", stream=True)
# -*- Print the messages in the memory
pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])
