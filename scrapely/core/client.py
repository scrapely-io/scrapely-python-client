from scrapely.services.google import Google
from scrapely.services.cloudflare import Cloudflare
from scrapely.services.crawler import Crawler
from scrapely._version import __version__
import httpx, time

class Scrapely:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.scrapely.io/v2",
        poll_interval: float = 5.0,
        poll_timeout: float = 600.0,
    ):
        """
        Initialize the Scrapely client.

        Args:
            api_key: Your Scrapely API key.
            base_url: The base URL for the Scrapely API.
            poll_interval: Interval in seconds to poll for task results.
            poll_timeout: Maximum time in seconds to wait for a task to complete.
        """
        self.api_key = api_key
        self.base_url = base_url
        if poll_interval < 1.0:
            poll_interval = 1.0
        self.poll_interval = poll_interval
        self.poll_timeout = poll_timeout
        self._google = Google(self)
        self._cloudflare = Cloudflare(self)
        self._crawler = Crawler(self)
        self.client = httpx.Client(
            base_url=self.base_url,
            headers={
                "X-API-Key": self.api_key,
                "User-Agent": f"python-scrapely-client/{__version__}",
                "Content-Type": "application/json"
            }
        )
    def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ):
        """
        Make an internal request to the Scrapely API.

        Args:
            method: HTTP method (GET, POST, etc.).
            endpoint: API endpoint path.
            **kwargs: Additional arguments for the httpx request.

        Returns:
            httpx.Response: The API response.
        """
        response = self.client.request(
            method=method,
            url=endpoint,
            **kwargs
        )
        return response
    def _poll_task(
        self,
        task_id: str
    ):
        """
        Poll for the result of a created task.

        Args:
            task_id: The ID of the task to poll.

        Returns:
            dict: The task result data.

        Raises:
            TimeoutError: If the task does not complete within the poll_timeout.
        """
        start_time = time.time()
        while True:
            response = self._request(
                method="GET",
                endpoint=f"/tasks/{task_id}",
            )
            result = response.json()
            if result.get("status") in ["completed", "failed"]:
                return result
            if time.time() - start_time > self.poll_timeout:
                raise TimeoutError(f"Task {task_id} timed out after {self.poll_timeout} seconds")
            time.sleep(self.poll_interval)
    @property
    def google(self):
        """Access Google CAPTCHA solving services."""
        return self._google
    @property
    def cloudflare(self):
        """Access Cloudflare challenge solving services."""
        return self._cloudflare
    @property
    def crawler(self):
        """Access web crawling and automation services."""
        return self._crawler