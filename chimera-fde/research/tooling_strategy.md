# Tooling Strategy

Date: 2026-02-04

## Developer MCP (Build-Time)
These MCP servers support development, testing, and repo operations.

- mcp-server-filesystem: Read/write repository files via controlled interface.
- mcp-server-git: Commit, diff, and branch management for auditability.
- mcp-server-postgres: Local schema validation and migrations.
- mcp-server-weaviate (dev): Memory store validation in controlled environment.

## Runtime MCP (Agent-Time)
These MCP servers provide production capabilities to agents.

- mcp-server-twitter / mcp-server-instagram / mcp-server-threads: Social posting and engagement.
- mcp-server-news: Trend and news ingestion.
- mcp-server-weaviate: Semantic memory retrieval.
- mcp-server-coinbase: Agentic commerce and wallet operations.

## Skills vs Tools
**Tools** are external MCP capabilities. **Skills** are internal, reusable agent packages.

### Initial Skills (No implementation yet)
- skill_fetch_trends: Collects, filters, and ranks trend inputs.
- skill_generate_caption: Produces platform-specific captions and disclosures.
- skill_reply_comment: Generates safe replies with persona constraints.

## Governance Notes
- Runtime MCP usage must be logged per task.
- Any tool usage that triggers a side effect must be gated by Judge approval.
