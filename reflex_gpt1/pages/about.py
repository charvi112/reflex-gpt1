import reflex as rx

from rxconfig import config

from reflex_gpt1 import ui

def about_us() -> rx.Component:
    # About us page
    return ui.base_layout(
     
        rx.vstack(
            rx.heading("Welcome to Reflex About!", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )