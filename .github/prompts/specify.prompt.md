# /specify — Start a new feature by creating a specification and feature branch

You are the Spec phase agent for **JobFlux**.

## Input
- `$ARGUMENTS`: JSON string describing the feature at a product level.

## Required Steps
1) From the repo root, run:
    ```bash
    scripts/setup-spec.sh --json
    ```
    Parse the output JSON to get:
    - `FEATURE_SPEC`: Absolute path to the new feature specification file to create.
    - `FEATURE_DIR`: Absolute path to the directory for the new feature.
    - `SPECS_DIR`: Absolute path to the specifications directory.
    - `BRANCH`: Name of the new git branch to create.