"""
Custom exceptions for Scrapely API errors
"""
from typing import Optional, Dict, Any

class ScrapelyException(Exception):
    """Base exception for all Scrapely API errors"""
    
    def __init__(self, message: str, status_code: Optional[int] = None):
        """
        Initialize ScrapelyException.

        Args:
            message: Error message.
            status_code: HTTP status code associated with the error.
        """
        self.message = message
        self.status_code = status_code
        super().__init__(message)


# API Key Exceptions
class APIKeyRequired(ScrapelyException):
    """API key is required"""
    
    def __init__(self, message: str = "API key is required"):
        """Initialize APIKeyRequired exception."""
        super().__init__(message, 401)


class APIKeyInvalid(ScrapelyException):
    """Invalid API key"""
    
    def __init__(self, message: str = "Invalid API key"):
        """Initialize APIKeyInvalid exception."""
        super().__init__(message, 403)


# Instruction Exceptions
class InstructionInvalidType(ScrapelyException):
    """Instruction has invalid type"""
    
    def __init__(self, message: str = "Instruction has invalid type"):
        """Initialize InstructionInvalidType exception."""
        super().__init__(message, 400)


class InstructionActionRequired(ScrapelyException):
    """Instruction action is required"""
    
    def __init__(self, message: str = "Instruction action is required"):
        """Initialize InstructionActionRequired exception."""
        super().__init__(message, 400)


class InstructionActionInvalidType(ScrapelyException):
    """Instruction action has invalid type"""
    
    def __init__(self, message: str = "Instruction action has invalid type"):
        """Initialize InstructionActionInvalidType exception."""
        super().__init__(message, 400)


class InstructionActionInvalid(ScrapelyException):
    """Instruction action is invalid"""
    
    def __init__(self, message: str = "Instruction action is invalid"):
        """Initialize InstructionActionInvalid exception."""
        super().__init__(message, 400)


class InstructionSelectorRequired(ScrapelyException):
    """Instruction selector is required"""
    
    def __init__(self, message: str = "Instruction selector is required"):
        """Initialize InstructionSelectorRequired exception."""
        super().__init__(message, 400)


class InstructionSelectorConflict(ScrapelyException):
    """Instruction selector conflict"""
    
    def __init__(self, message: str = "Instruction selector conflict"):
        """Initialize InstructionSelectorConflict exception."""
        super().__init__(message, 400)


class InstructionSelectorInvalidType(ScrapelyException):
    """Instruction selector has invalid type"""
    
    def __init__(self, message: str = "Instruction selector has invalid type"):
        """Initialize InstructionSelectorInvalidType exception."""
        super().__init__(message, 400)


class InstructionXPathInvalidType(ScrapelyException):
    """Instruction XPath has invalid type"""
    
    def __init__(self, message: str = "Instruction XPath has invalid type"):
        """Initialize InstructionXPathInvalidType exception."""
        super().__init__(message, 400)


class InstructionTimeoutInvalidType(ScrapelyException):
    """Instruction timeout has invalid type"""
    
    def __init__(self, message: str = "Instruction timeout has invalid type"):
        """Initialize InstructionTimeoutInvalidType exception."""
        super().__init__(message, 400)


class InstructionTimeoutNegative(ScrapelyException):
    """Instruction timeout cannot be negative"""
    
    def __init__(self, message: str = "Instruction timeout cannot be negative"):
        """Initialize InstructionTimeoutNegative exception."""
        super().__init__(message, 400)

class InstructionTimeoutTooHigh(ScrapelyException):
    """Instruction timeout is too high"""
    
    def __init__(self, message: str = "Instruction timeout is too high"):
        """Initialize InstructionTimeoutTooHigh exception."""
        super().__init__(message, 400)


class InstructionIndexInvalidType(ScrapelyException):
    """Instruction index has invalid type"""
    
    def __init__(self, message: str = "Instruction index has invalid type"):
        """Initialize InstructionIndexInvalidType exception."""
        super().__init__(message, 400)


class InstructionIndexNegative(ScrapelyException):
    """Instruction index cannot be negative"""
    
    def __init__(self, message: str = "Instruction index cannot be negative"):
        """Initialize InstructionIndexNegative exception."""
        super().__init__(message, 400)


