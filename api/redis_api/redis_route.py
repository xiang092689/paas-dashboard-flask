from flask import Blueprint

from api.redis_api.redis_instances import instance_api

redis_route = Blueprint('redis_route', __name__)
redis_route.register_blueprint(instance_api, url_prefix='/instances')
