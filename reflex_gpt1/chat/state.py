# reflex_gpt1/chat/state.py

from reflex import State, session
from typing import List
from pydantic import BaseModel
from reflex_gpt1.models import Chat as ChatModel
import ollama


# For UI display
class ChatMessage(BaseModel):
    role: str
    content: str


class ChatState(State):
    message: str = ""
    response: str = ""
    messages: List[ChatMessage] = []
    email: str = "user@example.com"  # Set dynamically if needed

    def create_new_chat_session(self):
        with rx.session() as db_session:
            obj = ChatSession()
            db_session.add(obj)
            db_session.commit()
            db_session.refresh(obj)
            self.chat_session = obj

    def clear_and_start_new(self):
        self.chat_session = None
        self.create_new_chat_session()
        self.messages = []
        yield
        

    def on_load(self):
        # Optional: Load previous user messages
        with session() as db:
            results = db.exec(ChatModel.select()).all()
            self.messages = [
                ChatMessage(role="user", content=chat.content) for chat in results
            ]
            print(results)

    def append_message(self, message: str, is_bot: bool = False):
        # Store in DB only if it's a user message
        if not is_bot:
            with session() as db:
                obj = ChatModel(
                    content=message,
                    email=self.email
                )
                db.add(obj)
                db.commit()

        # Append to UI messages
        self.messages.append(
            ChatMessage(role="assistant" if is_bot else "user", content=message)
        )

    def handle_submit(self):
        # Save user message
        self.append_message(self.message, is_bot=False)

        # Get assistant reply from Ollama
        result = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": self.message}]
        )
        self.response = result["message"]["content"]

        # Save assistant reply (not in DB)
        self.append_message(self.response, is_bot=True)

        # Clear input box
        self.message = ""