class InstructionTextRequired(ScrapelyException):
    """Instruction text is required"""
    
    def __init__(self, message: str = "Instruction text is required"):
        """Initialize InstructionTextRequired exception."""
        super().__init__(message, 400)


class InstructionTextInvalidType(ScrapelyException):
    """Instruction text has invalid type"""
    
    def __init__(self, message: str = "Instruction text has invalid type"):
        """Initialize InstructionTextInvalidType exception."""
        super().__init__(message, 400)


class InstructionTextTooLong(ScrapelyException):
    """Instruction text is too long"""
    
    def __init__(self, message: str = "Instruction text is too long"):
        """Initialize InstructionTextTooLong exception."""
        super().__init__(message, 400)


class InstructionsTotalTimeoutExceeded(ScrapelyException):
    """Total instructions timeout exceeded"""
    
    def __init__(self, message: str = "Total instructions timeout exceeded"):
        """Initialize InstructionsTotalTimeoutExceeded exception."""
        super().__init__(message, 400)


# Task Validation Exceptions
class InvalidFields(ScrapelyException):
    """Invalid fields provided"""
    
    def __init__(self, message: str = "Invalid fields provided"):
        """Initialize InvalidFields exception."""
        super().__init__(message, 400)


class AmbiguousTaskType(ScrapelyException):
    """Ambiguous task type"""
    
    def __init__(self, message: str = "Cannot provide both 'captcha' and 'crawler' objects"):
        """Initialize AmbiguousTaskType exception."""
        super().__init__(message, 400)


class TaskTypeRequired(ScrapelyException):
    """Task type is required"""
    
    def __init__(self, message: str = "Either 'captcha' or 'crawler' object is required"):
        """Initialize TaskTypeRequired exception."""
        super().__init__(message, 400)


# Captcha Exceptions
class InvalidCaptchaFields(ScrapelyException):
    """Invalid captcha fields"""
    
    def __init__(self, message: str = "Invalid captcha fields"):
        """Initialize InvalidCaptchaFields exception."""
        super().__init__(message, 400)


class InvalidCaptchaType(ScrapelyException):
    """Invalid captcha type"""
    
    def __init__(self, message: str = "Invalid captcha type"):
        """Initialize InvalidCaptchaType exception."""
        super().__init__(message, 400)


class CaptchaWebsiteUrlRequired(ScrapelyException):
    """Captcha website URL is required"""
    
    def __init__(self, message: str = "Captcha website URL is required"):
        """Initialize CaptchaWebsiteUrlRequired exception."""
        super().__init__(message, 400)


class CaptchaWebsiteUrlInvalidType(ScrapelyException):
    """Captcha website URL has invalid type"""
    
    def __init__(self, message: str = "Captcha website URL has invalid type"):
        """Initialize CaptchaWebsiteUrlInvalidType exception."""
        super().__init__(message, 400)


class CaptchaWebsiteUrlInvalidScheme(ScrapelyException):
    """Captcha website URL has invalid scheme"""
    
    def __init__(self, message: str = "Captcha website URL has invalid scheme"):
        """Initialize CaptchaWebsiteUrlInvalidScheme exception."""
        super().__init__(message, 400)


class CaptchaWebsiteUrlTooLong(ScrapelyException):
    """Captcha website URL is too long"""
    
    def __init__(self, message: str = "Captcha website URL is too long"):
        """Initialize CaptchaWebsiteUrlTooLong exception."""
        super().__init__(message, 400)


class CaptchaWebsiteKeyRequired(ScrapelyException):
    """Captcha website key is required"""
    
    def __init__(self, message: str = "Captcha website key is required"):
        """Initialize CaptchaWebsiteKeyRequired exception."""
        super().__init__(message, 400)


class CaptchaWebsiteKeyInvalidType(ScrapelyException):
    """Captcha website key has invalid type"""
    
    def __init__(self, message: str = "Captcha website key has invalid type"):
        """Initialize CaptchaWebsiteKeyInvalidType exception."""
        super().__init__(message, 400)


class CaptchaWebsiteKeyTooShort(ScrapelyException):
    """Captcha website key is too short"""
    
    def __init__(self, message: str = "Captcha website key is too short"):
        """Initialize CaptchaWebsiteKeyTooShort exception."""
        super().__init__(message, 400)


