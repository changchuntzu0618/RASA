# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import os
import openai


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
    

class ActionGptJoke(Action):

    def name(self) -> Text:
        self.openai=openai
        self.openai.api_key = os.getenv("OPENAI_API_KEY")
        return "action_gpt_joke"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        last_message = tracker.latest_message['text']

        completion = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a joke provider. Provide a new joke everytime to make people happy. Remember, do not provide the joke which is provided before"},
                # {"role": "user", "content":last_message},
            ],
            temperature=1.5,
        )

        answer = completion.choices[0].message["content"]

        dispatcher.utter_message(text=answer)

        return []

