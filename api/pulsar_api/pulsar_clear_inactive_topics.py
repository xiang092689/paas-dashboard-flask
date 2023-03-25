import threading
from flask import Blueprint

from pulsar_admin.p_admin import PulsarAdmin

from api.pulsar_api.pulsar_instances import pulsar_instance_map

pulsar_clear_inactive_topics_api = Blueprint('clear_inactive_topic', __name__)


@pulsar_clear_inactive_topics_api.route('/<instance>/clear-inactive-topic', methods=['POST'])
def clear_inactive_topic(instance=None):
    instance_info = pulsar_instance_map.get(instance)
    if instance_info is None:
        return {'message': f'Instance "{instance}" not found'}, 404
    pulsar_admin = PulsarAdmin(instance_info.host, instance_info.web_port)
    threading.Thread(target=do_clear_inactive_topic, args=[pulsar_admin]).start()
    return "OK"


def do_clear_inactive_topic(pulsar_admin: PulsarAdmin):
    tenants: list = pulsar_admin.tenants.get_tenants()
    print(f'got tenant {str(tenants)}')
    for tenant_name in tenants:
        process_namespaces(pulsar_admin, tenant_name)


def process_namespaces(padmin: PulsarAdmin, tenant: str):
    print(f'processing tenant {tenant}')
    tenant_namespace_list: list[str] = padmin.namespaces.get_namespaces(tenant)
    for tenant_namespace_name in tenant_namespace_list:
        [tenant_name, namespace_name] = tenant_namespace_name.split('/')
        process_topics(padmin, tenant_name, namespace_name)


def process_topics(padmin: PulsarAdmin, tenant: str, namespace: str):
    print(f'processing namespace {tenant}/{namespace}')
    tenant_namespace_topic_list: list[str] = padmin.persistent_topics.get_partitioned_topic_list(tenant, namespace)
    for tenant_namespace_topic_name in tenant_namespace_topic_list:
        [_, _, tenant_name, namespace_name, topic_name] = tenant_namespace_topic_name.split('/')
        decide_whether_clear_inactive_topic(padmin, tenant_name, namespace_name, topic_name)


def decide_whether_clear_inactive_topic(padmin: PulsarAdmin, tenant: str, namespace: str, topic: str):
    print(f'processing topic {tenant}/{namespace}/{topic}')
    if not padmin.persistent_topics.get_subscription(tenant, namespace, topic):
        print(f'processing inactive topic {tenant}/{namespace}/{topic}')
        padmin.persistent_topics.delete_partitioned_topic(tenant, namespace, topic)
