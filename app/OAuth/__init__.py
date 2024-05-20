from flask import blueprints

oauth = blueprints.Blueprint("oauth", __name__)

from .oauth import *
