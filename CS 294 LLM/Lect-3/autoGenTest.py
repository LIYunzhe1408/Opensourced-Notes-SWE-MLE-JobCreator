import os
import autogen
from autogen import AssistantAgent, UserProxyAgent


os.environ["OPENAI_API_KEY"] = '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'
llm_config = {"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}
assistant = AssistantAgent("assistant", llm_config=llm_config)

user_proxy = UserProxyAgent(
    "user_proxy", code_execution_config={"executor": autogen.coding.LocalCommandLineCodeExecutor(work_dir="coding")}
)

# Start the chat
user_proxy.initiate_chat(
    assistant,
    message="Plot a chart of NVDA and TESLA stock price change YTD.",
)