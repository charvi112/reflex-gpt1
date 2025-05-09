import reflex as rx
import sqlalchemy
from datetime import datetime, timezone
from sqlmodel import Field


def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Chat(rx.Model, table=True):
    id: int = Field(default=None, primary_key=True)

    content: str  # User's message
    email: str    # User's email (optional but useful)

    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now()
        },
        nullable=False,
    )

    update_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "onupdate": sqlalchemy.func.now(),
            "server_default": sqlalchemy.func.now()
        },
        nullable=False,
    )
