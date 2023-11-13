from rasa_sdk.events import SlotSet
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetAvailableTimeSlots(Action):
    def name(self) -> Text:
        return "action_get_available_time_slots"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        available_time_slots = {
            "Monday 13/11/2023": ["10:00 AM", "11:00 AM", "2:00 PM"],
            "Thursday 16/11/2023": ["9:00 AM", "12:00 PM", "3:00 PM"],
           
        }

        dispatcher.utter_message(text="Available time slots: {}".format(available_time_slots))
        return []
 


class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        return [SlotSet("name", text)]
    
class ActionReceiveDay(Action):

    def name(self) -> Text:
        return "action_receive_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        return [SlotSet("name", text)]
    
class ActionReceiveDate(Action):

    def name(self) -> Text:
        return "action_receive_date"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        return [SlotSet("name", text)]
    
class ActionReceiveTime(Action):

    def name(self) -> Text:
        return "action_receive_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message['text']
        return [SlotSet("name", text)]
    
class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text="I don't know your name.")
        else:
            dispatcher.utter_message(text=f"Ok {name}!")
        return []
    

class ActionConfirmAppointment(Action):
    def name(self) -> Text:
        return "action_confirm_appointment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Extract entities
        day = tracker.get_slot("day")
        date = tracker.get_slot("date")
        time = tracker.get_slot("time")

        if day and date and time:
            response = f"Persa is looking forward to meeting you on {day} {date} at {time}!"
        else:
            response = "It seems there's some missing information. Could you provide the day, date, and time again?"

        # Utter the response
        dispatcher.utter_message(text=response)

        return [] 