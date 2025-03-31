# Contributing to [Agno](https://www.agno.com/)

## Resources

- [Docs](https://docs.agno.com/introduction)
- [GitHub](https://github.com/agno-agi/agno)
- [my fork](https://github.com/wgong/phidata)

## Apps

### Demos


created a helper pkg [utils_u8hi](https://github.com/digital-duck/st_tools/tree/main/utils-u8hi)

#### cookbook/u8hi_agents
store all Agno agents I have tried and liked

```bash
conda activate agno
cd ~/projects/wgong/phidata/cookbook/u8hi_agents 
python fin_agents_u8hi.py
```

wgong/phidata/cookbook/agent_concepts/memory/01_builtin_memory.py


`phidata/cookbook/u8hi_agents/04_persistent_memory_postgres.py`

use `DBeaver` client to connect to pgVector in docker

localhost:5532, schema=ai, user/pwd=ai/ai, 

query the recipe book

##### Playground

```
python agentic_rag_agent_playground_u8hi.py
```

Playground URL: https://app.agno.com/playground?endpoint=localhost%3A7777


##### [Workspace](https://docs.agno.com/workspaces/introduction)

```bash
pip install -U "agno[aws]"
curl -LsSf https://astral.sh/uv/install.sh | sh

update .env file

cd cookbook/u8hi_agents
ag ws create --template agent-app --name agent-app-chinook
cd agent-app-chinook
# https://docs.agno.com/workspaces/workspace-management/development-app

ag ws up --env dev --infra docker --type image --force
# failed
# posted issue at Agno community:
# https://community.agno.com/t/failed-to-start-workspace-due-to-docker-issue/889
ag ws restart --env dev --infra docker --type container

# select template = agent-app (others=agent-api)
# ws_name = agent-app1

```
Your new workspace is available at ./cookbook/u8hi_agents/agent-app1

- start ws: `ag ws up`
- Stop workspace: `ag ws down`

##### Local setup


https://docs.agno.com/workspaces/agent-app/local

https://github.com/digital-duck/agent-app-chinook

```
conda activate agno
cd ~/projects/wgong/phidata/cookbook/u8hi_agents/agent-app-chinook

ag ws up
# - Open localhost:8501 to view the streamlit UI.
# - Open localhost:8000/docs to view the FastAPI routes.

ag ws down
```

#### Issues 

##### docker sock non-default

https://community.agno.com/t/failed-to-start-workspace-due-to-docker-issue/889

see `~/projects/wgong/py4kids/lesson-18-ai/Agents/agno-phidata/readme.md`

##### Models DO NOT support tools
- `phi4` 
- `deepseek-r1` 

## Roadmap

## Dev

###  TODO

#### setup dev env

- scripts/dev_setup.sh
    - https://docs.agno.com/how-to/contribute

##### phidata-docs locally
- [source](https://github.com/agno-agi/phidata-docs)

- [fork](https://github.com/wgong/agno-docs)
    - ~/projects/wgong/agno-docs


#### learn uv

- https://pypi.org/project/uv/

#### learn agno Reference

- https://docs.agno.com/reference/agents/agent

#### play with cookbook

- https://docs.agno.com/examples/introduction

#### streamlit-app
- https://github.com/agno-agi/streamlit-app
- https://github.com/agno-agi/agno-demo-app

#### Build DataAgent
- as if a vanna wrapper

#### Build DocAgent
- similar to AG2

#### Dynamic Workflow
wrap `Prefect`


###  DONE





# Cookbook

## 2025-03-18

### `cookbook/workflows/blog_post_generator.py` : workflow / content creation


## 2025-03-16

### `cookbook/examples/agents/finance_agent_u8hi.py` : Finance Agent


### `cookbook/examples/agents/agno_support_agent_u8hi.py` : Agno Support Agent

got an error:
```
ERROR    Function save_and_run_code not found
```

### Tools

- `PythonTools`  in `agno_support_agent_u8hi.py`
- `YouTubeTools` in `youtube_agent`
- `ExaTools` in `travel_planner`, `shopping_partner`, `movie_recommedation`, `book_recommendation`
- `DuckDuckGoTools`, `Newspaper4kTools` in `research_agent`
- `GithubTools`, `LocalFileSystemTools` in `readme_generator`
- `FirecrawlTools` in `media_trend_analysis_agent`
- `PgVector` in `legal_consultant`
- `LanceDB` in `deep_knowledge`

