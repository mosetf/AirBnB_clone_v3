#!/usr/bin/python3
"""
initialization file for views in REST API
the # noqa is used to address linting errors
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
