from sqlalchemy.orm import Session

from ..models.job import Job


class SearchService:
    def __init__(self, db: Session):
        self.db = db

    def search_jobs(
        self,
        title: str = None,
        location: str = None,
        tags: list[str] = None,
        salary_min: int = None,
        salary_max: int = None,
    ):
        query = self.db.query(Job)

        if title:
            query = query.filter(Job.title.ilike(f"%{title}%"))
        if location:
            query = query.filter(Job.location.ilike(f"%{location}%"))
        if tags:
            # Assuming tags are stored as an array in PostgreSQL
            query = query.filter(Job.tags.overlap(tags))
        if salary_min:
            query = query.filter(Job.salary_min >= salary_min)
        if salary_max:
            query = query.filter(Job.salary_max <= salary_max)

        return query.all()
