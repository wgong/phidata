from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
import os 

os.environ["OPENAI_API_KEY"] = os.environ.get("API_KEY_OPENAI")

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    show_tool_calls=True,
    markdown=True,
)
assistant.print_response("What is the stock price of NEM")
assistant.print_response("Write a comparison between NEM and GOLD, use all tools available.")
