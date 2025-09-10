# /plan — Plan how to implement the specified feature

You are the Plan phase agent for **JobFlux**.

## Input
- `$ARGUMENTS`: JSON with implementation details, constraints, and priorities.

## Required Steps
1) From the repo root, run:
      ```bash
      scripts/check-task-prerequisites.sh --json
      ```
      Parse the output JSON to get:
      - `FEATURE_DIR`: Absolute path to the feature directory.
      - `AVAILABLE_DOCS`: List of absolute paths to available design documents.  
2) Load and analyze available design documents:
   - Always read `plan.md` for tech stack and libraries
   - IF EXISTS: Read `data-model.md` for entities
   - IF EXISTS: Read `contracts/` for API endpoints
   - IF EXISTS: Read `research.md` for technical decisions
   - IF EXISTS: Read `quickstart.md` for test scenarios
   Note: Not all projects have all documents. For example:
   - CLI tools might not have `contracts/`
   - Simple libraries might not need `data-model.md`
   - Generate plan based on what's available
3) Create a detailed implementation plan in `FEATURE_DIR/plan.md`:
   - Summarize key points from design docs
   - Outline main components and their interactions
   - Highlight any technical decisions or trade-offs
   - Specify libraries, frameworks, and tools to use
   - Include diagrams if helpful (describe them in text)
   - Ensure clarity for the next Task phase
4) Ensure the plan is actionable and aligns with the provided context in `$ARGUMENTS`.