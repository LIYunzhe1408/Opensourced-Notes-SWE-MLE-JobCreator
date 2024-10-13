import os
from typing import Dict, List

from autogen import ConversableAgent

def fetch_restaurant_data(restaurant_name: str) -> Dict[str, List[str]]:
    data = {restaurant_name: []}
    with open("./restaurant-data.txt") as file:
        lines = file.readlines()
        for line in lines:
            name, description = line.replace("\n", "").split(".", 1)[0], line.replace("\n", "").split(".", 1)[1].strip()
            if name == restaurant_name:
                data[restaurant_name].append(description)
    return data


# Let's first define the assistant agent that suggests tool calls.
assistant = ConversableAgent(
    name="Assistant",
    system_message="You are a helpful AI assistant. "
    "You can Fetches the reviews for a specific restaurant. "
    "Return 'TERMINATE' when the task is done.",
    llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ["OPENAI_API_KEY"]}]},
)

# The user proxy agent is used for interacting with the assistant agent
# and executes tool calls.
user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="NEVER",
)

# Register the tool signature with the assistant agent.
assistant.register_for_llm(name="fetch_restaurant_data", description="Fetches the reviews for a specific restaurant.")(fetch_restaurant_data)

# Register the tool function with the user proxy agent.
user_proxy.register_for_execution(name="fetch_restaurant_data")(fetch_restaurant_data)

chat_result = user_proxy.initiate_chat(assistant, message="How good is the food at Subway")