class CaptchaWebsiteKeyTooLong(ScrapelyException):
    """Captcha website key is too long"""
    
    def __init__(self, message: str = "Captcha website key is too long"):
        """Initialize CaptchaWebsiteKeyTooLong exception."""
        super().__init__(message, 400)


class CaptchaTypeRequired(ScrapelyException):
    """Captcha type is required"""
    
    def __init__(self, message: str = "Captcha type is required"):
        """Initialize CaptchaTypeRequired exception."""
        super().__init__(message, 400)


class CaptchaTypeInvalidType(ScrapelyException):
    """Captcha type has invalid type"""
    
    def __init__(self, message: str = "Captcha type has invalid type"):
        """Initialize CaptchaTypeInvalidType exception."""
        super().__init__(message, 400)


class InvalidCrawlerFields(ScrapelyException):
    """Invalid crawler fields"""
    
    def __init__(self, message: str = "Invalid crawler fields"):
        """Initialize InvalidCrawlerFields exception."""
        super().__init__(message, 400)


class CrawlerWebsiteUrlRequired(ScrapelyException):
    """Crawler website URL is required"""
    
    def __init__(self, message: str = "Crawler website URL is required"):
        """Initialize CrawlerWebsiteUrlRequired exception."""
        super().__init__(message, 400)


class CrawlerWebsiteUrlInvalidType(ScrapelyException):
    """Crawler website URL has invalid type"""
    
    def __init__(self, message: str = "Crawler website URL has invalid type"):
        """Initialize CrawlerWebsiteUrlInvalidType exception."""
        super().__init__(message, 400)


class CrawlerWebsiteUrlInvalidScheme(ScrapelyException):
    """Crawler website URL has invalid scheme"""
    
    def __init__(self, message: str = "Crawler website URL has invalid scheme"):
        """Initialize CrawlerWebsiteUrlInvalidScheme exception."""
        super().__init__(message, 400)


class CrawlerWebsiteUrlTooLong(ScrapelyException):
    """Crawler website URL is too long"""
    
    def __init__(self, message: str = "Crawler website URL is too long"):
        """Initialize CrawlerWebsiteUrlTooLong exception."""
        super().__init__(message, 400)


class CrawlerBlockResourcesInvalidType(ScrapelyException):
    """Crawler block resources has invalid type"""
    
    def __init__(self, message: str = "Crawler block resources has invalid type"):
        """Initialize CrawlerBlockResourcesInvalidType exception."""
        super().__init__(message, 400)


class CrawlerDeviceInvalidType(ScrapelyException):
    """Crawler device has invalid type"""
    
    def __init__(self, message: str = "Crawler device has invalid type"):
        """Initialize CrawlerDeviceInvalidType exception."""
        super().__init__(message, 400)


class CrawlerDeviceInvalidValue(ScrapelyException):
    """Crawler device has invalid value"""
    
    def __init__(self, message: str = "Crawler device has invalid value"):
        """Initialize CrawlerDeviceInvalidValue exception."""
        super().__init__(message, 400)


class CrawlerScreenshotInvalidType(ScrapelyException):
    """Crawler screenshot has invalid type"""
    
    def __init__(self, message: str = "Crawler screenshot has invalid type"):
        """Initialize CrawlerScreenshotInvalidType exception."""
        super().__init__(message, 400)


class CrawlerScreenshotFullPageInvalidType(ScrapelyException):
    """Crawler screenshot full page has invalid type"""
    
    def __init__(self, message: str = "Crawler screenshot full page has invalid type"):
        """Initialize CrawlerScreenshotFullPageInvalidType exception."""
        super().__init__(message, 400)

class CrawlerScreenshotConflict(ScrapelyException):
    """Crawler screenshot conflict"""
    
    def __init__(self, message: str = "Crawler screenshot conflict"):
        """Initialize CrawlerScreenshotConflict exception."""
        super().__init__(message, 400)


class CrawlerReturnPageSourceInvalidType(ScrapelyException):
    """Crawler return page source has invalid type"""
    
    def __init__(self, message: str = "Crawler return page source has invalid type"):
        """Initialize CrawlerReturnPageSourceInvalidType exception."""
        super().__init__(message, 400)

