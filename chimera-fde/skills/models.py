from enum import Enum
from typing import Any, Dict

from pydantic import BaseModel, Field


class AgentRole(str, Enum):
    PLANNER = "Planner"
    WORKER = "Worker"
    JUDGE = "Judge"


class TaskSchema(BaseModel):
    task_id: str = Field(..., min_length=1)
    agent_role: AgentRole
    payload: Dict[str, Any]
    status: str = Field(..., pattern=r"^(pending|in_progress|review|complete)$")
