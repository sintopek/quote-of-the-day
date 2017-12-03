# Quote of the Day skill
# Credits to They Said So.

import requests
#import json 

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'sintopek'
LOGGER = getLogger(__name__)

class QuoteSkill(MycroftSkill):
    def __init__(self):
        super(QuoteSkill, self).__init__(name="QuoteSkill")

    def initialize(self):
        intent = IntentBuilder("QuoteIntent"). \
            require("QuoteKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:
           r = requests.get("https://quotes.rest/qod")
           head = r.json()["contents"]["quotes"][0]
           self.speak_dialog("quote", { 'quote': head["quote"], 'author': head["author"] })
        except:
           self.speak_dialog("not.found")

    def stop(self):
        pass


def create_skill():
    return QuoteSkill()
