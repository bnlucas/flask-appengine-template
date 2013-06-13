"""
Initialize Flask app

"""
from flask import Flask

# from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.debug import DebuggedApplication


app = Flask('application')
app.config.from_object('application.settings')

# Enable jinja2 loop controls extension
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

# Pull in URL dispatch routes
import urls

# Flask-DebugToolbar (only enabled when DEBUG=True)
# toolbar = DebugToolbarExtension(app)

# Werkzeug Debugger (only enabled when DEBUG=True)
if app.debug:
    app = DebuggedApplication(app, evalex=True)
