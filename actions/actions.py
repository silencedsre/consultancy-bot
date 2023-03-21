# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import logging

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict
from rasa.shared.core.events import UserUttered, ActionExecuted
from rasa_sdk.executor import CollectingDispatcher

logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)

logger.error("Started")

VALID_BACHELORS = [
    "bachelors",
    "bachelor",
    "undergraduate",
    "undergrad"
]

VALID_MASTERS = [
    "masters",
    "master"
    "graduate",
    "grad"
]

VALID_ACADEMICS = VALID_MASTERS + VALID_BACHELORS

VALID_COUNTRY = [
    "usa",
    "us",
    "united states",
    "canada",
    "australia",
]


class Validate_Country_Academics_Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_country_academics_form"

    def validate_academics(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `academics` value."""

        # buttons = [
        #     {"title": "Bachelors", "payload": "/academics"},
        #     {"title": "Masters", "payload": "/academics"},
        # ]

        if slot_value.lower() not in VALID_ACADEMICS:
            dispatcher.utter_message(
                text=f"We only accept: Bachelors and Masters.",
            )
            return {"academics": None}
        return {"academics": slot_value}

    def validate_country(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `country` value."""

        # buttons = [
        #     {"title": "USA", "payload": "/country"},
        #     {"title": "Australia", "payload": "/country"},
        #     {"title": "Canada", "payload": "/country"},
        # ]

        if slot_value.lower() not in VALID_COUNTRY:
            dispatcher.utter_message(
                text=f"We only work with {'/'.join(VALID_COUNTRY)}."
            )
            return {"country": None}
        # dispatcher.utter_message(text=f"OK! You want to join in {slot_value}")
        return {"country": slot_value}

class Validate_Country_Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_country_form"

    def validate_country(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `country` value."""

        if slot_value.lower() not in VALID_COUNTRY:
            dispatcher.utter_message(text=f"We only work with {'/'.join(VALID_COUNTRY)}.")
            return {"country": None}
        return {"country": slot_value}


class Validate_Lead_gen_Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_lead_generation_form"

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `name` value."""

        logger.info(f"The name is: {slot_value}")
        return {"name": slot_value}

    def validate_number(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `number` value."""

        logger.info(f"The number is: {slot_value}")
        return {"number": slot_value}

class ActionIELTS_Score(Action):

    def name(self) -> Text:
        return "action_ielts_score"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        text = tracker.latest_message
        academics = tracker.get_slot("academics")
        country = tracker.get_slot("country")
        intent = tracker.get_intent_of_latest_message()

        logger.info(f"The current intent:{intent}")
        logger.info(f"Academics: {academics}")
        logger.info(f"Country: {country}")

        if academics.lower() in VALID_BACHELORS:
            dispatcher.utter_message(text="GPA 2.60 and above and IELTS 6.0 not less 5.5")

        elif  academics.lower() in VALID_MASTERS:
            dispatcher.utter_message(text="GPA 2.65 and above and IELTS 6.5 not less than 6")

        else:
            dispatcher.utter_message(text="Invalid request")

        slots = [
            SlotSet("academics", None),
            SlotSet("country", None),
        ]

        return slots

class Action_Working_Hour(Action):

    def name(self) -> Text:
        return "action_working_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        academics = tracker.get_slot("academics")
        country = tracker.get_slot("country")
        intent = tracker.get_intent_of_latest_message()

        logger.info(f"The current intent:{intent}")
        logger.info(f"Academics: {academics}")
        logger.info(f"Country: {country}")

        dispatcher.utter_message(text=f"You are allowed to work 20 hours a week for {academics} in {country}")

        slots = [
            SlotSet("academics", None),
            SlotSet("country", None),
        ]

        return slots

class Action_Scholorships(Action):

    def name(self) -> Text:
        return "action_scholorships"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        academics = tracker.get_slot("academics")
        country = tracker.get_slot("country")
        intent = tracker.get_intent_of_latest_message()

        logger.info(f"The current intent:{intent}")
        logger.info(f"Academics: {academics}")
        logger.info(f"Country: {country}")

        dispatcher.utter_message(text=f"Yes, depending upon GPA and IELTS Score you have. We will request universities on your behalf to provide best scholarship possible.")

        slots = [
            SlotSet("academics", None),
            SlotSet("country", None),
        ]

        return slots


class Action_Cost_to_Apply(Action):

    def name(self) -> Text:
        return "action_cost_to_apply"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        academics = tracker.get_slot("academics")
        country = tracker.get_slot("country")
        intent = tracker.get_intent_of_latest_message()

        logger.info(f"The current intent:{intent}")
        logger.info(f"Academics: {academics}")
        logger.info(f"Country: {country}")

        dispatcher.utter_message(text=f"It depends on the state and universities you chose. For pursuing {academics} in {country}, you will need this amount: (Some Amount in NRS.)")

        slots = [
            SlotSet("academics", None),
            SlotSet("country", None),
        ]

        return slots

class Action_Visa_Processing_Time(Action):

    def name(self) -> Text:
        return "action_visa_processing_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        academics = tracker.get_slot("academics")
        country = tracker.get_slot("country")
        intent = tracker.get_intent_of_latest_message()

        logger.info(f"The current intent:{intent}")
        logger.info(f"Academics: {academics}")
        logger.info(f"Country: {country}")

        dispatcher.utter_message(text=f"It depends on university and documents you have provided but in general we are getting visa in 35 days.")

        slots = [
            SlotSet("academics", None),
            SlotSet("country", None),
        ]

        return slots
