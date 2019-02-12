import logging
from flask import Flask, g, jsonify



app = Flask(__name__, static_url_path='/static', static_folder='../static',)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


import source.views
import source.routes
