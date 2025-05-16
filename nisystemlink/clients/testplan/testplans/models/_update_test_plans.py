from typing import List, Optional, Dict, Any, Union

from nisystemlink.clients.core import ApiError
from nisystemlink.clients.core._uplink._json_model import JsonModel
from . import TestPlan

class UpdateTestPlanRequestBodyContent(JsonModel):
    id: str
    name: Optional[str] = None
    state: Optional[str] = None
    description: Optional[str] = None
    dut_id: Optional[Union[str, None]] = None
    part_number: Optional[str] = None
    assigned_to: Optional[Union[str, None]] = None
    test_program: Optional[Union[str, None]] = None
    properties: Optional[Union[Dict[str, str], None]] = None
    workspace: Optional[Union[str, None]] = None
    work_order_id: Optional[Union[str, None]] = None
    file_ids_from_template: Optional[List[str]] = None

class UpdateTestPlansRequestBody(JsonModel):
    test_plans: List[UpdateTestPlanRequestBodyContent]
    replace: Optional[bool] = None

class UpdateTestPlansResponse(JsonModel):
    updated_test_plans: Optional[List[TestPlan]] = None
    failed_test_plans: Optional[List[UpdateTestPlanRequestBodyContent]] = None
    error: Optional[ApiError] = None
