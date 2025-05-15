from dataclasses import field
from typing import List, Optional, Dict
from nisystemlink.clients.core import ApiError

from nisystemlink.clients.core._uplink._json_model import JsonModel
from ._testplan_template import TestPlanTemplate

class QueryTestPlanTemplatesRequestBody(JsonModel):
    filter: Optional[str] = None
    take: Optional[int] = None
    orderBy: Optional[str] = None
    descending: Optional[bool] = None

class QueryTestPlanTemplatesResponse(JsonModel):
    testPlanTemplates: List[TestPlanTemplate]
    error: Optional[ApiError] = None
