"""
Scrapely Python Client Library
A comprehensive library for interacting with the Scrapely API
"""

from scrapely.core.client import Scrapely
from scrapely.core.async_client import AsyncScrapely
from scrapely.models.types import SendKeys, Click, Wait, ScrollIntoView, MouseClick
from scrapely.models.response import CrawlerResponse, CrawlerResult, CaptchaResponse, CaptchaResult
from scrapely._version import __version__

__all__ = [
    "Scrapely",
    "AsyncScrapely",
    "SendKeys",
    "Click",
    "Wait",
    "ScrollIntoView",
    "MouseClick",
    "CrawlerResponse",
    "CrawlerResult",
    "CaptchaResponse",
    "CaptchaResult",
    "__version__"
]