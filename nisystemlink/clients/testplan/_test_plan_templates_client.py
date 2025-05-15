from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients import core

class TestPlanTemplatesClient(BaseClient):
    def __init__(self, client):
        """Initialize an instance.

        Args:
            configuration: Defines the web server to connect to and information about
                how to connect. If not provided, the
                :class:`HttpConfigurationManager <nisystemlink.clients.core.HttpConfigurationManager>`
                is used to obtain the configuration.

        Raises:
            ApiException: if unable to communicate with the WorkOrder Service.
        """
        if configuration is None:
            configuration = core.HttpConfigurationManager.get_configuration()
        super().__init__(configuration, base_path="/niworkorder/v1/")