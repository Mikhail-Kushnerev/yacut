import os


class Config:
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "DATABASE_URI",
        default="sqlite:///db.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SECRET_KEY: str = os.getenv("SECRET_KEY", default="qwerty12345")
