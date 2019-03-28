#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hermes_python.hermes import Hermes
from datetime import datetime

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

name = "&APqvKWgN3mEoXVjPaPqOzQnya8J6G01wdYkOZM9r"


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def intent_received(hermes, intent_message):
    sentence = 'Hallo ich funktioniere endlich...'
    if intent_message.intent.intent_name == '&APqvKWgN3mEoXVjPaPqOzQnya8J6G01wdYkOZM9r:mDa':
        print('mDa')
        sentence = 'Sie ist in' + days_between(datetime.date, "2019-06-28") + 'wieder da.'

    # else:
    #     return

    # forecast_country_slot = intent_message.slots.forecast_country.first()
    # forecast_locality_slot = intent_message.slots.forecast_locality.first()
    # forecast_start_datetime_slot = intent_message.slots.forecast_start_datetime

    # if forecast_locality_slot is not None:
    #     sentence += 'in ' + forecast_locality_slot.value
    # if forecast_country_slot is not None:
    #     sentence += 'in ' + forecast_country_slot.value
    # if forecast_start_datetime_slot is not None and len(forecast_start_datetime_slot) > 0:
    #     sentence += ' ' + forecast_start_datetime_slot[0].raw_value

    hermes.publish_end_session(intent_message.session_id, sentence)


with Hermes(MQTT_ADDR) as h:
    h.subscribe_intents(intent_received).start()