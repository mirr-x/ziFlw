#!/usr/bin/python3
import requests
import os


class PrinteDiscord:
    def __init__(self, data):
        self.data = {"content": data}  # Ensure data is in the correct format
        self.url = os.environ['DISCORD_WEBHOOK_URL']
        self.send()

    def send(self):
        response = requests.post(self.url, json=self.data)
        if response.status_code != 204:
            print(f'Failed to send message to Discord: {response.status_code}, {response.text}')
