import os

from kubernetes import config

if os.getenv('KUBERNETES_DEFAULT_CONFIG_TYPE') == 'cluster':
    config.load_incluster_config()
else:
    config.load_kube_config()
