from fastapi import APIRouter, Depends
from typing import List
from ..services.search_service import SearchService

router = APIRouter()

@router.get("/api/v1/search", response_model=List[dict])
def search_jobs(
    title: str = None,
    location: str = None,
    tags: str = None,
    salary_min: int = None,
    salary_max: int = None,
    search_service: SearchService = Depends(SearchService)
):
    # The tags parameter is a comma-separated string, we need to convert it to a list
    tags_list = tags.split(',') if tags else []
    jobs = search_service.search_jobs(
        title=title,
        location=location,
        tags=tags_list,
        salary_min=salary_min,
        salary_max=salary_max
    )
    return jobs
