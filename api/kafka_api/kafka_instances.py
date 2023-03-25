import os

from flask import Blueprint, jsonify

from module.kafka.kafka_instance import KafkaInstance

instance_api = Blueprint('instances', __name__)

kafka_instance_map = {}

# Get all Kafka instances
# eg: KAFKA_DEFAULT_BOOTSTRAP_SERVERS=localhost:9092
prefix_len = len('KAFKA_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('KAFKA_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in kafka_instance_map:
        kafka_instance_map[name] = KafkaInstance(name.lower())
    kafka_instance = kafka_instance_map[name]
    if conf_property == 'BOOTSTRAP_SERVERS':
        kafka_instance.bootstrapServers = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(kafka_instance_map.values()))
