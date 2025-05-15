import pytest

from nisystemlink.clients.testplan.testplan_templates.models._testplan_template import TestPlanTemplate
from nisystemlink.clients.testplan.testplan_templates.models._query_testplan_templates import QueryTestPlanTemplatesRequestBody ,QueryTestPlanTemplatesResponse

class TestTestPlanTemplate:
    def test_get_test_plan_template(self, testplan_templates_client):
        request_body = QueryTestPlanTemplatesRequestBody(
            filter="",
            take=10,
            orderBy="name",
            descending=False
        )

        response = testplan_templates_client.get_test_plan_template(request_body)

        assert isinstance(response, QueryTestPlanTemplatesResponse)

        assert isinstance(response.testPlanTemplates, list)
        for template in response.testPlanTemplates:
            assert isinstance(template, TestPlanTemplate)