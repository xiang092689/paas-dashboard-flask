from flask import Blueprint, jsonify

instances_api = Blueprint('instances', __name__)


@instances_api.route('', methods=['GET'])
def get_instance_list():
    default_instance = {"name": "default"}
    return jsonify([default_instance])
