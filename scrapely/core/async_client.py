from scrapely.services.google import AsyncGoogle
from scrapely.services.cloudflare import AsyncCloudflare
from scrapely.services.crawler import AsyncCrawler
from scrapely._version import __version__
import httpx, asyncio, time

class AsyncScrapely:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.scrapely.io/v2",
        poll_interval: float = 5.0,
        poll_timeout: float = 600.0,
    ):
        """
        Initialize the AsyncScrapely client.

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
        self._google = AsyncGoogle(self)
        self._cloudflare = AsyncCloudflare(self)
        self._crawler = AsyncCrawler(self)
        self.headers = {
            "X-API-Key": self.api_key,
            "User-Agent": f"python-scrapely-client-async/{__version__}",
            "Content-Type": "application/json"
        }

    async def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ):
        """
        Make an internal asynchronous request to the Scrapely API.

        Args:
            method: HTTP method (GET, POST, etc.).
            endpoint: API endpoint path.
            **kwargs: Additional arguments for the httpx request.

        Returns:
            httpx.Response: The API response.
        """
        async with httpx.AsyncClient(base_url=self.base_url, headers=self.headers) as client:
            response = await client.request(
                method=method,
                url=endpoint,
                **kwargs
            )
            return response

    async def _poll_task(
        self,
        task_id: str
    ):
        """
        Poll for the result of a created task asynchronously.

        Args:
            task_id: The ID of the task to poll.

        Returns:
            dict: The task result data.

        Raises:
            TimeoutError: If the task does not complete within the poll_timeout.
        """
        start_time = time.time()
        while True:
            response = await self._request(
                method="GET",
                endpoint=f"/tasks/{task_id}",
            )
            result = response.json()
            if result.get("status") in ["completed", "failed"]:
                return result
            if time.time() - start_time > self.poll_timeout:
                raise TimeoutError(f"Task {task_id} timed out after {self.poll_timeout} seconds")
            await asyncio.sleep(self.poll_interval)

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
