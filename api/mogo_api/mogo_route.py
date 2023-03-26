from flask import Blueprint

from api.mogo_api.mogo_instances import instance_api

mogo_route = Blueprint('mogo_route', __name__)
mogo_route.register_blueprint(instance_api, url_prefix='/instances')
