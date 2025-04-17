import reflex as rx
from .state import ChatState

def chat():
    return rx.container(
        rx.heading("Chat Here", size="6xl"),
        rx.box(
            rx.text(ChatState.message, bg="blue", color="black", padding="1em", border_radius="lg"),
            margin_top="1em",
        ),
        rx.box(
            rx.text(ChatState.response, bg="gray.200", color="black", padding="1em", border_radius="lg"),
            margin_top="1em",
        ),
        rx.input(
            placeholder="Type your message...",
            on_change=ChatState.set_message,
            value=ChatState.message,
            width="100%",
        ),
        rx.button("Submit", on_click=ChatState.submit, color_scheme="blue"),
    )
