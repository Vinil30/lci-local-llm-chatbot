
from collections import deque

class ChatMemory:
    def __init__(self, max_turns=5):
        self.history = deque(maxlen=max_turns)

    def add_turn(self, user_input, bot_response):
        self.history.append(f"User: {user_input}")
        self.history.append(f"Bot: {bot_response}")

    def get_context(self):
        return "\n".join(self.history)
