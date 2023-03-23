from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class PersistentTopics:
    BASE_URL_PERSISTENT_DOMAIN = UrlConst.BASE_URL_V2 + "/persistent"

    def __init__(self, http_client):
        self.http_client = http_client

    def get_domain_base_url(self):
        return self.BASE_URL_PERSISTENT_DOMAIN

    def create_partitioned_topic(self, tenant, namespace, encoded_topic, num_partitions,
                                 create_local_topic_only):
        url = f"{self.get_domain_base_url()}/{tenant}/{namespace}/{encoded_topic}{UrlConst.PARTITIONS}"
        try:
            response = self.http_client.put(url, data={'numPartitions': num_partitions,
                                                       'createLocalTopicOnly': create_local_topic_only})
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to create partitioned topic {tenant}/{namespace}/{encoded_topic}, "
                                           f"status code {response.status_code}, body: {response.text}")
        except (requests.exceptions.RequestException, PulsarAdminException) as e:
            raise PulsarAdminException(str(e)) from e

    def delete_partitioned_topic(self, tenant, namespace, encoded_topic, force, authoritative):
        url = f"{self.get_domain_base_url()}/{tenant}/{namespace}/{encoded_topic}{UrlConst.PARTITIONS}"
        try:
            response = self.http_client.delete(url, params={'force': force,
                                                             'authoritative': authoritative})
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to delete partitioned topic {tenant}/{namespace}/{encoded_topic}, "
                                           f"status code {response.status_code}, body: {response.text}")
        except (requests.exceptions.RequestException, PulsarAdminException) as e:
            raise PulsarAdminException(str(e)) from e

    def update_partitioned_topic(self, tenant, namespace, encoded_topic,
                                  update_local_topic_only, authoritative, force, num_partitions):
        url = f"{self.get_domain_base_url()}/{tenant}/{namespace}/{encoded_topic}{UrlConst.PARTITIONS}"
        try:
            response = self.http_client.post(url, data={'numPartitions': num_partitions,
                                                        'updateLocalTopicOnly': update_local_topic_only,
                                                        'authoritative': authoritative,
                                                        'force': force})
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to update partitioned topic {tenant}/{namespace}/{encoded_topic}, "
                                           f"status code {response.status_code}, body: {response.text}")
        except (requests.exceptions.RequestException, PulsarAdminException) as e:
            raise PulsarAdminException(str(e)) from e

    def get_partitioned_metadata(self, tenant, namespace, encoded_topic, check_allow_auto_creation, authoritative):
        url = f"{self.get_domain_base_url()}/{tenant}/{namespace}/{encoded_topic}{UrlConst.PARTITIONS}"
        try:
            response = self.http_client.get(url, params={'checkAllowAutoCreation': check_allow_auto_creation,
                                                          'authoritative': authoritative})
            if response.status_code != 200:
                raise PulsarAdminException(f"failed to get partitioned topic metadata {tenant}/{namespace}/{encoded_topic}, "
                                           f"status code {response.status_code}, body: {response.text}")
            return JacksonService.toObject(response.text, PartitionedTopicMetadata)
        except (requests.exceptions.RequestException, PulsarAdminException) as e:
            raise PulsarAdminException(str(e)) from e
