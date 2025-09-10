import logging
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..auth import get_current_user
from ..database import get_db
from ..schemas import SearchQueryParams  # Import SearchQueryParams
from ..services.search_service import SearchService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/api/v1/search", response_model=List[dict])
def search_jobs(
    params: SearchQueryParams = Depends(),  # Use SearchQueryParams for validation
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    logger.info(f"Search request received from user: {current_user['username']}")
    logger.info(f"with params: {params.dict()}")
    # The tags parameter is a comma-separated string, we need to convert it to a list
    tags_list = params.tags.split(",") if params.tags else []
    search_service = SearchService(db)
    jobs = search_service.search_jobs(
        title=params.title,
        location=params.location,
        tags=tags_list,
        salary_min=params.salary_min,
        salary_max=params.salary_max,
    )
    logger.info(f"Search request completed. Found {len(jobs)} jobs.")
    return jobs
