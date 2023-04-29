#!/usr/bin/python3
"""Init file for package views"""

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

app_views = Blueprint('app_views', __name__, template_folder='templates')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.amenities import *
from api.v1.views.places import *
