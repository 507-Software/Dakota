"""
Axis API 2.0 "Ella" is the latest version of the axis api. Allows the user to connect to a hosted llama instance.
"""

import os
import json
import requests

class Memory:
    def __init__(self, memfile):
        """
        Initialize the Memory system with a JSON file.
        """
        self.memory_file = memfile
        self.memory_data = {}
        self.load_memory()

    def load_memory(self):
        """
        Load memory data from the JSON file.
        """
        if os.path.exists(self.memory_file):
            with open(self.memory_file, "r") as file:
                self.memory_data = json.load(file)
        else:
            self.memory_data = {}

    def save_memory(self):
        """
        Save memory data to the JSON file.
        """
        with open(self.memory_file, "w") as file:
            json.dump(self.memory_data, file, indent=4)

    def get(self, key, default=None):
        """
        Retrieve a value from memory by key.
        """
        return self.memory_data.get(key, default)

    def set(self, key, value):
        """
        Set a value in memory by key and save the memory.
        """
        self.memory_data[key] = value
        self.save_memory()

    def delete(self, key):
        """
        Delete a key from memory and save the memory.
        """
        if key in self.memory_data:
            del self.memory_data[key]
            self.save_memory()


class Chat:
    def __init__(self, api_url, headers=None):
        """
        Initialize the Chat system with an API URL and optional headers.
        """
        self.api_url = api_url
        self.headers = headers if headers else {"Content-Type": "application/json"}

    def send_message(self, message):
        """
        Send a message to the AI service and return the response.
        """
        payload = {
            "messages": [{"role": "user", "content": message}]
        }

        try:
            response = requests.post(self.api_url, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP issues
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None