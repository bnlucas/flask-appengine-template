Flask on AppFog Project Template
====================================

Boilerplate project template for running a Flask-based application on
AppFog (Python)

Based on the wonderful [flask-appengine-template][fat] by [Kamal Gill][kamalgill]


About Flask
-----------
[Flask][flask] is a BSD-licensed microframework for Python based on
[Werkzeug][wz], [Jinja2][jinja2] and good intentions.

See <http://flask.pocoo.org> for more info.


Setup/Configuration
-------------------
1. Download this repository via
   `git clone git@github.com:bnlucas/flask-appfog-template.git`
   or download the tarball at
   <http://github.com/bnlucas/flask-appfog-template/tarball/master>
2. Copy the src/ folder to your application's root folder
3. Configure datastore models at `src/application/models.py`
4. Configure application views at `src/application/views.py`
5. Configure URL routes at `src/application/urls.py`
6. Configure forms at `src/application/forms.py`
7. Add the secret keys for CSRF protection by running the `generate_keys.py`
   script at `src/application/generate_keys.py`, which will generate the
   secret keys module at src/application/secret_keys.py

Note: Copy the .gitignore file from the tarball folder's root to your git
repository root to keep the secret_keys module out of version control.

Or, add the following to your .(git|hg|bzr)ignore file

<pre class="console">
  # Keep secret keys out of version control
  secret_keys.py
</pre>


Install python dependencies
---------------------------
The local dev environment requires installation of Jinja2, PIL, and simplejson,
which can be installed via:

<pre class="console">
  pip install -r requirements_dev.txt
</pre>


Front-end Customization
-----------------------
1. Customize the main HTML template at
   `src/templates/base.html`
2. Customize CSS styles at `src/static/css/main.css`
3. Add custom JavaScript code at `src/static/js/main.js`
4. Customize favicon at `src/static/img/favicon.ico`
5. Customize 404 page at `src/templates/404.html`


Previewing the Application
--------------------------
<pre class="console">
  wsgi.py
</pre>

The test environment is available at <http://127.0.0.1:5000>


Deploying the Application
-------------------------
To deploy the application to AppFog, use [af update][af]
<pre class="console">
  af login
  af update {APPID}
</pre>

The application should be visible at http://{APPID}.{APPSERVER}.af.cm


Folder structure
----------------
The App Engine app's root folder is located at `src/`.

<pre class="console">
  src/
  |-- application (application code)
  |-- lib/
  |   |-- blinker/ (library for event/signal support)
  |   |-- flask/ (Flask core)
  |   |-- flask_cache/  (Flask-Cache extension)
  |   |-- flask_debugtoolbar/  (Port of Django Debug Toolbar to Flask)
  |   |-- flaskext/ (Flask extensions go here)
  |   |-- jinja2/ (Jinja2 Templateing)
  |   |-- werkzeug/ (WSGI utilities for Python-based web development)
  |   `-- wtforms/ (Jinja2-compatible web form utility)
  |-- tests/ (unit tests)
  |-- static/
  |   |-- css/
  |   |   |-- bootstrap-*.css (Twitter Bootstrap styles)
  |   |   |-- fontawesome-*.css (Fontawesome styles)
  |   |   `-- main.css (custom styles)
  |   |-- font/
  |   |   `various fontawesome font files
  |   |-- img/
  |   |   |-- favicon.ico
  |   |   |-- favicon.png
  |   |   `-- glyphicons-*.png (Twitter bootstrap icons sprite)
  |   `-- js/
  |       |-- main.js (site-wide JS)
  |       `-- lib/ (third-party JS libraries)
  |           |--bootstrap-*.js (Bootstrap jQuery plugins
  |           `--modernizer-*.js (HTML5 detection library)
  |-- templates/
  |   |-- includes/ (common include files)
  |   |-- 404.html (not found page)
  |   |-- 500.html (server error page)
  |   `-- base.html (master template)
</pre>

The application code is located at `src/application`.

<pre class="console">
  application/
  |-- __init__.py (initializes Flask app)
  |-- decorators.py (decorators for URL handlers)
  |-- forms.py (web form models and validators)
  |-- generate_keys.py (generate CSRF and session keys)
  |-- models.py (App Engine datastore models)
  |-- settings.py (settings for Flask app)
  |-- urls.py (URL dispatch routes)
  `-- views.py (Handlers for URL routes defined at urls.py)
</pre>


Removing Extended Attributes (@ flag)
-------------------------------------
A few of the files in the source tree were uploaded (with apologies) to
GitHub with extended attributes (notice the '@' symbol when running ls -al).

To remove the extended attributes, use `xattr -rd` at the root of the
src/ folder.

<pre class='console'>
  xattr -rd com.apple.quarantine .
  xattr -rd com.macromates.caret .
</pre>

Note: Windows users may safely ignore the xattr fix


Licenses
--------
See licenses/ folder


Package Versions
----------------
- Blinker: 1.1
- Bootstrap: 2.3.1 (set in base.html)
- Flask: 0.9
- Flask-Cache 0.10.1
- Flask-DebugToolbar: 0.7.1
- Flask-WTF: 0.6
- FontAwesome: 3.0
- Jinja2: 2.6
- jQuery: 1.9.1 (set in base.html)
- Modernizr: 2.6.2 (set in base.html)
- Werkzeug: 0.8.3
- WTForms: 1.0.4


Credits
-------
This is an AppFog port of [Kamal Gill's][kamalgill]
[flask-appengine-template][fat]

Project template layout was heavily inspired by Francisco Souza's
[gaeseries Flask project][gaeseries]

Incorporates [Flask-DebugToolbar][debugtoolbar] by Matt Good et. al.
and [Flask-Cache][flaskcache] by Thadeus Burgess

Layout, form, table, and button styles provided by [Bootstrap][bootstrap]

[Font Awesome][fontawesome] by Dave Gandy

HTML5 detection provided by [Modernizr 2][modernizr] (configured with all features)


[appcfg]: http://code.google.com/appengine/docs/python/tools/uploadinganapp.html
[bootstrap]: http://twitter.github.com/bootstrap
[debugtoolbar]: https://readthedocs.org/projects/flask-debugtoolbar/
[devserver]: http://code.google.com/appengine/docs/python/tools/devserver.html
[flask]: http://flask.pocoo.org
[flaskcache]: http://pythonhosted.org/Flask-Cache/
[fontawesome]: http://fortawesome.github.com/Font-Awesome/
[html5]: http://html5boilerplate.com/
[jinja2]: http://jinja.pocoo.org/2/documentation/
[gaeseries]: http://github.com/franciscosouza/gaeseries/tree/flask
[modernizr]: http://www.modernizr.com/
[profiler]: http://packages.python.org/Flask-GAE-Mini-Profiler/
[wz]: http://werkzeug.pocoo.org/
[wzda]: https://github.com/nshah/werkzeug-debugger-appengine
[kamalgill]: https://github.com/kamalgill
[fat]: https://github.com/kamalgill/flask-appengine-template
[af]: https://docs.appfog.com/getting-started/af-cli
