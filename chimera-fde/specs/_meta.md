# Project Chimera — Spec Meta

## Vision
Project Chimera builds an Autonomous Influencer Network: a governed, auditable, MCP-native platform where agents research trends, generate content, manage engagement, and propose commerce actions with minimal human intervention.

## 3-Day Challenge Scope
Day-0 to Day-3 goal: produce ratified specs, executable tests, and environment scaffolding to enable rapid implementation without architectural drift.

In scope:
- Spec-first definitions of task, tool, and resource contracts.
- Minimal skill surface to cover trends, content, and commerce.
- Safety gates and HITL checkpoints for sensitive actions.

Out of scope:
- Production-grade UI/UX.
- Live social posting or payment execution.
- Any proprietary model training or data ingestion pipelines.

## Constraints
- No implementation code before specs are ratified.
- All external interactions must route through MCP tools/resources.
- HITL is mandatory for low-confidence or policy-sensitive outputs.
- The system must remain deterministic and testable in isolation.

## Success Criteria
- Specs fully define task schemas and MCP tool contracts.
- TDD tests exist (even failing) to drive implementation.
- The environment is encapsulated and reproducible via Docker.
