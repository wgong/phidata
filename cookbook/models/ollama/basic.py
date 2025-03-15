from agno.agent import Agent, RunResponse  # noqa
from agno.models.ollama import Ollama

model_id = "llama3.1"
agent = Agent(
            model=Ollama(id=model_id), 
            markdown=True,
        )

# Get the response in a variable
# run: RunResponse = agent.run("Share a 2 sentence horror story")
# print(run.content)

# Print the response in the terminal
user_msg = "write me a poem about Chinese character"
agent.print_response(user_msg, stream=True)
