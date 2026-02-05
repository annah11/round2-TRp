# OpenClaw Integration (Optional)

## Goal
Publish Chimera availability/status to the OpenClaw network for interoperability with other agents.

## Proposed Status Payload
```json
{
  "agent_id": "uuid",
  "status": "available|busy|offline",
  "capabilities": ["trend_scan", "content_gen", "reply"],
  "contact": {
    "mcp_endpoint": "https://...",
    "public_key": "..."
  },
  "timestamp": "iso8601"
}
```

## Governance
- Status updates must not include private keys or secrets.
- Any automated updates are rate-limited and logged.

## Open Questions
- Confirm OpenClaw schema and publish endpoint.
- Determine authentication and signing requirements.
