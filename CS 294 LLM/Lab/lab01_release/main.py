from typing import Dict, List

import numpy as np
from autogen import ConversableAgent
import sys
import os

def fetch_restaurant_data(restaurant_name: str) -> Dict[str, List[str]]:
    # This function takes in a restaurant name and returns the reviews for that restaurant. 
    # The output should be a dictionary with the key being the restaurant name and the value being a list of reviews for that restaurant.
    # The "data fetch agent" should have access to this function signature, and it should be able to suggest this as a function call. 
    # Example:
    # > fetch_restaurant_data("Applebee's")
    # {"Applebee's": ["The food at Applebee's was average, with nothing particularly standing out.", ...]}
    data = {restaurant_name: []}
    with open("./restaurant-data.txt") as file:
        lines = file.readlines()
        for line in lines:
            name, description = line.replace("\n", "").split(".", 1)[0], line.replace("\n", "").split(".", 1)[1].strip()
            if name == restaurant_name:
                data[restaurant_name].append(description)
    return data


def calculate_overall_score(restaurant_name: str, food_scores: List[int], customer_service_scores: List[int]) -> Dict[str, float]:
    # TODO
    # This function takes in a restaurant name, a list of food scores from 1-5, and a list of customer service scores from 1-5
    # The output should be a score between 0 and 10, which is computed as the following:
    # SUM(sqrt(food_scores[i]**2 * customer_service_scores[i]) * 1/(N * sqrt(125)) * 10
    # The above formula is a geometric mean of the scores, which penalizes food quality more than customer service. 
    # Example:
    # > calculate_overall_score("Applebee's", [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
    # {"Applebee's": 5.048}
    # NOTE: be sure to that the score includes AT LEAST 3  decimal places. The public tests will only read scores that have 
    # at least 3 decimal places.
    result = 0.0
    for i in range(len(food_scores)):
        result += np.sqrt(food_scores[i]**2 * customer_service_scores[i]) * 1 / (len(food_scores) * np.sqrt(125))
    result *= 10
    return {restaurant_name: result}

def get_data_fetch_agent_prompt(restaurant_query: str) -> str:
    # TODO
    # It may help to organize messages/prompts within a function which returns a string. 
    # For example, you could use this function to return a prompt for the data fetch agent 
    # to use to fetch reviews for a specific restaurant.
    return f"Please fetch the reviews for {restaurant_query} from the available dataset."

# TODO: feel free to write as many additional functions as you'd like.

# Do not modify the signature of the "main" function.
def main(user_query: str):
    entrypoint_agent_system_message = "You are a supervisor agent responsible for managing the process of fetching restaurant reviews and calculating their overall score." # TODO
    # example LLM config for the entrypoint agent
    llm_config = {"config_list": [{"model": "gpt-4o-mini", "api_key": os.environ.get("OPENAI_API_KEY")}]}
    # the main entrypoint/supervisor agent
    entrypoint_agent = ConversableAgent("entrypoint_agent", 
                                        system_message=entrypoint_agent_system_message, 
                                        llm_config=llm_config)

    # TODO
    # Create more agents here.
    data_fetch_agent = ConversableAgent(name="data_fetch_agent",
                                        system_message="Fetches the reviews for a specific restaurant.",
                                        llm_config=llm_config,
                                        human_input_mode="NEVER",
                                        max_consecutive_auto_reply=1)

    review_analysis_agent = ConversableAgent(name="review_analysis_agent",
                                        system_message="Analyzes every review restrictly based on the rule below, "
                                                       "generate two dictionaries, the keys are food_score and service_scorelist, values are lists contain scores. Plus, give a restaurant name"
                                             "Score 1/5 has one of these adjectives: awful, horrible, or disgusting."
                                             "Score 2/5 has one of these adjectives: bad, unpleasant, or offensive."
                                             "Score 3/5 has one of these adjectives: average, uninspiring, or forgettable."
                                             "Score 4/5 has one of these adjectives: good, enjoyable, or satisfying."
                                             "Score 5/5 has one of these adjectives: awesome, incredible, or amazing.",
                                        llm_config=llm_config,
                                        human_input_mode="NEVER",
                                        max_consecutive_auto_reply=1)

    scoring_agent = ConversableAgent(name="scoring_agent",
                                        system_message="Score a specific restaurant, providing restaurant_name, food_score, and service_score. "
                                                       "Based on the calculation result, Return in the format of : the average food quality score is xx. in one line",
                                        llm_config=llm_config,
                                        human_input_mode="NEVER")

    data_fetch_agent.register_for_llm(name="fetch_restaurant_data", description="Fetches the reviews for a specific restaurant.")(fetch_restaurant_data)
    scoring_agent.register_for_llm(name="calculate_overall_score", description="calculate overall score")(calculate_overall_score)
    entrypoint_agent.register_for_execution(name="fetch_restaurant_data")(fetch_restaurant_data)
    entrypoint_agent.register_for_execution(name="calculate_overall_score")(calculate_overall_score)


    # TODO
    # Fill in the argument to `initiate_chats` below, calling the correct agents sequentially.
    # If you decide to use another conversation pattern, feel free to disregard this code.
    
    # Uncomment once you initiate the chat with at least one agent.
    result = entrypoint_agent.initiate_chats(
        [
            {
                "recipient": data_fetch_agent,
                "message": user_query,
                "max_turns": 2,
                "summary_method": "last_msg"
            },
            {
                "recipient": review_analysis_agent,
                "message": "These are fetched reviews for the specific restaurant",
                "max_turns": 1,
                "summary_method": "reflection_with_llm",
                "summary_args": {"summary_prompt": "Show the score strictly follows the dictionary format: {restaurant_name: xx,  food_score_list: [], customer_service_score_list: []}"},
            },
            {
                "recipient": scoring_agent,
                "message": "These are scores information for the specific restaurant",
                "max_turns": 2,
            }
        ]
    )
    # print("First Chat Summary: ", result[1].summary)
    
# DO NOT modify this code below.
if __name__ == "__main__":
    assert len(sys.argv) > 1, "Please ensure you include a query for some restaurant when executing main."
    main(sys.argv[1])