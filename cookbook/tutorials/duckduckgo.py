from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
import os 

os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY_OPENAI")

assistant = Assistant(
    llm=OpenAIChat(model="gpt-3.5-turbo"),
    tools=[DuckDuckGo()], 
    show_tool_calls=True
)
assistant.print_response("Whats happening in France?", markdown=True)
