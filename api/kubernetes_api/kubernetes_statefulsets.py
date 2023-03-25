from flask import Blueprint, jsonify, request
from kubernetes import client

statefulsets_api = Blueprint('statefulsets', __name__)

v1 = client.AppsV1Api()


@statefulsets_api.route('/stateful-sets', methods=['GET'])
@statefulsets_api.route('/namespaces/<namespace>/stateful-sets', methods=['GET'])
def get_deployments(namespace=None):
    # If a namespace was specified, list deployments for that namespace only
    # Otherwise, list deployments for all namespaces
    if namespace:
        statefulsets_list = v1.list_namespaced_stateful_set(namespace, watch=False)
    else:
        statefulsets_list = v1.list_stateful_set_for_all_namespaces(watch=False)
    return jsonify([statefulset.to_dict() for statefulset in statefulsets_list.items])


@statefulsets_api.route('/namespaces/<namespace>/stateful-sets/<statefulset_name>', methods=['POST'])
def patch_statefulset(namespace, statefulset_name):
    # Get the patch data from the request body
    patch_data = request.get_data()

    # Apply the patch to the stateful set
    v1.patch_namespaced_stateful_set(
        name=statefulset_name,
        namespace=namespace,
        body=patch_data,
    )

    # Return a success message
    return 'Stateful set patched successfully'


@statefulsets_api.route('/namespaces/<string:namespace>/stateful-sets/<string:stateful_set_name>/ready-check',
                        methods=['POST'])
def ready_check(namespace, stateful_set_name):
    image = request.args.get('image')
    stateful_sets = v1.list_namespaced_stateful_set(namespace, watch=False)
    stateful_set = next((s for s in stateful_sets.items() if s.metadata.name == stateful_set_name), None)
    if stateful_set is None:
        return jsonify({}), 404
    if image and stateful_set.spec.template.spec.containers[0].image != image:
        return jsonify({}), 406
    if stateful_set.status and stateful_set.status.available_replicas != stateful_set.status.replicas:
        return jsonify({'ready': False}), 200
    return jsonify({'ready': True}), 200
