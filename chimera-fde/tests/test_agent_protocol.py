def test_task_schema_validates_minimal_payload():
    """TaskSchema should validate required fields."""
    from skills.models import TaskSchema

    payload = {
        "task_id": "task-1",
        "agent_role": "Planner",
        "payload": {"goal": "analyze trends"},
        "status": "pending",
    }
    model = TaskSchema.model_validate(payload)

    assert model.task_id == payload["task_id"]
    assert model.agent_role.value == payload["agent_role"]
    assert model.payload == payload["payload"]
    assert model.status == payload["status"]
