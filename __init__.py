import sys
from mycroft import MycroftSkill, intent_file_handler
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = 'aio_Krbg85X148ma3n5Hyya5B757A5ZN'
ADAFRUIT_IO_USERNAME = 'Kenzo16'

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect()
client.loop_background()


class FanControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    @intent_file_handler('fan.control.intent')
    def handle_jarvis_introducing(self, message):
        self.speak_dialog('fan.control')
        client.publish('Fan', 1)


def create_skill():
    return FanControl()

