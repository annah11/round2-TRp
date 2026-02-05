# Skill: Commerce Manager

## Purpose
Propose and execute commerce actions (offers, affiliate placements, payouts) with audit trails.

## Inputs
- `action` (string): `propose` or `execute`.
- `offer_id` (string)
- `amount` (number)
- `currency` (string)
- `counterparty` (string)
- `justification` (string)

## Outputs
- `transaction_id` (string)
- `status` (string): `proposed`, `approved`, `rejected`, or `executed`
- `audit_ref` (string)

## MCP Tool
`mcp://tool/commerce_manager`

## Notes
Side-effecting execution requires Judge approval.
