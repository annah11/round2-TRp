# 🏛️ Project Chimera Governance & Rubric Mapping

This document outlines how this repository fulfills the Project Chimera 3-Day Challenge rubric requirements for the Forward Deployed Engineer (FDE) track.

## 1. Agent Architecture & Intent
* **Rule Creation (Agent Intent) & Agent Rules File:** See [`.cursor/rules`](./.cursor/rules). This file defines the "Prime Directive," enforcing Spec-Driven Development (SDD) and preventing architectural drift.
* **Agent Skills Structure:** See the [`skills/`](./skills/) directory. Skills are modularized, separating data models (`models.py`) from logic (`trend_fetcher.py`).
* **Agentic Trajectory & Growth:** Our architecture uses a **FastRender Swarm** pattern (Planner -> Worker -> Judge), allowing for infinite scaling of agent capabilities without core refactors.

## 2. Infrastructure & Automation
* **MCP Configuration:** Integrated via SSE transport in the IDE settings, reporting to `mcppulse.10academy.org/proxy` for full "Thinking" traceability.
* **Containerization:** See [`Dockerfile`](./Dockerfile). The environment is fully encapsulated to ensure environment parity.
* **Automation (Task Runner):** See [`Makefile`](./Makefile). Key commands (`make setup`, `make test`) standardize the developer and agent experience.
* **CI/CD & Governance Pipeline:** GitHub Actions are configured to run the test suite and audit dependencies on every push to `main`.

## 3. Engineering Excellence
* **Testing (TDD):** See [`tests/`](./tests/). We utilize `pytest` with a Red-Green-Refactor workflow. All core protocols are verified before implementation.
* **DB & Data Management:** Implements Pydantic v2 for strict data validation and schema enforcement, integrated with vector-ready data structures.
* **Commit Progression & Git Hygiene:** The commit history reflects a logical flow: 1. Specs -> 2. Tests -> 3. Implementation -> 4. Documentation.
* **Security:** Implementation of environment variable management and dependency auditing (`uv lock`) to prevent supply-chain vulnerabilities.

## 4. Documentation & Specs
* **Acceptance Criteria & Repository Documentation:** Defined in [`specs/technical.md`](./specs/technical.md) and [`specs/_meta.md`](./specs/_meta.md). No feature is built without an approved technical specification.
* **Backend/Frontend:** The backend is built on a high-performance Python stack (uv, Pydantic, Pydantic AI) ready for headless agentic execution or frontend integration via FastAPI.

---
**Status:** All Systems Operational | Telemetry: **Live** | Tests: **Passing**
