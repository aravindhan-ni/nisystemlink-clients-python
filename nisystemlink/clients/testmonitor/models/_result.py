from datetime import datetime
from typing import Dict, List, Optional

from nisystemlink.clients.core._uplink._json_model import JsonModel
from nisystemlink.clients.testmonitor.models._status import Status, StatusType
from pydantic import ConfigDict


class Result(JsonModel):
    """Contains information about a result."""

    status: Optional[Status] = None
    """The status of the result."""

    started_at: Optional[datetime] = None
    """The time that the result started."""

    updated_at: Optional[datetime] = None
    """The last time that this result was updated."""

    program_name: Optional[str] = None
    """The name of the program that generated this result."""

    id: Optional[str] = None
    """The globally unique id of the result."""

    system_id: Optional[str] = None
    """The id of the system that generated this result."""

    host_name: Optional[str] = None
    """The name of the host that generated this result."""

    part_number: Optional[str] = None
    """The part number is the unique identifier of a product within a single org."""

    serial_number: Optional[str] = None
    """The serial number of the system that generated this result."""

    total_time_in_seconds: Optional[float] = None
    """The total time that the result took to run in seconds."""

    keywords: Optional[List[str]] = None
    """A list of keywords that categorize this result."""

    properties: Optional[Dict[str, Optional[str]]] = None
    """A list of custom properties for this result."""

    operator: Optional[str] = None
    """The operator that ran the result."""

    file_ids: Optional[List[str]] = None
    """A list of file ids that are attached to this result."""

    data_table_ids: Optional[List[str]] = None
    """A list of data table ids that are attached to this result."""

    status_type_summary: Optional[Dict[StatusType, int]] = None
    """A summary of the status types in the result."""

    workspace: Optional[str] = None
    """The id of the workspace that this product belongs to."""
    model_config = ConfigDict(extra="ignore")
