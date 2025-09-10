# Research for Job Search Aggregation & Filtering

This document summarizes the research and decisions made to clarify the ambiguities in the implementation plan.

## Technology Stack

- **Language/Version**: 
    - **API**: Python 3.11
    - **Web**: TypeScript 5.2
- **Primary Dependencies**:
    - **API**: FastAPI
    - **Web**: React, Next.js
    - **Data**: SQLAlchemy for the ORM
- **Storage**: 
    - **Database**: PostgreSQL
- **Testing**:
    - **API**: pytest
    - **Web**: Jest, Cypress

**Rationale**: This stack is a modern and widely used combination for building web applications. FastAPI is a high-performance Python framework for building APIs. React and Next.js are popular choices for building modern web frontends. PostgreSQL is a powerful open-source relational database.

## Architecture and Design Patterns

- **Using framework directly?**: Yes, we will use FastAPI and Next.js directly without any custom wrappers to maintain simplicity.
- **Avoiding patterns?**: We will start without complex design patterns like Repository or Unit of Work. We will use SQLAlchemy's session management for database interactions.

**Rationale**: We are following the principle of simplicity and YAGNI (You Ain't Gonna Need It). We will introduce more complex patterns only when they are proven to be necessary.

## Observability

- **Frontend logs → backend?**: Yes, frontend logs will be sent to the backend to a dedicated logging endpoint. This will allow for a unified logging stream and easier debugging.

**Rationale**: Centralized logging is a best practice for observability.

## API Versioning

- **Version number assigned?**: The API will be versioned using a path-based scheme, e.g., `/api/v1/search`. The initial version will be `v1`.

**Rationale**: Path-based versioning is a common and straightforward way to version APIs.

## Feature-specific Clarifications

- **Accessibility Standards**: The web interface will adhere to WCAG 2.1 AA standards to ensure it is accessible to users with disabilities.
- **Deduplication Rules**: Job listings will be deduplicated based on a combination of the job title, company name, and the job posting URL. A unique constraint will be added to the database to enforce this.
- **Authentication Method**: Requests to the search API will be authenticated using JWT (JSON Web Tokens). An authentication middleware will be implemented in the API.
- **User Attributes**: For the initial implementation, we will not store any user-specific search data. The `User` entity is out of scope for this feature.
