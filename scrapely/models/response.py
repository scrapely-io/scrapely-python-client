from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

@dataclass
class CrawlerResult:
    """Result data from a crawler task"""
    html: str = ""
    text: str = ""
    screenshot: str = ""
    user_agent: str = ""
    cookies: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    instructions: List[Any] = field(default_factory=list)

@dataclass
class CrawlerResponse:
    """Response from a crawler task"""
    success: bool
    task_id: str
    status: str
    created_at: str
    result: CrawlerResult
    completed_at: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CrawlerResponse":
        result_data = data.get("result", {})
        result = CrawlerResult(
            html=result_data.get("html", ""),
            text=result_data.get("text", ""),
            screenshot=result_data.get("screenshot", ""),
            user_agent=result_data.get("user_agent", ""),
            cookies=result_data.get("cookies", {}),
            metadata=result_data.get("metadata", {}),
            instructions=result_data.get("instructions", [])
        )
        return cls(
            success=data.get("success", False),
            task_id=data.get("task_id", ""),
            status=data.get("status", ""),
            created_at=data.get("created_at", ""),
            completed_at=data.get("completed_at"),
            result=result
        )

@dataclass
class CaptchaResult:
    """Result data from a captcha task"""
    solution: str = ""

@dataclass
class CaptchaResponse:
    """Response from a captcha task"""
    success: bool
    task_id: str
    status: str
    created_at: str
    result: CaptchaResult
    completed_at: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CaptchaResponse":
        result_data = data.get("result", {})
        result = CaptchaResult(
            solution=result_data.get("solution", "")
        )
        return cls(
            success=data.get("success", False),
            task_id=data.get("task_id", ""),
            status=data.get("status", ""),
            created_at=data.get("created_at", ""),
            completed_at=data.get("completed_at"),
            result=result
        )
