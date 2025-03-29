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


#### Issues 


The following models DO NOT support tools
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

