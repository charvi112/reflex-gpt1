# reflex_gpt1/chat/page.py

import reflex as rx
from .state import ChatState

def chat_page():
    return rx.container(
        rx.heading("Chat Here", size="5"),
        rx.button(" + New Chat", on_click= ChatState. clear_and_start_new),
        rx.vstack(
            rx.foreach(
                ChatState.messages,
                lambda msg: rx.box(
                    msg.content,
                    bg=rx.cond(msg.role == "user", "#0d6efd", "#e4e4e7"),
                    color=rx.cond(msg.role == "user", "white", "black"),
                    p="4",
                    border_radius="lg",
                    align_self=rx.cond(msg.role == "user", "flex-end", "flex-start"),
                    max_width="60%",
                    mb="2",
                )
            ),
            spacing="4",
            align_items="stretch",
        ),
        rx.hstack(
            rx.input(
                value=ChatState.message,
                placeholder="Type a message...",
                on_change=ChatState.set_message,
                width="100%",
            ),
            rx.button("Submit", on_click=ChatState.handle_submit),
            spacing="2",
            width="100%",
        ),
        spacing="4",
        padding="4",
        width="100%",
        align_items="center",
    )
