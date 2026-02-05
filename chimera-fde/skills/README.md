# Skills Catalog (Draft)

Skills are internal capability packages used by agents. Each skill defines explicit input/output contracts and does not directly call external APIs without MCP tools.

## skill_fetch_trends
**Purpose:** Collect, filter, and rank trend inputs.

**Inputs**
- `sources`: array of MCP resource URIs
- `relevance_threshold`: float

**Outputs**
- `trend_items`: array of `{topic, score, source_uri}`

## skill_generate_caption
**Purpose:** Generate platform-specific captions with required AI disclosure.

**Inputs**
- `platform`: string
- `persona_constraints`: array of strings
- `content_brief`: string

**Outputs**
- `caption_text`: string
- `disclosure_level`: one of `automated|assisted|none`

## skill_reply_comment
**Purpose:** Generate safe replies aligned with persona and policy.

**Inputs**
- `comment_text`: string
- `persona_constraints`: array of strings
- `safety_flags`: array of strings

**Outputs**
- `reply_text`: string
- `confidence_score`: float
