# Tasks: Job Search Aggregation & Filtering

**Input**: Design documents from `/specs/002-feature-job-search/`
**Prerequisites**: plan.md (required), research.md, data-model.md, contracts/

## Format: `[ID] [P?] Description`
- **[P]**: Can run in parallel (different files, no dependencies)
- Include exact file paths in descriptions

## Path Conventions
- **Web app**: `apps/api/`, `apps/web/`

## Phase 3.1: Setup
- [ ] T001 Create project structure for `apps/api` and `apps/web`.
- [ ] T002 Initialize Python project for `apps/api` with FastAPI, SQLAlchemy, and other dependencies.
- [ ] T003 Initialize TypeScript project for `apps/web` with Next.js, React, and other dependencies.
- [ ] T004 [P] Configure linting and formatting tools for `apps/api` (e.g., ruff, black).
- [ ] T005 [P] Configure linting and formatting tools for `apps/web` (e.g., ESLint, Prettier).

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [ ] T006 [P] Create contract test for `GET /api/v1/search` in `apps/api/tests/contract/test_search.py`.
- [ ] T007 [P] Create integration test for the job search feature based on `quickstart.md` in `apps/web/tests/integration/job-search.spec.ts`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)
- [ ] T008 Create `Job` model in `apps/api/src/models/job.py` based on `data-model.md`.
- [ ] T009 Create database migration script for the `Job` table in `apps/api/db/migrations.sql`.
- [ ] T010 Create `search_service.py` in `apps/api/src/services/` to handle the business logic for searching jobs.
- [ ] T011 Implement `GET /api/v1/search` endpoint in `apps/api/src/api/search.py`.
- [ ] T012 Create search page UI in `apps/web/src/pages/search.tsx`.
- [ ] T013 Create search filter components in `apps/web/src/components/search/`.
- [ ] T014 Implement API client in `apps/web/src/services/api.ts` to fetch job listings.

## Phase 3.4: Integration
- [ ] T015 Connect `search_service.py` to the PostgreSQL database.
- [ ] T016 Implement JWT authentication middleware in `apps/api`.
- [ ] T017 Implement structured logging for the search endpoint in `apps/api`.
- [ ] T018 Implement logging for the search page in `apps/web` and send logs to the backend.

## Phase 3.5: Polish
- [ ] T019 [P] Add unit tests for input validation in `apps/api`.
- [ ] T020 [P] Add unit tests for the search filter components in `apps/web`.
- [ ] T021 Run performance tests on the search endpoint to ensure p95 < 200ms.
- [ ] T022 [P] Update API documentation.
- [ ] T023 [P] Ensure the web UI meets WCAG 2.1 AA accessibility standards.

## Dependencies
- Setup (T001-T005) before all other phases.
- Tests (T006-T007) before implementation (T008-T014).
- T008 blocks T009, T010.
- T010 blocks T011, T015.
- T016 blocks T011.
- Implementation before polish (T019-T023).

## Parallel Example
```
# Launch T004, T005, T006, T007 together:
Task: "Configure linting and formatting tools for apps/api"
Task: "Configure linting and formatting tools for apps/web"
Task: "Create contract test for GET /api/v1/search in apps/api/tests/contract/test_search.py"
Task: "Create integration test for the job search feature based on quickstart.md in apps/web/tests/integration/job-search.spec.ts"
```
