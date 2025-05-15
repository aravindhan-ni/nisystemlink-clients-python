from typing import List, Literal, Union

class ExecutionEventBase:
    """
    Base class for execution events, containing common attributes such as action,
    the time the event was triggered, and the user who triggered it.
    """
    action: str
    triggeredAt: str
    triggeredBy: str = None

class NotebookExecutionEvent(ExecutionEventBase):
    """
    Represents an execution event triggered by a notebook.
    Includes the type identifier and the execution ID.
    """
    type: Literal['NOTEBOOK']
    executionId: str

class JobExecutionEvent(ExecutionEventBase):
    """
    Represents an execution event triggered by a job.
    Includes the type identifier and a list of job IDs.
    """
    type: Literal['JOB']
    jobIds: List[str]

class ManualExecutionEvent(ExecutionEventBase):
    """
    Represents an execution event triggered manually.
    Includes only the type identifier.
    """
    type: Literal['MANUAL']

ExecutionEvent = Union[NotebookExecutionEvent, ManualExecutionEvent, JobExecutionEvent]