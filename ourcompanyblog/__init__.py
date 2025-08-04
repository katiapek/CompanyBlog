# ourcompanyblog/__init__.py

from flask import Flask

app = Flask(__name__)

# Import Blueprints
from ourcompanyblog.core.views import core
from ourcompanyblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)