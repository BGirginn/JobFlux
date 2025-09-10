from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Users will wait between 1 and 2 seconds between tasks

    @task
    def search_jobs(self):
        # Simulate a search request with some parameters
        self.client.get(
            "/api/v1/search",
            params={
                "title": "Software Engineer",
                "location": "London",
                "salary_min": 50000,
            },
            headers={"Authorization": "Bearer valid-jwt-token"},
        )
