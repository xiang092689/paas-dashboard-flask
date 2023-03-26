from flask import Blueprint

from api.rocketmq_api.rocketmq_instances import instance_api

rocketmq_route = Blueprint('rocketmq_route', __name__)
rocketmq_route.register_blueprint(instance_api, url_prefix='/instances')
