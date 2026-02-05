# Trend Strategy (MCP)

## Objective

Provide a deterministic, auditable method for collecting and ranking trend signals using MCP tools/resources.

## MCP Approach

We will use MCP tools to access external trend sources without direct network calls from skills:

- **Google Trends** via an MCP tool (e.g., `mcp://tool/google_trends`).
- **Twitter/X** via an MCP tool (e.g., `mcp://tool/twitter_trends`).
- **News APIs** via an MCP tool (e.g., `mcp://tool/news_search`).

Each tool call returns normalized items with:

- `trend_name`
- `confidence_score`
- `source_metadata`

## Aggregation & Ranking

1. Fetch in parallel per source with consistent query parameters (`topic`, `locale`, `time_window`).
2. Normalize scores to $[0, 1]$.
3. De-duplicate by `trend_name` (case-insensitive).
4. Rank by `confidence_score` descending.
5. Emit top `limit` results.

## Governance

All external interactions must be routed through MCP tools. No direct HTTP calls are permitted from skills.

## Notes

This strategy is a placeholder until the MCP tools are implemented and authenticated.
