from flask import Blueprint, jsonify, request
from kubernetes import client

deployments_api = Blueprint('deployments', __name__)

v1 = client.AppsV1Api()


@deployments_api.route('/deployments', methods=['GET'])
@deployments_api.route('/namespaces/<namespace>/deployments', methods=['GET'])
def get_deployments(namespace=None):
    # If a namespace was specified, list deployments for that namespace only
    # Otherwise, list deployments for all namespaces
    if namespace:
        deployments_list = v1.list_namespaced_deployment(namespace, watch=False)
    else:
        deployments_list = v1.list_deployment_for_all_namespaces(watch=False)
    return jsonify([deployment.to_dict() for deployment in deployments_list.items])


@deployments_api.route('/namespaces/<namespace>/deployments/<deployment_name>', methods=['POST'])
def patch_deployment(namespace, deployment_name):
    # Get the patch data from the request body
    patch_data = request.get_data()

    # Apply the patch to the deployment
    v1.patch_namespaced_deployment(
        name=deployment_name,
        namespace=namespace,
        body=patch_data,
    )

    # Return a success message
    return 'Deployment patched successfully'


@deployments_api.route('/namespaces/<string:namespace>/deployments/<string:deployment_name>/ready-check',
                       methods=['POST'])
def deployment_ready_check(namespace, deployment_name):
    image = request.args.get('image')
    deployment_list = v1.list_namespaced_deployment(namespace)
    deployment = next((d for d in deployment_list.items if d.metadata.name == deployment_name), None)
    if deployment is None:
        return jsonify({}), 404
    if image and deployment.spec.template.spec.containers[0].image != image:
        return jsonify({}), 406
    if deployment.status and deployment.status.available_replicas != deployment.status.replicas:
        return jsonify({'ready': False}), 200
    return jsonify({'ready': True}), 200
