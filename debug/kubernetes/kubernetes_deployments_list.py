from kubernetes import config, client

namespace = "default"
config.load_kube_config()
v1 = client.AppsV1Api()
deployments_list = v1.list_namespaced_deployment(namespace)
