from flask import Blueprint

from api.kubernetes_api.kubernetes_deployments import deployments_api
from api.kubernetes_api.kubernetes_instances import instances_api
from api.kubernetes_api.kubernetes_statefulsets import statefulsets_api

kubernetes_route = Blueprint('kubernetes_route', __name__)
kubernetes_route.register_blueprint(instances_api, url_prefix='/instances')
kubernetes_route.register_blueprint(deployments_api, url_prefix='/instances/default')
kubernetes_route.register_blueprint(statefulsets_api, url_prefix='/instances/default')
