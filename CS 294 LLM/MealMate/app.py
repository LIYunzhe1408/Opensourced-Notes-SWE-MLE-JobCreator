import autogen

config_list = [
    {
        'model': 'gpt-4o-mini',
        'api_key': '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'
    }
]

llm_config = {
    "seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10, # Too high, infinite loop
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswitch("TERMINATE"),
    code_execution_config=False,
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved."
)

task = """
Give me a recipe of pasta with tomato sauce
"""

user_proxy.initiate_chat(
    assistant,
    message=task
)

# from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# # Load LLM inference endpoints from an env variable or a file
# # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
# # and OAI_CONFIG_LIST_sample
# # config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
# config_list = [
#     {
#         'model': 'gpt-4o-mini',
#         'api_key': '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'
#     }
# ]
# # You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4', 'api_key': '<your OpenAI API key here>'},]
# assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
# user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
# user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# # This initiates an automated chat between the two agents to solve the task