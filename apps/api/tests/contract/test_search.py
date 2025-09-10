import httpx
import pytest

# Base URL for the API
BASE_URL = "http://127.0.0.1:8000"


def test_search_endpoint_exists():
    """
    Tests that the /api/v1/search endpoint exists and is reachable.
    This test is expected to fail until the server is running.
    """
    try:
        with httpx.Client() as client:
            response = client.get(f"{BASE_URL}/api/v1/search")
            # If we get a response, we want the test to fail if it's a 404
            assert response.status_code != 404
    except httpx.ConnectError:
        # This is the expected failure until the server is running
        pytest.fail(
            "Connection to the server failed. "
            "This is expected if the server is not running."
        )
    except Exception as e:
        pytest.fail(f"An unexpected error occurred: {e}")


@pytest.mark.skip(reason="Endpoint not yet implemented, so no response to validate.")
def test_search_endpoint_schema():
    """
    Tests that the response from the /api/v1/search endpoint matches the OpenAPI schema.
    This test will be skipped until the endpoint is implemented.
    """
    # TODO: Implement schema validation against openapi.yaml
    pass
