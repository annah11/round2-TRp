# Technical Specification

## JSON Schema — TaskSchema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://chimera.ai/schemas/task-schema.json",
  "title": "TaskSchema",
  "type": "object",
  "additionalProperties": false,
  "required": ["task_id", "agent_role", "payload", "status"],
  "properties": {
    "task_id": { "type": "string", "minLength": 1 },
    "agent_role": { "type": "string", "enum": ["Planner", "Worker", "Judge"] },
    "payload": { "type": "object", "additionalProperties": true },
    "status": {
      "type": "string",
      "enum": ["pending", "in_progress", "review", "complete"]
    }
  }
}
```

## TrendFetcher Output Schema

Exact output for the TrendFetcher skill (array of items):

```json
[
  {
    "trend_name": "string",
    "confidence_score": 0.0,
    "source_metadata": {
      "source": "string",
      "source_url": "string",
      "captured_at": "iso8601",
      "query": "string",
      "locale": "string",
      "time_window": "24h|7d|30d"
    }
  }
]
```

- System must support 1,000 concurrent workers.
- Task latency for high-priority replies: $\leq 10s$ (excluding HITL).
