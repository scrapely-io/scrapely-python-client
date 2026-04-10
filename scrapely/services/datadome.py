from __future__ import annotations
from scrapely.models.captcha import CaptchaType
from scrapely.models.exceptions import raise_scrapely_exception
from scrapely.models.response import CaptchaResponse

class DataDome:
    def __init__(self, instance):
        """
        Initialize the DataDome service.

        Args:
            instance (Scrapely): The Scrapely client instance.
        """
        from scrapely.core.client import Scrapely
        assert isinstance(instance, Scrapely)
        self.instance = instance
    def solve(
        self,
        website_url: str,
        captcha_url: str,
        user_agent: str = None,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a DataDome challenge.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            captcha_url: The URL of the CAPTCHA image.
            user_agent: The user agent to use for the solve.
            proxy_scheme: The scheme scheme to use for the proxy.
            proxy_host: The host of the proxy.
            proxy_port: The port of the proxy.
            proxy_username: The username of the proxy.
            proxy_password: The password of the proxy.
        Returns:
            CaptchaResponse: The response from the Scrapely API.
        """
        data = {
            "captcha": {
                "type": CaptchaType.DATADOME,
                "websiteURL": website_url,
                "CaptchaURL": captcha_url,
            },
            "options": {},
        }
        if user_agent:
            data["options"]["user_agent"] = user_agent
        if all([proxy_scheme, proxy_host, proxy_port]):
            data["proxy"] = {
                "scheme": proxy_scheme,
                "host": proxy_host,
                "port": proxy_port,
            }
        if all([proxy_scheme, proxy_host, proxy_port, proxy_username, proxy_password]):
            data["proxy"]["username"] = proxy_username
            data["proxy"]["password"] = proxy_password
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
            return CaptchaResponse.from_dict(response_dict)


class AsyncDataDome:
    def __init__(self, instance):
        """
        Initialize the DataDome service.

        Args:
            instance (Scrapely): The Scrapely client instance.
        """
        from scrapely.core.async_client import AsyncScrapely
        assert isinstance(instance, AsyncScrapely)
        self.instance = instance
    async def solve(
        self,
        website_url: str,
        captcha_url: str,
        user_agent: str = None,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a DataDome challenge.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            captcha_url: The URL of the CAPTCHA image.
            user_agent: The user agent to use for the solve.
            proxy_scheme: The scheme scheme to use for the proxy.
            proxy_host: The host of the proxy.
            proxy_port: The port of the proxy.
            proxy_username: The username of the proxy.
            proxy_password: The password of the proxy.
        Returns:
            CaptchaResponse: The response from the Scrapely API.
        """
        data = {
            "captcha": {
                "type": CaptchaType.DATADOME,
                "websiteURL": website_url,
                "CaptchaURL": captcha_url,
            },
            "options": {},
        }
        if user_agent:
            data["options"]["user_agent"] = user_agent
        if all([proxy_scheme, proxy_host, proxy_port]):
            data["proxy"] = {
                "scheme": proxy_scheme,
                "host": proxy_host,
                "port": proxy_port,
            }
        if all([proxy_scheme, proxy_host, proxy_port, proxy_username, proxy_password]):
            data["proxy"]["username"] = proxy_username
            data["proxy"]["password"] = proxy_password
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
            return CaptchaResponse.from_dict(response_dict)


