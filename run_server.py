""" Script for run project """
from werkzeug.contrib.profiler import ProfilerMiddleware
from source import app
from source.local_settings import DEBUG, SERVER_HOST, SERVER_PORT, SECRET_KEY

app.secret_key = SECRET_KEY

if __name__ == '__main__':
    # app.config['PROFILE'] = True
    # app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[30])
    app.run(
        debug=DEBUG,
        host=SERVER_HOST,
        port=SERVER_PORT,
    )
