from flask import Blueprint, jsonify
from kafka import KafkaAdminClient

from api.kafka.kafka_instances import kafka_instance_map

consumer_groups_api = Blueprint('consumer-groups', __name__)


@consumer_groups_api.route('', methods=['GET'])
def get_consumer_groups(instance):
    if instance not in kafka_instance_map:
        return {'message': f'Instance "{instance}" not found'}, 404
    instance_config = kafka_instance_map[instance]
    bootstrap_servers = instance_config.bootstrapServers
    admin_client = KafkaAdminClient(
        bootstrap_servers=bootstrap_servers,
        client_id='flask-kafka-admin-client'
    )
    groups = admin_client.list_consumer_groups()
    consumer_group_list = [group for group in groups if group[0] == instance]
    return jsonify([group[1] for group in consumer_group_list])
