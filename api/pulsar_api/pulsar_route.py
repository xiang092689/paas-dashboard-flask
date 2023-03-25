from flask import Blueprint

from api.pulsar_api.pulsar_instances import instance_api
from api.pulsar_api.pulsar_clear_inactive_topics import pulsar_clear_inactive_topics_api

pulsar_route = Blueprint('pulsar_route', __name__)
pulsar_route.register_blueprint(instance_api, url_prefix='/instances')
pulsar_route.register_blueprint(pulsar_clear_inactive_topics_api, url_prefix='/instances')
