from functools import wraps
from flask import request, session, abort, redirect, url_for
from source import app
from source.local_settings import DEBUG


def auth_required(view):
    @wraps(view)
    def decorated_function(*args, **kwargs):
        user = session.get('user')
        if not user:
            if request.path.startswith('/api/'):
                return abort(401)
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return decorated_function
    
    
@app.before_request
def before_request():
    if DEBUG:
        print(request.method, request.path)