class CrawlerReturnPageTextInvalidType(ScrapelyException):
    """Crawler return page text has invalid type"""
    def __init__(self, message: str = "Crawler return page text has invalid type"):
        """Initialize CrawlerReturnPageTextInvalidType exception."""
        super().__init__(message, 400)

def raise_scrapely_exception(error_obj: Dict[str, Any], status_code: int) -> None:
    """Raise appropriate ScrapelyException based on error response"""
    error_message = error_obj.get("message", "Unknown error")
    error_type = error_obj.get("type", "unknown")
    exception_map = {
        "api_key_required": APIKeyRequired,
        "api_key_invalid": APIKeyInvalid,
        "instruction_invalid_type": InstructionInvalidType,
        "instruction_action_required": InstructionActionRequired,
        "instruction_action_invalid_type": InstructionActionInvalidType,
        "instruction_action_invalid": InstructionActionInvalid,
        "instruction_selector_required": InstructionSelectorRequired,
        "instruction_selector_conflict": InstructionSelectorConflict,
        "instruction_selector_invalid_type": InstructionSelectorInvalidType,
        "instruction_xpath_invalid_type": InstructionXPathInvalidType,
        "instruction_timeout_invalid_type": InstructionTimeoutInvalidType,
        "instruction_timeout_negative": InstructionTimeoutNegative,
        "instruction_timeout_too_high": InstructionTimeoutTooHigh,
        "instruction_index_invalid_type": InstructionIndexInvalidType,
        "instruction_index_negative": InstructionIndexNegative,
        "instruction_text_required": InstructionTextRequired,
        "instruction_text_invalid_type": InstructionTextInvalidType,
        "instruction_text_too_long": InstructionTextTooLong,
        "instructions_total_timeout_exceeded": InstructionsTotalTimeoutExceeded,
        "invalid_fields": InvalidFields,
        "ambiguous_task_type": AmbiguousTaskType,
        "task_type_required": TaskTypeRequired,
        "invalid_captcha_fields": InvalidCaptchaFields,
        "invalid_captcha_type": InvalidCaptchaType,
        "captcha_website_url_required": CaptchaWebsiteUrlRequired,
        "captcha_website_url_invalid_type": CaptchaWebsiteUrlInvalidType,
        "captcha_website_url_invalid_scheme": CaptchaWebsiteUrlInvalidScheme,
        "captcha_website_url_too_long": CaptchaWebsiteUrlTooLong,
        "captcha_website_key_required": CaptchaWebsiteKeyRequired,
        "captcha_website_key_invalid_type": CaptchaWebsiteKeyInvalidType,
        "captcha_website_key_too_short": CaptchaWebsiteKeyTooShort,
        "captcha_website_key_too_long": CaptchaWebsiteKeyTooLong,
        "captcha_type_required": CaptchaTypeRequired,
        "captcha_type_invalid_type": CaptchaTypeInvalidType,
        "invalid_crawler_fields": InvalidCrawlerFields,
        "crawler_website_url_required": CrawlerWebsiteUrlRequired,
        "crawler_website_url_invalid_type": CrawlerWebsiteUrlInvalidType,
        "crawler_website_url_invalid_scheme": CrawlerWebsiteUrlInvalidScheme,
        "crawler_website_url_too_long": CrawlerWebsiteUrlTooLong,
        "crawler_block_resources_invalid_type": CrawlerBlockResourcesInvalidType,
        "crawler_device_invalid_type": CrawlerDeviceInvalidType,
        "crawler_device_invalid_value": CrawlerDeviceInvalidValue,
        "crawler_screenshot_invalid_type": CrawlerScreenshotInvalidType,
        "crawler_screenshot_full_page_invalid_type": CrawlerScreenshotFullPageInvalidType,
        "crawler_screenshot_conflict": CrawlerScreenshotConflict,
        "crawler_return_page_source_invalid_type": CrawlerReturnPageSourceInvalidType,
        "crawler_return_page_text_invalid_type": CrawlerReturnPageTextInvalidType,
    }
    exception_class = exception_map.get(error_type, ScrapelyException)
    raise exception_class(error_message, status_code)