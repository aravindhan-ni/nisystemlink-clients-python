import pytest
from nisystemlink.clients.testplan import TestPlansClient
from nisystemlink.clients.core._http_configuration import HttpConfiguration

@pytest.fixture(scope="class")
def client(enterprise_config: HttpConfiguration) -> TestPlansClient:
    """Fixture to create a TestPlansClient instance."""
    return TestPlansClient(enterprise_config)