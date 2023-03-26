import os

from flask import Blueprint, jsonify

from module.pulsar.pulsar_instance import PulsarInstance

instance_api = Blueprint('instances', __name__)

pulsar_instance_map = {}

# Get all Pulsar instances
# eg: PULSAR_HOST=localhost
#     PULSAR_WEB_PORT=8080
#     PULSAR_TCP_PORT=6650
prefix_len = len('PULSAR_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('PULSAR_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in pulsar_instance_map:
        pulsar_instance_map[name] = PulsarInstance(name.lower())
    pulsar_instance = pulsar_instance_map[name]
    if conf_property == 'HOST':
        pulsar_instance.host = value
    elif conf_property == 'WEB_PORT':
        pulsar_instance.web_port = value
    elif conf_property == 'TCP_PORT':
        pulsar_instance.tcp_port = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(pulsar_instance_map.values()))
