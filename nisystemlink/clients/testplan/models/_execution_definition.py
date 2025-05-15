from typing import Union

from nisystemlink.clients.core._uplink._json_model import JsonModel

class Job(JsonModel):
    """
    Represents a job to be executed, including its functions, arguments, and metadata.
    """
    functions: list[str]
    arguments: list[list[object]]
    metadata: dict[str, object]

class NotebookExecutionDefinition(JsonModel):
    """
    Defines the execution of a notebook, specifying the action and notebook ID.
    """
    action: str
    type: str = 'NOTEBOOK'
    notebookId: str

class ManualExecutionDefinition(JsonModel):
    """
    Represents a manual execution definition with a specific action.
    """
    action: str
    type: str = 'MANUAL'

class JobExecutionDefinition(JsonModel):
    """
    Defines the execution of one or more jobs, including system ID and job details.
    """
    action: str
    type: str = 'JOB'
    jobs: list[Job]
    systemId: str | None = None

class ScheduleExecutionDefinition(JsonModel):
    """
    Represents a scheduled execution definition with a specific action.
    """
    action: str
    type: str = 'SCHEDULE'

class UnscheduleExecutionDefinition(JsonModel):
    """
    Represents an unscheduled execution definition with a specific action.
    """
    action: str
    type: str = 'UNSCHEDULE'


class NoneExecutionDefinition(JsonModel):
    """
    Represents a definition where no execution is specified.
    """
    action: str
    type: str = 'None'

ExecutionDefinition = Union[
    NotebookExecutionDefinition,
    ManualExecutionDefinition,
    JobExecutionDefinition,
    NoneExecutionDefinition,
    ScheduleExecutionDefinition,
    UnscheduleExecutionDefinition
]