from __future__ import annotations
from scrapely.models.types import InstructionBase
from typing import Literal
from scrapely.models.exceptions import raise_scrapely_exception
from scrapely.models.response import CrawlerResponse
import json

class Crawler:
    def __init__(self, instance):
        """
        Initialize the Crawler service.

        Args:
            instance (Scrapely): The Scrapely client instance.
        """
        from scrapely.core.client import Scrapely
        assert isinstance(instance, Scrapely)
        self.instance = instance
    def crawl(
        self,
        website_url: str,
        block_resources: bool = False, # block image loading
        device: Literal["desktop", "mobile"] = "desktop",
        screenshot: bool = False,
        screenshot_full_page: bool = False,
        return_page_source: bool = False,
        return_page_text: bool = False,
        return_page_cookies: bool = False,
        return_user_agent: bool = False,
        return_page_meta: bool = False,
        user_agent: str = None,
        instructions: list[InstructionBase] = [],
    ) -> CrawlerResponse:
        """
        Crawl a website with optional instructions and data return options.

        Args:
            website_url: The URL of the website to crawl.
            block_resources: Whether to block images and other resources.
            device: Emulated device type (desktop or mobile).
            screenshot: Whether to take a screenshot.
            screenshot_full_page: Whether the screenshot should be full page.
            return_page_source: Whether to return the HTML source.
            return_page_text: Whether to return the page text.
            return_page_cookies: Whether to return page cookies.
            return_user_agent: Whether to return the user agent used.
            return_page_meta: Whether to return page metadata.
            user_agent: Custom user agent string.
            instructions: List of automation instructions to execute.

        Returns:
            CrawlerResponse: The result of the crawl task.
        """
        data = {
            "crawler": {
                "websiteURL": website_url,
            }
        }
        if block_resources:
            data["crawler"]["block_resources"] = True
        if device:
            data["crawler"]["device"] = device
        if screenshot:
            data["crawler"]["screenshot"] = True
        if screenshot_full_page:
            data["crawler"]["screenshot_full_page"] = True
        if return_page_source:
            data["crawler"]["return_page_source"] = True
        if return_page_text:
            data["crawler"]["return_page_text"] = True
        if return_page_cookies:
            data["crawler"]["return_page_cookies"] = True
        if return_user_agent:
            data["crawler"]["return_user_agent"] = True
        if return_page_meta:
            data["crawler"]["return_page_meta"] = True
        if instructions:
            data["crawler"]["instructions"] = [instruction.to_dict() for instruction in instructions]
        if user_agent:
            if not data.get("options"):
                data["options"] = {}
            data["options"]["user_agent"] = user_agent
        task = self.instance._request(
            method="POST",
            endpoint="/tasks/create",
            json=data,
        )
        result = task.json()
        if result.get("success") == False:
            raise_scrapely_exception(
                result.get("error"),
                task.status_code
            )
        else:
            task_id = result["task"]["id"]
            response_dict = self.instance._poll_task(
                task_id=task_id,
            )
            return CrawlerResponse.from_dict(response_dict)

class AsyncCrawler:
    def __init__(self, instance):
        """
        Initialize the AsyncCrawler service.

        Args:
            instance (AsyncScrapely): The AsyncScrapely client instance.
        """
        from scrapely.core.async_client import AsyncScrapely
        assert isinstance(instance, AsyncScrapely)
        self.instance = instance

    async def crawl(
        self,
        website_url: str,
        block_resources: bool = False, # block image loading
        device: Literal["desktop", "mobile"] = "desktop",
        screenshot: bool = False,
        screenshot_full_page: bool = False,
        return_page_source: bool = False,
        return_page_text: bool = False,
        return_page_cookies: bool = False,
        return_user_agent: bool = False,
        return_page_meta: bool = False,
        user_agent: str = None,
        instructions: list[InstructionBase] = [],
    ) -> CrawlerResponse:
        """
        Crawl a website with optional instructions and data return options asynchronously.

        Args:
            website_url: The URL of the website to crawl.
            block_resources: Whether to block images and other resources.
            device: Emulated device type (desktop or mobile).
            screenshot: Whether to take a screenshot.
            screenshot_full_page: Whether the screenshot should be full page.
            return_page_source: Whether to return the HTML source.
            return_page_text: Whether to return the page text.
            return_page_cookies: Whether to return page cookies.
            return_user_agent: Whether to return the user agent used.
            return_page_meta: Whether to return page metadata.
            user_agent: Custom user agent string.
            instructions: List of automation instructions to execute.

        Returns:
            CrawlerResponse: The result of the crawl task.
        """
        data = {
            "crawler": {
                "websiteURL": website_url,
            }
        }
        if block_resources:
            data["crawler"]["block_resources"] = True
        if device:
            data["crawler"]["device"] = device
        if screenshot:
            data["crawler"]["screenshot"] = True
        if screenshot_full_page:
            data["crawler"]["screenshot_full_page"] = True
        if return_page_source:
            data["crawler"]["return_page_source"] = True
        if return_page_text:
            data["crawler"]["return_page_text"] = True
        if return_page_cookies:
            data["crawler"]["return_page_cookies"] = True
        if return_user_agent:
            data["crawler"]["return_user_agent"] = True
        if return_page_meta:
            data["crawler"]["return_page_meta"] = True
        if instructions:
            data["crawler"]["instructions"] = [instruction.to_dict() for instruction in instructions]
        if user_agent:
            if not data.get("options"):
                data["options"] = {}
            data["options"]["user_agent"] = user_agent
        task = await self.instance._request(
            method="POST",
            endpoint="/tasks/create",
            json=data,
        )
        result = task.json()
        if result.get("success") == False:
            raise_scrapely_exception(
                result.get("error"),
                task.status_code
            )
        else:
            task_id = result["task"]["id"]
            response_dict = await self.instance._poll_task(
                task_id=task_id,
            )
            return CrawlerResponse.from_dict(response_dict)
