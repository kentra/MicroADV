import os, sys, io
import M5
from M5 import *
from umqtt import MQTTClient
import time
from app.states import AppState
import asyncio


class MQTTTool:
    def __init__(self):
        self.mqtt_client: MQTTClient = MQTTClient(
            "MiniADV",
            "10.217.1.3",
            port=1883,
            user="esp32",
            password="esp32",
            keepalive=0,
            ssl=False,
        )

        # self.mqtt_client.disconnect()
        # self.mqtt_client.reconnect()

    async def connect(self):
        self.mqtt_client.connect(clean_session=True)
        while not self.mqtt_client.isconnected():
            AppState.mqtt_connected = self.mqtt_client.isconnected()
            if AppState.mqtt_connected:
                print("Connected to MQTT broker!")
                break
            asyncio.sleep_ms(1000)

    async def publish(self, topic, message):
        if AppState.mqtt_connected:
            self.mqtt_client.publish(topic, message, qos=0, retain=False)

    async def subscribe(self, topic):
        if AppState.mqtt_connected:
            self.mqtt_client.subscribe("esp/cardputer", self.callback, qos=0)

    async def callback(self, callback):
        if AppState.mqtt_connected:
            print(f"MQTT Message received: {callback}")

    async def check_msg(self, attempts: int = 2) -> None:
        if AppState.mqtt_connected:
            await self.mqtt_client.check_msg(attempts=attempts)
