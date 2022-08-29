from flask import url_for

from datetime import datetime

from yacut import db

# video1video2video3video4video5
class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())

    def to_dict(self):
        value = dict(
            url=self.original,
            short_link=url_for(
                "short_url", short=self.short, _external=True
            )
        )
        return value
