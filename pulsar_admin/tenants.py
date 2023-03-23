from http_client import HttpClient
from pulsar_admin.pulsar_admin_exception import PulsarAdminException
from pulsar_admin.url_const import UrlConst


class Tenants:
    def __init__(self, http_client: HttpClient):
        self.http_client = http_client

    def create_tenant(self, tenant, tenant_info):
        try:
            response = self.http_client.put(
                f"{UrlConst.TENANTS}/{tenant}",
                data=tenant_info
            )
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to create tenant {tenant}, status code {response.status_code}, body: {response.text}")
        except Exception as e:
            raise PulsarAdminException(e)

    def delete_tenant(self, tenant, force):
        try:
            response = self.http_client.delete(
                f"{UrlConst.TENANTS}/{tenant}",
                params={"force": str(force)}
            )
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to delete tenant {tenant}, status code {response.status_code}, body: {response.text}")
        except Exception as e:
            raise PulsarAdminException(e)

    def update_tenant(self, tenant, tenant_info):
        try:
            response = self.http_client.post(
                f"{UrlConst.TENANTS}/{tenant}",
                data=tenant_info
            )
            if response.status_code != 204:
                raise PulsarAdminException(f"failed to update tenant {tenant}, status code {response.status_code}, body: {response.text}")
        except Exception as e:
            raise PulsarAdminException(e)

    def get_tenant_admin(self, tenant):
        try:
            response = self.http_client.get(f"{UrlConst.TENANTS}/{tenant}")
            if response.status_code != 200:
                raise PulsarAdminException(f"failed to get tenant {tenant}, status code {response.status_code}, body: {response.text}")
            return JacksonService.toObject(response.text, TenantInfo)
        except Exception as e:
            raise PulsarAdminException(e)

    def get_tenants(self):
        try:
            response = self.http_client.get(UrlConst.TENANTS)
            if response.status_code != 200:
                raise PulsarAdminException(f"failed to get list of tenants, status code {response.status_code}, body: {response.text}")
            return JacksonService.toList(response.text, List[str])
        except Exception as e:
            raise PulsarAdminException(e)
