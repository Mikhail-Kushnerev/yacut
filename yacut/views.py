from flask import flash, render_template, redirect, url_for

from . import app, db
from .forms import ShortURLForm
from .models import URL_map


@app.route('/', methods=("GET", "POST"))
def my_index_view():
    form = ShortURLForm()
    if form.validate_on_submit():
        url = form.custom_id.data
        if not url:
            ...
        shorturl = URL_map(
            original=form.original_link.data,
            short=url
        )
        db.session.add(shorturl)
        db.session.commit()
        flash(url_for("short_url", short=url, _external=True))

    return render_template('index.html', form=form)


@app.route('/<string:short>/')
def short_url(short):
    url = URL_map.query.filter_by(short=short).first()
    if url:
        return redirect(url.original)
    raise ...

