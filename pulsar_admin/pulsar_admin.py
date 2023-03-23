from pulsar_admin.clusters import Clusters
from pulsar_admin.http_client import HttpClient


class PulsarAdmin:
    def __init__(self, host, port):
        self.http_client = HttpClient(host, port)
        self.clusters = Clusters(self.http_client)
