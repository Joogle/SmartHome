#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

name = "&APqvKWgN3mEoXVjPaPqOzQnya8J6G01wdYkOZM9r"
sentence = ''


def intent_received(hermes, intent_message):
    if intent_message.intent.intent_name == name + ':mDa':
        dateOfToday = datetime.date.today()
        dateOfReturn = datetime.date(2019, 6, 28)
        timedelta = abs(dateOfToday - dateOfReturn)
        sentence = 'Sie ist in ' + str(timedelta.days) + ' Tagen wieder da.'
    if intent_message.intent.intent_name == name + ':Lichtsteuerung':
        python_obj = json.loads(intent_message)
        for slot in python_obj["slots"]:
            if slot["slot_name"] == "Licht":
                licht = slot["value"]["value"]
            elif slot["slot_name"] == "an_aus":
                an_aus = slot["value"]["value"]
        sentence = 'Ok, mache' + licht + an_aus
    hermes.publish_end_session(intent_message.session_id, sentence)

if __name__ == "__main__":
    with Hermes(MQTT_ADDR) as h:
        h.subscribe_intents(intent_received).start()