import random
from string import ascii_lowercase, ascii_uppercase, digits

from flask import abort

from .models import URL_map


STRING: str = "".join((ascii_uppercase, ascii_lowercase, digits))


def get_unique_short_id() -> str:
    while True:
        short_url: str = "".join(random.choices(population=STRING, k=6))
        if not check_original(short_url):
            return short_url


def check_original(target: str):
    obj: URL_map = URL_map.query.filter_by(short=target).first()
    if obj:
        return obj.original
