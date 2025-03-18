"""
make this a helper installable module
see option 2 at https://claude.ai/chat/00162a89-54ea-4de6-918d-6ed33afe50da



"""

from api_key_store import ApiKeyStore
import os
from time import time 
from datetime import datetime
from agno.agent import Agent

def get_api_key(key_name="OPENAI/Yiwen"):
    return ApiKeyStore().get_api_key(key_name)



os.environ["OPENAI_API_KEY"] = get_api_key()

# use this less costly model
model_id = "gpt-4o-mini"

def log_response(topic, resp_msg, model_id, ts_now, elapsed_sec, file_log="", to_print=True):
    if to_print:
        # print to console
        print(resp_msg)

    if not file_log:
        filename_without_ext = os.path.splitext(os.path.basename(__file__))[0]  # e.g., "script"
        file_log = f"{filename_without_ext}.log.md"

    # log Agent response
    with open(file_log, "a") as flog:
        flog.write("\n\n" + 80*"=" + "\n")
        flog.write(f"\n [Topic] {topic} \n")
        flog.write("\n\n" + 40*"=" + "\n")
        flog.write(resp_msg)
        flog.write(f"\n\n[ ({model_id}) - ({ts_now}) ] Completed in {elapsed_sec:.3f} sec")
        flog.write("\n\n" + 40*"=" + "\n")

def invoke_agent(agent: Agent, topic : str, file_log : str = ""):
    if not topic.strip():
        return

    ts_now = str(datetime.now())

    ts_start = time()
    run_resp = agent.run(topic)
    ts_stop = time()

    elapsed_sec = ts_stop - ts_start
    resp_msg = run_resp.content

    log_response(topic, resp_msg, model_id, ts_now, elapsed_sec, file_log = file_log)
