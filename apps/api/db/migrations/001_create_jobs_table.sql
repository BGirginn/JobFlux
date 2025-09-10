-- 001_create_jobs_table.sql

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    tags VARCHAR[],
    salary_min INTEGER,
    salary_max INTEGER,
    description TEXT NOT NULL,
    company VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
