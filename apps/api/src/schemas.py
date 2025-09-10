from typing import Optional

from pydantic import BaseModel, Field


class SearchQueryParams(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    location: Optional[str] = Field(None, min_length=1, max_length=255)
    tags: Optional[str] = None  # Comma-separated string
    salary_min: Optional[int] = Field(None, ge=0)
    salary_max: Optional[int] = Field(None, ge=0)

    # Add a validator for salary_min and salary_max
    # @validator('salary_max')
    # def salary_max_greater_than_min(cls, v, values):
    #     if 'salary_min' in values and v is not None and \
    #        values['salary_min'] is not None and v < values['salary_min']:
    #         raise ValueError('salary_max must be greater than or equal to salary_min')
    #     return v
