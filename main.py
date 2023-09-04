from textbase import bot, Message
from textbase.models import OpenAI
from typing import List
import openai


# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a vacation bot. I can help you plan your vacation!
"""

@bot()
def on_message(message_history: List[Message], state: dict = ""):

    # Extract the last user message
    user_message = message_history[-1].content.lower()

    # Initialize conversation state if it's the first message
    if state is None:
        state = {
            "destination": None,
            "budget": None,
            "duration": None,
            "season": None,
        }

    # Check user's intent and respond accordingly
    if "hi" in user_message:
        print("hi I'm travel chatbot")
    if "recommend hotel" in user_message:
        state["destination"] = None  # Reset destination for hotel recommendation
        bot_response = "Sure, I can recommend hotels for you. Please tell me your destination."
    elif state["destination"] is None:
        state["destination"] = user_message
        bot_response = f"Great! You want to travel to {state['destination']}. When do you plan to go?"
    elif state["season"] is None:
        state["season"] = user_message
        bot_response = "Got it! Now, please tell me your budget for the trip."
    elif state["budget"] is None:
        state["budget"] = user_message
        bot_response = "Thanks! How many days do you plan to stay?"
    elif state["duration"] is None:
        state["duration"] = user_message
        bot_response = (
            f"Perfect! You want to stay in {state['destination']} for {state['duration']} days."
            "I will now recommend hotels and attractions based on your preferences."
            # You can add code here to recommend hotels and attractions based on the user's inputs
        )
    else:
        bot_response = "I'm here to help plan your vacation. Feel free to ask any questions or specify your preferences."
        

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }