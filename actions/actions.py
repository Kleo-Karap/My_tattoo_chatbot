# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import requests
import json
import os
from dotenv import load_dotenv

#curl "https://api.airtable.com/v0/appkHyLJUgNtS3bGJ/tblHUOMXM1tEcjk2e" \
#-H "Authorization: Bearer patDUbmxv5SzlZ4uO.65436ccc0154bb7e0b2004f13fc3867b9636f882f867b4f36212005850e3af0e
load_dotenv()

ALLOWED_TATTOO_SIZES = ["x-small", "small", "medium","large", "extra-large", "larger than above"]
ALLOWED_TATTOO_STYLES = ["tribal", "geometric", "japanese", "anime", "minimal","realistic", "old-school"]
#ALLOWED_ARTIST_NAMES=["Persa", "Zoe"]
ALLOWED_BODY_PLACEMENTS= ["arm", "leg", "neck","back", "ankle", "shoulder", "back"]

airtable_api_key= os.getenv("AIRTABLE_API_KEY") 
base_id= os.getenv("BASE_ID")                   
table_name= os.getenv("TABLE_NAME")             

def create_tattoo_log(full_name, e_mail, artist_name, tattoo_style, tattoo_size, body_placement):
    request_url=f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {airtable_api_key}"
    }
    data = {
        "fields": {
            "Full name": full_name,
            "E-mail": e_mail,
            "Artist name": artist_name,
            "Tattoo Style": tattoo_style,
            "Tattoo size": tattoo_size,
            "Body Placement": body_placement
        }
    }

    try:
        response = requests.post(
            request_url, headers=headers, data=json.dumps(data)
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    return response
    print(response.status_code)

class ActionTattooInfoForm(Action):
    def name(self) -> Text:
        return "action_tattoo_info_form"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response= create_tattoo_log(
            tracker.get_slot("full_name"),
            tracker.get_slot("e_mail"),
            tracker.get_slot("artist_name"),
            tracker.get_slot("tattoo_style"),
            tracker.get_slot("tattoo_size"),
            tracker.get_slot("body_placement")
        )
        dispatcher.utter_message("Your answers have been successfull saved")
        return[]

class ValidateTattooInfoForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_tattoo_info_form"
#    def validate_artist_name(
#            self,
#            slot_value: Any,
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: DomainDict,
#    ) -> Dict[Text, Any]:
#        """Validate 'artist_name' value."""

#        if slot_value.lower() not in ALLOWED_ARTIST_NAMES:
#            dispatcher.utter_message(text=f"Persa and Zoe are our two main artists")
#            return {"artist_name": None}
#        dispatcher.utter_message(text=f"{slot_value} will gladly help you with your dream tattoo design")
#        return {"artist_name": slot_value}
    
    def validate_tattoo_size(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'tattoo_size' value."""

        if slot_value.lower() not in ALLOWED_TATTOO_SIZES:
            dispatcher.utter_message(text=f"Accepted tattoo sizes: x-small, small, medium, large, larger than above")
            return {"tattoo_size": None}
        dispatcher.utter_message(text=f"A {slot_value}-sized tattoo")
        return {"tattoo_size": slot_value}
    
    def validate_tattoo_style(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'tattoo_style' value."""

        if slot_value.lower() not in ALLOWED_TATTOO_STYLES:
            dispatcher.utter_message(text=f"Persa tattoo studio is not specialized in this tattoo style, but the team supports: {'/'.join(ALLOWED_TATTOO_STYLES)}.")
            return {"tattoo_style": None}
        dispatcher.utter_message(text=f"A {slot_value} tattoo")
        return {"tattoo_style": slot_value}
    
    def validate_body_placement(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'body_placement' value."""

        if slot_value.lower() not in ALLOWED_BODY_PLACEMENTS:
            dispatcher.utter_message(text=f"Accepted body placements: arm, leg, neck, back, ankle, shoulder, back")
            return {"body_placement": None}
        dispatcher.utter_message(text=f"A(n) {slot_value}-spotted tattoo")
        return {"body_placement": slot_value}




