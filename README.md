# Scrapely Python Client

The official Python client for [Scrapely.io](https://scrapely.io), a powerful API for web scraping and CAPTCHA solving.

## Features

- **Web Crawling**: Scrape websites with advanced options like screenshotting, resource blocking, and custom instructions (click, scroll, type, wait).
- **CAPTCHA Solving**: Solve Google reCAPTCHA (V2/V3) and Cloudflare Turnstile/Challenge.
- **Async Support**: Fully asynchronous client (`AsyncScrapely`) for high-concurrency applications.
- **Typed Responses**: All API responses are returned as typed Python objects for better IDE support and type safety.

## Installation

```bash
pip install scrapely-python-client
```

## Usage

### Synchronous Client

```python
from scrapely import Scrapely

client = Scrapely(api_key="YOUR_API_KEY")

# 1. Crawl a website
response = client.crawler.crawl(
    website_url="https://example.com",
    return_page_text=True
)
print(response.result.text)

# 2. Solve reCAPTCHA V3
captcha = client.google.RecaptchaV3(
    website_url="https://example.com",
    website_key="6LdKlZEpAAAAAAOQjzC2v_d36tWxCl6dWsozdSy9"
)
print(captcha.result.solution)
```

### Asynchronous Client

```python
import asyncio
from scrapely import AsyncScrapely

async def main():
    client = AsyncScrapely(api_key="YOUR_API_KEY")

    # 1. Crawl a website asynchronously
    response = await client.crawler.crawl(
        website_url="https://example.com",
        screenshot=True
    )
    print(f"Screenshot URL: {response.result.screenshot}")

    # 2. Solve Cloudflare Turnstile asynchronously
    captcha = await client.cloudflare.Turnstile(
        website_url="https://example.com",
        website_key="0x4AAAAAA..."
    )
    print(f"Token: {captcha.result.solution}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Advanced Usage

### Automation Instructions

You can pass a list of instructions to interact with the page before scraping.

```python
from scrapely import Scrapely
from scrapely.models.types import SendKeys, Click, Wait

client = Scrapely(api_key="YOUR_API_KEY")

instructions = [
    SendKeys(selector="#search", text="scraping"),
    Click(selector="#submit-button"),
    Wait(timeout=2) # Wait 2 seconds
]

response = client.crawler.crawl(
    website_url="https://example.com",
    instructions=instructions,
    return_page_text=True
)
```

### Response Objects

Responses are typed dataclasses:

- **`CrawlerResponse`**: Contains `result` (`CrawlerResult`) with fields like `html`, `text`, `cookies`, `screenshot`.
- **`CaptchaResponse`**: Contains `result` (`CaptchaResult`) with the `solution` string.

## License

MIT
