import pytest

pytestmark = pytest.mark.xfail(
    reason="Skills interface not implemented yet",
    strict=False,
)


def test_skills_module_exposes_skill_contracts():
    """Failing test: skills package should expose expected contract helpers."""
    from chimera.skills import get_skill_contract

    contract = get_skill_contract("trend_fetcher")

    assert contract["tool"] == "mcp://tool/trend_fetcher"
    assert "parameters" in contract and "returns" in contract
