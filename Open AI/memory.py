import json
import os
from langchain.schema import HumanMessage, AIMessage 

class MemoryHandler:
    def __init__(self, memory):
        self.memory = memory
        self.file_path = 'conversation_memory.json'
        self.load_memory()

    def add_user_message(self, message):
        self.memory.add_user_message(message)
        self.save_memory()

    def add_ai_message(self, message):
        self.memory.add_ai_message(message)
        self.save_memory()

    def save_memory(self):
        with open(self.file_path, 'w') as f:
            # Save messages with correct role determination
            json.dump([{'role': 'user', 'content': msg.content} if isinstance(msg, HumanMessage) else 
                        {'role': 'assistant', 'content': msg.content} for msg in self.memory.messages], f)

    def load_memory(self):
        if os.path.exists(self.file_path) and os.path.getsize(self.file_path) > 0:
            try:
                with open(self.file_path, 'r') as f:
                    messages = json.load(f)
                    for msg in messages:
                        role = msg.get('role')
                        content = msg.get('content')

                        if role and content:
                            if role == 'user':
                                self.memory.add_user_message(content)
                            elif role == 'assistant':
                                self.memory.add_ai_message(content)
            except json.JSONDecodeError:
                print("Error: JSON file is invalid, starting with an empty memory.")
                self.memory.messages = []
        else:
            print("No existing memory file found or file is empty, starting fresh.")
            self.memory.messages = []
