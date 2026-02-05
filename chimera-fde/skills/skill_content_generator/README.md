# Skill: Content Generator

## Purpose

Generate platform-ready content from a structured brief and constraints.

## Inputs

- `brief` (string): Content brief.
- `format` (string): `text`, `image`, `video`, or `thread`.
- `channels` (array): Target platforms.
- `tone` (string): Desired tone.
- `constraints` (array): Must-follow constraints.

## Outputs

- `content` (object)
  - `type` (string)
  - `payload` (object)
- `confidence_score` (number)
- `risk_labels` (array)

## MCP Tool

`mcp://tool/content_generator`

## Notes

All outputs are subject to Judge review prior to publication.
