# Agent Workflow v1 — Spec Drafting

## 1. Purpose

### What problem does this workflow solve?
Creates a governed, repeatable path for producing a complete specification before any implementation begins, reducing unsafe autonomy and rework.

### Why is it the first one?
Chimera is documentation-first; a spec workflow establishes governance, auditability, and task decomposition before any agent executes actions.

## 2. Actors

- Planner: Decomposes the requested spec into atomic drafting tasks and assigns workers.
- Worker(s): Draft spec sections using approved resources and templates.
- Judge(s): Validate completeness, safety, and compliance with governance rules.
- Human (if any): Approves low-confidence or sensitive outputs per governance rules.

## 3. Inputs

- MCP resources:
  - Repository files (README, existing specs, docs)
  - Approved templates (if any) in specs/
  - Tool abstraction layer for reading/writing files
- Triggers (time / event / threshold):
  - Event: New spec request from human or system
  - Threshold: Planner confidence < 0.7 triggers HITL before drafting

## 4. Outputs

- Content artifacts:
  - A new or updated specification file in specs/ (e.g., specs/<name>.md)
- Side effects:
  - Log: Planning decision record (task list + confidence)
  - Store memory: Link spec to goal, version, and reviewer decision

## 5. Step-by-Step Flow

1. Planner receives spec request and loads relevant repo context.
2. Planner defines required sections and creates atomic drafting tasks.
3. Planner estimates confidence per section and checks governance rules.
4. If confidence < 0.7 or content is sensitive, request human approval before drafting.
5. Workers draft assigned sections using only approved MCP resources.
6. Judge validates each section for completeness and policy compliance.
7. If any section fails, return to Planner with reasons and required fixes.
8. If all sections pass, assemble the final spec file and write to specs/.
9. Judge performs final spec-level validation and logs approval.

## 6. Governance Rules

- Confidence thresholds:
  - Planner: Must be >= 0.7 to proceed without HITL.
  - Judge: Must be >= 0.8 to approve the final spec.
- When HITL is required:
  - Confidence below thresholds
  - Any sensitive or high-risk content
  - Any request to use unapproved tools or data sources
- What is forbidden:
  - Drafting from unapproved sources
  - Skipping Judge review
  - Writing files outside specs/
  - Making implementation changes or creating code

## 7. Failure Modes

- Missing or ambiguous requirements → Planner returns INSUFFICIENT_CONTEXT to human.
- Unapproved tools/resources requested → Halt and request approval or alternative.
- Judge rejection of section(s) → Re-plan and re-draft only failed sections.
- Write failure (file system/permissions) → Log error and request human intervention.
