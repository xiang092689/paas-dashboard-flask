import os

from flask import Blueprint, jsonify

from module.rocketmq.rocketmq_instance import RocketmqInstance

instance_api = Blueprint('instances', __name__)

rocketmq_instance_map = {}

# Get all Rocketmq instances
# eg: ROCKETMQ_DEFAULT_NAMESRV_ADDR=localhost:9876
#     ROCKETMQ_DEFAULT_CLUSTER=DefaultCluster
prefix_len = len('ROCKETMQ_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('ROCKETMQ_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in rocketmq_instance_map:
        rocketmq_instance_map[name] = RocketmqInstance(name.lower())
    rocketmq_instance = rocketmq_instance_map[name]
    if conf_property == 'NAMESRV_ADDR':
        rocketmq_instance.namesrv_addr = value
    elif conf_property == 'CLUSTER':
        rocketmq_instance.cluster = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(rocketmq_instance_map.values()))
