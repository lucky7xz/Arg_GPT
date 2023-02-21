from typing import List, Tuple
from chatgpt_wrapper import ChatGPT

def extract_arguments(text: str) -> List[dict]:
    # Set up ChatGPT
    chatbot = ChatGPT()
    prompt = "Extract arguments:"

    # Initialize list to hold extracted arguments
    arguments = []

    # Generate prompts and extract arguments for each sentence in the input text
    for i, sentence in enumerate(text.split(".")):
        # Generate prompt for current sentence
        message = f"{prompt} {sentence.strip()}"

        # Send prompt to ChatGPT and receive response
        response = chatbot.ask(message)

        # Parse response and add argument to list
        if response.startswith("Claim:"):
            claim = response.replace("Claim:", "").strip()
            if i > 0:
                # If this is not the first sentence, add previous sentence as premise
                premise = text.split(".")[i-1].strip()
                arguments.append({
                    "claim": claim,
                    "premise": premise
                })
            else:
                # If this is the first sentence, add claim with empty premise
                arguments.append({
                    "claim": claim,
                    "premise": ""
                })

    return arguments