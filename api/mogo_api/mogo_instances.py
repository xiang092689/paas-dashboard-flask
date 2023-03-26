import os

from flask import Blueprint, jsonify

from module.mogo.mogo_instance import MogoInstance

instance_api = Blueprint('instances', __name__)

mogo_instance_map = {}

# Get all Mogo instances
# eg: MOGO_DEFAULT_HOST=localhost
#     MOGO_DEFAULT_PORT=27017
prefix_len = len('MOGO_')
env_map = {k[prefix_len:]: v for k, v in os.environ.items() if k.startswith('MOGO_')}
for key, value in env_map.items():
    index = key.index('_')
    name = key[:index].lower()
    conf_property = key[index + 1:]
    if name not in mogo_instance_map:
        mogo_instance_map[name] = MogoInstance(name.lower())
    mogo_instance = mogo_instance_map[name]
    if conf_property == 'HOST':
        mogo_instance.host = value
    elif conf_property == 'PORT':
        mogo_instance.port = value


@instance_api.route('', methods=['GET'])
def get_instance_list():
    return jsonify(list(mogo_instance_map.values()))
