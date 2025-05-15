from typing import Dict, List, Optional
from nisystemlink.clients.core._uplink._json_model import JsonModel
from ._execution_definition import ExecutionDefinition

class DashboardReference(JsonModel):
    id: Optional[str] = None
    variables: Dict[str, str]

class Dashboard(JsonModel):
    id: Optional[str] = None
    variables: Dict[str, str]

class TestPlanTemplate(JsonModel):
    id: str
    name: str
    summary: str
    templateGroup: str
    productFamilies: List[str]
    partNumbers: List[str]
    description: str
    testProgram: Optional[str]
    systemFilter: Optional[str]
    estimatedDurationInSeconds: Optional[int]
    workspace: str
    createdBy: str
    updatedBy: str
    createdAt: str
    updatedAt: str
    properties: Dict[str, str]
    fileIds: List[str]
    dashboardReference: Optional[DashboardReference] = None
    dashboard: Optional[Dashboard] = None
    executionActions: List[ExecutionDefinition]