"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx


from . import  pages, navigation, chat
from .chat import chat_page


class State(rx.State):
    """The app state."""







app = rx.App()
app.add_page(pages.home_page, route=navigation.routes.HOME_ROUTE)
app.add_page(pages.about_us, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(chat.chat_page, route=navigation.routes.CHAT_ROUTE)
app.add_page(chat_page, route="/")
