from __future__ import annotations
from scrapely.models.exceptions import raise_scrapely_exception
from scrapely.models.response import OcrResponse


class Ocr:
    def __init__(self, instance):
        """
        Initialize the Ocr service.

        Args:
            instance (Scrapely): The Scrapely client instance.
        """
        from scrapely.core.client import Scrapely
        assert isinstance(instance, Scrapely)
        self.instance = instance

    def solve(
        self,
        image: str,
    ) -> OcrResponse:
        """
        Solve an OCR challenge.

        Args:
            image: Base64-encoded image string or data URI (data:image/...;base64,...).
                   Maximum image size is 100KB.

        Returns:
            OcrResponse: The result of the OCR task containing the recognized text.
        """
        data = {
            "ocr": {
                "image": image,
            }
        }
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
            return OcrResponse.from_dict(response_dict)


class AsyncOcr:
    def __init__(self, instance):
        """
        Initialize the AsyncOcr service.

        Args:
            instance (AsyncScrapely): The AsyncScrapely client instance.
        """
        from scrapely.core.async_client import AsyncScrapely
        assert isinstance(instance, AsyncScrapely)
        self.instance = instance

    async def solve(
        self,
        image: str,
    ) -> OcrResponse:
        """
        Solve an OCR challenge asynchronously.

        Args:
            image: Base64-encoded image string or data URI (data:image/...;base64,...).
                   Maximum image size is 100KB.

        Returns:
            OcrResponse: The result of the OCR task containing the recognized text.
        """
        data = {
            "ocr": {
                "image": image,
            }
        }
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
            return OcrResponse.from_dict(response_dict)