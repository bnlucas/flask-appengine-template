"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
import os

from flask import request, render_template, flash, url_for, redirect, send_file, send_from_directory

from flask_cache import Cache

from application import app
# from decorators import login_required, admin_required
# from forms import ExampleForm
# from models import ExampleModel


# Flask-Cache (configured to use Flask_Cahce simple) ## redis default soon.
cache = Cache(app)

def home():
    return 'welcome to appfog!'


def say_hello(username):
    """Contrived example to demonstrate Flask's url routing capabilities"""
    return 'Hello %s' % username


def af_env():
    return os.environ.get("VCAP_SERVICES", "{}")


## Static files
# favicon.ico
@app.route('/favicon.ico')
def favicon():
	return static('img/favicon.ico')

# robots.txt
@app.route('/robots.txt')
def robots():
	return static('robots.txt')

# static file
@app.route('/static/<filename>')
def static(filename):
	if '..' in filename or filename.startswith('/'):
		abort(404)
	try:
		static_path = os.path.join(app.root_path, 'static')
		return send_from_directory(static_path, filename)
	except IOError:
		abort(404)
