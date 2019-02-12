from flask import jsonify

from source import app


from .views_general import (
    index,
)


# Errors ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@app.errorhandler(400)
def error_400(error):
    return jsonify({'status': 400, 'message': 'Bad Request'}), 400

@app.errorhandler(401)
def error_401(error):
    return jsonify({'status': 401, 'message': 'Unauthorized'}), 401

@app.errorhandler(403)
def error_403(error):
    return jsonify({'status': 403, 'message': 'Forbidden'}), 403

@app.errorhandler(404)
def error_404(error):
    return jsonify({'status': 404, 'message': 'Not Found'}), 404

@app.errorhandler(405)
def error_405(error):
    return jsonify({'status': 405, 'message': 'Method Not Allowed'}), 405
