import json
import random
from DEPI_AMIT_AI.src.python.session4.code.response import responses


# with open("responses.json", "r") as file:
  #  responses = json.load(file)


def chatbot(message):
    message = message.lower().strip()

    if message in responses:
        return random.choice(responses[message])

    return random.choice([
        "Sorry, I don't understand.",
        "Can you rephrase that?",
        "I don't know what you mean."
    ])


while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    print("Bot:", chatbot(user))