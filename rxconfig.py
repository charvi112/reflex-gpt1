import reflex as rx
from decouple import config

DATABASE_URL = config("DATABASE_URL")
API_URL = config("API_URL", default="http://localhost:8000")  # <-- Add this line

config = rx.Config(
    app_name="reflex_gpt1",
    db_url=DATABASE_URL,
    api_url=API_URL,  # <-- And this line
)
