from kafka import KafkaAdminClient
from flask import Blueprint, jsonify

from api.kafka_api.kafka_instances import kafka_instance_map

topics_api = Blueprint('topics', __name__)


@topics_api.route('', methods=['GET'])
def get_topics(instance):
    if instance not in kafka_instance_map:
        return {'message': f'Instance "{instance}" not found'}, 404
    instance_config = kafka_instance_map[instance]
    bootstrap_servers = instance_config.bootstrapServers
    admin_client = KafkaAdminClient(
        bootstrap_servers=bootstrap_servers,
        client_id='flask-kafka_api-admin-client'
    )
    topic_names = admin_client.list_topics()
    return jsonify(topic_names)
