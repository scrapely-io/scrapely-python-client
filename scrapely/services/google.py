from __future__ import annotations
from scrapely.models.captcha import CaptchaType
from scrapely.models.exceptions import raise_scrapely_exception
from scrapely.models.response import CaptchaResponse

class Google:
    def __init__(self, instance):
        """
        Initialize the Google service.

        Args:
            instance (Scrapely): The Scrapely client instance.
        """
        from scrapely.core.client import Scrapely
        assert isinstance(instance, Scrapely)
        self.instance = instance
    def RecaptchaV3(
        self,
        website_url: str,
        website_key: str,
        action: str = None,
        enterprise: bool = False,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a Google reCAPTCHA V3 challenge.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            website_key: The site key for the reCAPTCHA.
            action: Optional action name.
            enterprise: Whether it's the Enterprise version.
            proxy_scheme: Proxy protocol (http, socks4, socks5).
            proxy_host: Proxy host address.
            proxy_port: Proxy port number.
            proxy_username: Optional proxy username.
            proxy_password: Optional proxy password.

        Returns:
            CaptchaResponse: The result of the solved CAPTCHA task.
        """
        data = {
            "captcha": {
                "type": CaptchaType.RECAPTCHA_V3,
                "websiteURL": website_url,
                "websiteKey": website_key,
            },
            "options": {},
        }
        if action:
            data["options"]["action"] = action
        if enterprise:
            data["options"]["enterprise"] = True
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
    def RecaptchaV2(
        self,
        website_url: str,
        website_key: str,
        invisible: bool = False,
        enterprise: bool = False,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a Google reCAPTCHA V2 challenge.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            website_key: The site key for the reCAPTCHA.
            invisible: Whether the CAPTCHA is invisible.
            enterprise: Whether it's the Enterprise version.
            proxy_scheme: Proxy protocol (http, socks4, socks5).
            proxy_host: Proxy host address.
            proxy_port: Proxy port number.
            proxy_username: Optional proxy username.
            proxy_password: Optional proxy password.

        Returns:
            CaptchaResponse: The result of the solved CAPTCHA task.
        """
        data = {
            "captcha": {
                "type": CaptchaType.RECAPTCHA_V2,
                "websiteURL": website_url,
                "websiteKey": website_key,
            },
            "options": {},
        }
        if invisible:
            data["options"]["invisible"] = True
        if enterprise:
            data["options"]["enterprise"] = True
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

class AsyncGoogle:
    def __init__(self, instance):
        """
        Initialize the AsyncGoogle service.

        Args:
            instance (AsyncScrapely): The AsyncScrapely client instance.
        """
        from scrapely.core.async_client import AsyncScrapely
        assert isinstance(instance, AsyncScrapely)
        self.instance = instance

    async def RecaptchaV3(
        self,
        website_url: str,
        website_key: str,
        action: str = None,
        enterprise: bool = False,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a Google reCAPTCHA V3 challenge asynchronously.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            website_key: The site key for the reCAPTCHA.
            action: Optional action name.
            enterprise: Whether it's the Enterprise version.
            proxy_scheme: Proxy protocol (http, socks4, socks5).
            proxy_host: Proxy host address.
            proxy_port: Proxy port number.
            proxy_username: Optional proxy username.
            proxy_password: Optional proxy password.

        Returns:
            CaptchaResponse: The result of the solved CAPTCHA task.
        """
        data = {
            "captcha": {
                "type": CaptchaType.RECAPTCHA_V3,
                "websiteURL": website_url,
                "websiteKey": website_key,
            },
            "options": {},
        }
        if action:
            data["options"]["action"] = action
        if enterprise:
            data["options"]["enterprise"] = True
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

    async def RecaptchaV2(
        self,
        website_url: str,
        website_key: str,
        invisible: bool = False,
        enterprise: bool = False,
        proxy_scheme: str = "http",
        proxy_host: str = None,
        proxy_port: int = None,
        proxy_username: str = None,
        proxy_password: str = None,
    ) -> CaptchaResponse:
        """
        Solve a Google reCAPTCHA V2 challenge asynchronously.

        Args:
            website_url: The URL of the website with the CAPTCHA.
            website_key: The site key for the reCAPTCHA.
            invisible: Whether the CAPTCHA is invisible.
            enterprise: Whether it's the Enterprise version.
            proxy_scheme: Proxy protocol (http, socks4, socks5).
            proxy_host: Proxy host address.
            proxy_port: Proxy port number.
            proxy_username: Optional proxy username.
            proxy_password: Optional proxy password.

        Returns:
            CaptchaResponse: The result of the solved CAPTCHA task.
        """
        data = {
            "captcha": {
                "type": CaptchaType.RECAPTCHA_V2,
                "websiteURL": website_url,
                "websiteKey": website_key,
            },
            "options": {},
        }
        if invisible:
            data["options"]["invisible"] = True
        if enterprise:
            data["options"]["enterprise"] = True
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
