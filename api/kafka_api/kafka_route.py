from flask import Blueprint

from api.kafka_api.kafka_consumer_groups import consumer_groups_api
from api.kafka_api.kafka_instances import instance_api
from api.kafka_api.kafka_topics import topics_api

kafka_route = Blueprint('kafka_route', __name__)
kafka_route.register_blueprint(instance_api, url_prefix='/instances')
kafka_route.register_blueprint(consumer_groups_api, url_prefix='/instances/<instance>/consumer-groups')
kafka_route.register_blueprint(topics_api, url_prefix='/instances/<instance>/topics')
