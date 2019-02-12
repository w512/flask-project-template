import datetime

from flask import (
    g,
    request,
    jsonify,
    abort,
    session,
    redirect,
    url_for,
    render_template,
)



def index():
    date = datetime.datetime.now()

    return render_template(
        'index.html', 
        date=date,
    )

