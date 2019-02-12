from source import app, views


app.add_url_rule('/', methods=['GET'], view_func=views.index)


