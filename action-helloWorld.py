#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

name = "&APqvKWgN3mEoXVjPaPqOzQnya8J6G01wdYkOZM9r"


def intent_received(hermes, intent_message):
    sentence = 'Hallo ich funktioniere endlich...'
    if intent_message.intent.intent_name == '&APqvKWgN3mEoXVjPaPqOzQnya8J6G01wdYkOZM9r:mDa':
        dateOfToday = datetime.date.today()
        dateOfReturn = datetime.date(2019, 6, 28)
        timedelta = abs(dateOfToday - dateOfReturn)
        sentence = 'Sie ist in ' + str(timedelta.days) + ' Tagen wieder da.'
    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()