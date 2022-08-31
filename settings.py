import logging
import os

from yacut.constants import LOG_FORMAT, DT_FORMAT


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default="sqlite:///db.sqlite3"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="qwerty12345")


def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT,
        datefmt=DT_FORMAT,
        handlers=(logging.StreamHandler(),)
    )
