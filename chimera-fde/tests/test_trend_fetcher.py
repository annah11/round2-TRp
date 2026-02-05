def test_trend_fetcher_returns_ranked_trends():
    """Trend fetcher must return ranked trends with required fields."""
    from skills.trend_fetcher import fetch_trends

    trends = fetch_trends(topic="ai", limit=5, locale="en-US", time_window="24h")

    assert isinstance(trends, list)
    assert len(trends) == 5
    assert all(
        "trend_name" in t and "confidence_score" in t and "source_metadata" in t
        for t in trends
    )
    assert trends == sorted(trends, key=lambda t: t["confidence_score"], reverse=True)
