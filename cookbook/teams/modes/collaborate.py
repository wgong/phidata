"""
This example demonstrates a collaborative team of AI agents working together to research topics across different platforms.

The team consists of two specialized agents:
1. Reddit Researcher - Uses DuckDuckGo to find and analyze relevant Reddit posts
2. HackerNews Researcher - Uses HackerNews API to find and analyze relevant HackerNews posts

The agents work in "collaborate" mode, meaning they:
- Both are given the same task at the same time
- Work towards reaching consensus through discussion
- Are coordinated by a team leader that guides the discussion

The team leader moderates the discussion and determines when consensus is reached.

This setup is useful for:
- Getting diverse perspectives from different online communities
- Cross-referencing information across platforms
- Having agents collaborate to form more comprehensive analysis
- Reaching balanced conclusions through structured discussion

"""

import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team.team import Team
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.hackernews import HackerNewsTools

reddit_researcher = Agent(
    name="Reddit Researcher",
    role="Research a topic on Reddit",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGoTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a Reddit researcher.
    You will be given a topic to research on Reddit.
    You will need to find the most relevant posts on Reddit.
    """),
)

hackernews_researcher = Agent(
    name="HackerNews Researcher",
    model=OpenAIChat("gpt-4o"),
    role="Research a topic on HackerNews.",
    tools=[HackerNewsTools()],
    add_name_to_instructions=True,
    instructions=dedent("""
    You are a HackerNews researcher.
    You will be given a topic to research on HackerNews.
    You will need to find the most relevant posts on HackerNews.
    """),
)


agent_team = Team(
    name="Discussion Team",
    mode="collaborate",
    model=OpenAIChat("gpt-4o"),
    members=[
        reddit_researcher,
        hackernews_researcher,
    ],
    instructions=[
        "You are a discussion master.",
        "You have to stop the discussion when you think the team has reached a consensus.",
    ],
    success_criteria="The team has reached a consensus.",
    enable_agentic_context=True,
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    show_members_responses=True,
)

if __name__ == "__main__":
    asyncio.run(
        agent_team.aprint_response(
            message="Start the discussion on the topic: 'What is the best way to learn to code?'",
            # stream=True,
            # stream_intermediate_steps=True,
        )
    )
