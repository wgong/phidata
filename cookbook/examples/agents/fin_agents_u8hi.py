"""🗞️ Finance Agent - Your Personal Market Analyst!

This example shows how to create a sophisticated financial analyst that provides
comprehensive market insights using real-time data. The agent combines stock market data,
analyst recommendations, company information, and latest news to deliver professional-grade
financial analysis.

Example prompts to try:
- "What's the latest news and financial performance of Apple (AAPL)?"
- "Give me a detailed analysis of Tesla's (TSLA) current market position"
- "How are Microsoft's (MSFT) financials looking? Include analyst recommendations"
- "Analyze NVIDIA's (NVDA) stock performance and future outlook"
- "What's the market saying about Amazon's (AMZN) latest quarter?"

Run: `pip install openai yfinance agno` to install the dependencies
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools

from utils_u8hi import * 

instructions=dedent("""\
        You are a seasoned Wall Street analyst with deep expertise in market analysis! 📊

        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Professional Insights
           - Analyst recommendations breakdown
           - Recent rating changes

        4. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use tables for data presentation
        - Include clear section headers
        - Add emoji indicators for trends (📈 📉)
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysis

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
    """)
                    
tools=[
    YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        historical_prices=True,
        company_info=True,
        company_news=True,
    )
]

topics = [
"""
Compare Telsa against other EV manufacturers in terms of 
production metrics and profit margins

"""
,
"""
"How do Meta's financial metrics compare to its social media peers?"
"""
,

"""
    Analyze the semiconductor market performance focusing on:
    - NVIDIA (NVDA)
    - AMD (AMD)
    - Intel (INTC)
    - Taiwan Semiconductor (TSM)
    Compare their market positions, growth metrics, and future outlook.
"""
,

"""
What's the latest news and financial performance for AMD?
"""
,

"""
What's the latest news and financial performance for Google?
"""
,

"""
What's the latest news and financial performance of Apple (AAPL)?
"""
,
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

model_id = "phi4"
model_obj = Ollama(id=model_id)
models.append((model_id, model_obj))

model_id = "llama3.1"
model_obj = Ollama(id=model_id)
models.append((model_id, model_obj))

for topic in topics:

    # select Google related topic
    if "google" not in topic.lower():
        continue 

    for model_id, model_obj in models:
        if model_id not in ["llama3.1"]:
            continue

        finance_agent = Agent(
            model=model_obj,
            tools=tools,
            instructions=instructions,
            add_datetime_to_instructions=True,
            show_tool_calls=True,
            markdown=True,
        )

        invoke_agent(finance_agent, 
                     topic, 
                     model_id = model_id, 
                     file_log=__file__)