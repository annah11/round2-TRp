# Skill: Trend Fetcher

## Purpose

Fetch and rank emerging trends for a given topic and time window using MCP resources.

## Inputs

- `topic` (string): Topic or keyword to analyze.
- `limit` (int): Maximum number of trends to return.
- `locale` (string): Locale for trend sources.
- `time_window` (string): One of `24h`, `7d`, or `30d`.

## Outputs

- `trends` (array): Sorted by descending score.
  - `id` (string)
  - `title` (string)
  - `score` (number)
  - `source` (string)
  - `url` (string)
  - `captured_at` (iso8601)

## MCP Tool

`mcp://tool/trend_fetcher`

## Notes

Trend fetcher must be deterministic and free of side effects.
