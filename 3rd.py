import re
import random
import datetime
from PIL import Image

bot_template = "HRBot : {0}"

responses = {
    "greet": ['Hello! How can I assist you?'],
    "goodbye": ['Goodbye!', 'Farewell!'],
    "holiday": ['{0}, you can take {1} leaves only.', '{0}, Sorry! You cannot take any leave because you already had so many holidays.',
                'See you on {2}'],
    "affirm": ['Yes', 'Perfect!'],
    "thankyou": ['You are welcome!'],
    "recruitment": ["{0}, Okay! Let's start the process.\nHRBot : What's your name?", 'Tell me about yourself.',
                    "Sorry, we didn't find such a position."]
}

keywords = {'greet': ['Hello!', 'Hi!', 'hello', 'hi', 'hey'],
            'goodbye': ['bye', 'farewell'],
            'thankyou': ['Thanks', 'Thank you', 'thanks', 'thx']
            }

patterns = {}

for intent, keys in keywords.items():
    patterns[intent] = re.compile('|'.join(keys), re.IGNORECASE)


def match_intent(message):
    for intent, pattern in patterns.items():
        if pattern.search(message):
            return intent
    return None


def send_message(message):
    response = respond(message)
    print(bot_template.format(response))


def respond(message):
    intent = match_intent(message)
    if intent == "affirm":
        return random.choice(responses["affirm"])
    elif intent == "holiday":
        # Simulate asking for an employee ID
        id = input("HRBot : Please provide your ID number to check your leave record: ")
        try:
            id = int(id)
            # Simulate checking database for leave record
            leave = 10  # Assume leave count for demo purpose
            if leave == 0:
                return responses["holiday"][1].format("Employee")
            else:
                return responses["holiday"][0].format("Employee", leave)
        except ValueError:
            return "Please enter a valid employee ID."
    elif intent == "recruitment":
        # Simulate recruitment process
        return responses["recruitment"][0].format("HRBot") + "\nUSER: John"
    elif intent == "greet":
        return random.choice(responses["greet"])
    else:
        return "I'm sorry, I couldn't find anything like that"


print("Welcome to HRBot! How can I assist you?")
while True:
    message = input("USER: ")
    if message.lower() == "bye":
        print(bot_template.format("Goodbye!"))
        break
    send_message(message)
