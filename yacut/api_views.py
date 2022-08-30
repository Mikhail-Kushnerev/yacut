import re

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .utils import get_unique_short_id, check_original


pattern = r"^[A-Za-z0-9]{1,16}$"
match = re.compile(pattern)

@app.route("/api/id/<string:short_id>/", methods=("GET",))
def get_link(short_id):
    try:
        target = check_original(short_id)
        if not target:
            raise Exception
    except Exception:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    else:
        return jsonify({"url": target}), 200


@app.route("/api/id/", methods=("POST",))
def push_link():
    data: dict[str, str] = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    elif "url" not in data:
        raise InvalidAPIUsage(f'"url" является обязательным полем!')
    elif "custom_id" not in data or len(data["custom_id"]) == 0:
        data.update({"custom_id": get_unique_short_id()})
    elif len(data["custom_id"]) > 16:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    elif not match.search(data["custom_id"]):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки')
    short: URL_map = URL_map()
    short.from_dict(data)
    db.session.add(short)
    db.session.commit()
    return jsonify(short.to_dict()), 201
