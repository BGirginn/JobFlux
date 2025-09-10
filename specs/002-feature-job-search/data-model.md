# Data Model for Job Search Feature

This document describes the data model for the `Job` entity.

## Entity: Job

Represents a job listing aggregated from various sources.

### Fields

| Field          | Type           | Description                                     | Constraints                |
|----------------|----------------|-------------------------------------------------|----------------------------|
| `id`           | `Integer`      | Primary key                                     | Not Null, Auto-increment   |
| `title`        | `String(255)`  | Job title                                       | Not Null                   |
| `location`     | `String(255)`  | Job location                                    | Not Null                   |
| `tags`         | `ARRAY(String)`| A list of tags associated with the job          |                            |
| `salary_min`   | `Integer`      | Minimum salary                                  |                            |
| `salary_max`   | `Integer`      | Maximum salary                                  |                            |
| `description`  | `Text`         | Job description                                 | Not Null                   |
| `company`      | `String(255)`  | Company name                                    | Not Null                   |
| `url`          | `String(255)`  | URL to the original job posting                 | Not Null, Unique           |
| `created_at`   | `DateTime`     | Timestamp when the job was added to our system  | Not Null, Default: now()   |

### Relationships

- No direct relationships to other entities in this feature.

### State Transitions

- A `Job` is created when a new job listing is scraped.
- A `Job` can be updated if the scraper finds new information about the same job.
- A `Job` can be deleted based on a data retention policy (e.g., after 90 days).
