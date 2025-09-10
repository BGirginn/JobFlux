import pytest
from pydantic import ValidationError
from apps.api.src.schemas import SearchQueryParams

def test_valid_search_params():
    params = SearchQueryParams(title="Software Engineer", location="London", salary_min=50000)
    assert params.title == "Software Engineer"
    assert params.location == "London"
    assert params.salary_min == 50000

def test_invalid_title_length():
    with pytest.raises(ValidationError):
        SearchQueryParams(title="") # Too short
    with pytest.raises(ValidationError):
        SearchQueryParams(title="a" * 256) # Too long

def test_invalid_salary_min():
    with pytest.raises(ValidationError):
        SearchQueryParams(salary_min=-100) # Less than 0

def test_invalid_salary_max():
    with pytest.raises(ValidationError):
        SearchQueryParams(salary_max=-100) # Less than 0

# Uncomment this test if you uncomment the validator in schemas.py
# def test_salary_max_less_than_min():
#     with pytest.raises(ValidationError):
#         SearchQueryParams(salary_min=100000, salary_max=50000)
