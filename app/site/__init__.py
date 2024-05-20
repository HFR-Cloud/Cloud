from flask import blueprints

site = blueprints.Blueprint("site", __name__)

from .site import *
