from flask import Blueprint

from api.pulsar.pulsar_instances import instance_api

pulsar_route = Blueprint('pulsar_route', __name__)
pulsar_route.register_blueprint(instance_api, url_prefix='/instances')
