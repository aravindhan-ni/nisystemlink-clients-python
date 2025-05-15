from nisystemlink.clients.core._uplink._base_client import BaseClient
from nisystemlink.clients import core
from uplink import Field
from .models._query_testplan_templates import QueryTestPlanTemplatesRequestBody, QueryTestPlanTemplatesResponse 
from nisystemlink.clients.core._uplink._methods import post

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

    @post("/testplan-templates", query=[Field("testplanTemplate")])
    def get_test_plan_template(
        self, testplanTemplate: QueryTestPlanTemplatesRequestBody
    ) -> QueryTestPlanTemplatesResponse:
        """Query test plan templates.

        Args:
            testplanTemplate: The request body containing query parameters for test plan templates.

        Returns:
            QueryTestPlanTemplatesResponse: The response containing the queried test plan templates.
        """