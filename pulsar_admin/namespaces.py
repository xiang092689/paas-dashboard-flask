from pulsar_admin.http_client import HttpClient
from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class Namespaces:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client


    def get_tenant_namespaces(self, tenant: str) -> List[str]:
        try:
            response = self.http_client.get(f"{UrlConst.NAMESPACES}/{tenant}")
            if response.status_code != 200:
                raise PulsarAdminException(
                    f"Failed to get namespaces of tenant {tenant}, status code {response.status_code}, "
                    f"body: {response.content}")
            return response.json()
        except Exception as e:
            raise PulsarAdminException(str(e))

    def get_topics(self, tenant: str, namespace: str, mode: Mode, include_system_topic: bool) -> List[str]:
        try:
            params = {"mode": str(mode), "includeSystemTopic": str(include_system_topic)}
            response = self.http_client.get(f"{UrlConst.NAMESPACES}/{tenant}/{namespace}/topics", params=params)
            if response.status_code != 200:
                raise PulsarAdminException(
                    f"Failed to get topics of namespace {tenant}/{namespace}, status code {response.status_code}, "
                    f"body: {response.content}")
            return response.json()
        except Exception as e:
            raise PulsarAdminException(str(e))

    def create_namespace(self, tenant: str, namespace: str) -> None:
        try:
            response = self.http_client.put(f"{UrlConst.NAMESPACES}/{tenant}/{namespace}")
            if response.status_code != 204:
                raise PulsarAdminException(
                    f"Failed to create namespace {tenant}/{namespace}, status code {response.status_code}, "
                    f"body: {response.content}")
        except Exception as e:
            raise PulsarAdminException(str(e))

    def delete_namespace(self, tenant: str, namespace: str, force: bool, authoritative: bool) -> None:
        try:
            params = {"force": str(force), "authoritative": str(authoritative)}
            response = self.http_client.delete(f"{UrlConst.NAMESPACES}/{tenant}/{namespace}", params=params)
            if response.status_code != 204:
                raise PulsarAdminException(
                    f"Failed to delete namespace {tenant}/{namespace}, status code {response.status_code}, "
                    f"body: {response.content}")
        except Exception as e:
            raise PulsarAdminException(str(e))

    def get_backlog_quota_map(self, tenant: str, namespace: str) -> Dict[BacklogQuotaType, BacklogQuota]:
        try:
            response = self.http_client.get(f"{UrlConst.NAMESPACES}/{tenant}/{namespace}{UrlConst.BACKLOG_QUOTA_MAP}")
            if response.status_code != 200:
                raise PulsarAdminException(
                    f"Failed to get backlog quota map of namespace {tenant}/{namespace}, status code "
                    f"{response.status_code}, body: {response.content}")
            return response.json()
        except Exception as e:
            raise PulsarAdminException(str(e))
