import os

from flask import Blueprint, jsonify

from module.redis.redis_instance import RedisInstance

instance_api = Blueprint('instances', __name__)

redis_instance_map = {}

# Get all Redis instances
# eg: REDIS_DEFAULT_URL=redis://localhost:6379
#     REDIS_DEFAULT_CLUSTER_URL=redis://localhost:6379
prefix_len = len('REDIS_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('REDIS_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in redis_instance_map:
        redis_instance_map[name] = RedisInstance(name.lower())
    redis_instance = redis_instance_map[name]
    if conf_property == 'URL':
        redis_instance.url = value
    elif conf_property == 'CLUSTER_URL':
        redis_instance.cluster_url = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(redis_instance_map.values()))
