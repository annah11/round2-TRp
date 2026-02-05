from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.test import TestModel


class TrendItem(BaseModel):
    trend_name: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    source_metadata: Dict[str, Any]


class TrendFetcher:
    """Simple TrendFetcher using a Pydantic AI agent pattern and mock data."""

    def __init__(self) -> None:
        self.agent = Agent(model=TestModel(), output_type=TrendItem)

    def run(self, topic: str, limit: int, locale: str = "en-US", time_window: str = "24h") -> List[Dict[str, Any]]:
        now = datetime.now(timezone.utc).isoformat()
        items = [
            TrendItem(
                trend_name=f"{topic} trend {i + 1}",
                confidence_score=max(0.0, 1.0 - (i * 0.1)),
                source_metadata={
                    "source": "mock",
                    "source_url": "https://example.com/trends",
                    "captured_at": now,
                    "query": topic,
                    "locale": locale,
                    "time_window": time_window,
                },
            )
            for i in range(limit)
        ]
        return [item.model_dump() for item in items]


def fetch_trends(topic: str, limit: int, locale: str = "en-US", time_window: str = "24h") -> List[Dict[str, Any]]:
    """Functional wrapper for TrendFetcher.run()."""
    return TrendFetcher().run(topic=topic, limit=limit, locale=locale, time_window=time_window)
