import random

from .constants import STRING
from .models import URL_map


def get_unique_short_id() -> str:
    while True:
        short_url: str = "".join(random.choices(population=STRING, k=6))
        if not check_original(short_url):
            return short_url


def check_original(target: str):
    obj: URL_map = URL_map.query.filter_by(short=target).first()
    if obj:
        return obj.original
