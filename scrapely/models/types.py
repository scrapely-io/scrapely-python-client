"""
Type definitions for Scrapely instructions and data structures
"""
from typing import Optional, Union
from dataclasses import dataclass

class InstructionBase:
    """Base class for all instructions"""
    def to_dict(self) -> dict:
        """Convert instruction to dictionary format for API"""
        raise NotImplementedError("Subclasses must implement to_dict method")

@dataclass
class SendKeys(InstructionBase):
    """Send keys instruction for form input"""
    text: str
    selector: Optional[str] = None
    xpath: Optional[str] = None
    timeout: int = 5
    index: int = 0
    def to_dict(self) -> dict:
        """
        Convert the SendKeys instruction to a dictionary for the API.

        Returns:
            dict: The dictionary representation of the instruction.

        Raises:
            ValueError: If neither selector nor xpath is provided, or both are.
        """
        if not self.selector and not self.xpath:
            raise ValueError("Either selector or xpath must be provided")
        if self.selector and self.xpath:
            raise ValueError("Cannot use both selector and xpath")
        instruction = {
            "action": "send_keys",
            "text": self.text,
            "timeout": self.timeout,
        }
        if self.selector:
            instruction["selector"] = self.selector
        elif self.xpath:
            instruction["xpath"] = self.xpath
            instruction["index"] = self.index
        return instruction

@dataclass
class Click(InstructionBase):
    """Click instruction for buttons and links"""
    selector: Optional[str] = None
    xpath: Optional[str] = None
    timeout: int = 5
    index: int = 0
    def to_dict(self) -> dict:
        """
        Convert the Click instruction to a dictionary for the API.

        Returns:
            dict: The dictionary representation of the instruction.

        Raises:
            ValueError: If neither selector nor xpath is provided, or both are.
        """
        if not self.selector and not self.xpath:
            raise ValueError("Either selector or xpath must be provided")
        if self.selector and self.xpath:
            raise ValueError("Cannot use both selector and xpath")
        instruction = {
            "action": "click",
            "timeout": self.timeout,
        }
        if self.selector:
            instruction["selector"] = self.selector
        elif self.xpath:
            instruction["xpath"] = self.xpath
            instruction["index"] = self.index
        return instruction


@dataclass
class MouseClick(InstructionBase):
    """Mouse click instruction for elements that require physical mouse interaction"""
    selector: Optional[str] = None
    xpath: Optional[str] = None
    timeout: int = 5
    index: int = 0
    def to_dict(self) -> dict:
        """
        Convert the MouseClick instruction to a dictionary for the API.

        Returns:
            dict: The dictionary representation of the instruction.

        Raises:
            ValueError: If neither selector nor xpath is provided, or both are.
        """
        if not self.selector and not self.xpath:
            raise ValueError("Either selector or xpath must be provided")
        if self.selector and self.xpath:
            raise ValueError("Cannot use both selector and xpath")
        instruction = {
            "action": "mouse_click",
            "timeout": self.timeout,
        }
        if self.selector:
            instruction["selector"] = self.selector
        elif self.xpath:
            instruction["xpath"] = self.xpath
            instruction["index"] = self.index
        return instruction


@dataclass
class Wait(InstructionBase):
    """Wait instruction for delays"""
    selector: Optional[str] = None
    xpath: Optional[str] = None
    timeout: int = 5
    index: int = 0
    def to_dict(self) -> dict:
        """
        Convert the Wait instruction to a dictionary for the API.

        Returns:
            dict: The dictionary representation of the instruction.

        Raises:
            ValueError: If neither selector nor xpath is provided, or both are.
        """
        if self.selector and self.xpath:
            raise ValueError("Cannot use both selector and xpath")
        instruction = {
            "action": "wait",
            "timeout": self.timeout,
        }
        if self.selector:
            instruction["selector"] = self.selector
        elif self.xpath:
            instruction["xpath"] = self.xpath
            instruction["index"] = self.index
        return instruction

@dataclass
class ScrollIntoView(InstructionBase):
    """Scroll element into view instruction"""
    selector: Optional[str] = None
    xpath: Optional[str] = None
    timeout: int = 5
    index: int = 0
    def to_dict(self) -> dict:
        """
        Convert the ScrollIntoView instruction to a dictionary for the API.

        Returns:
            dict: The dictionary representation of the instruction.

        Raises:
            ValueError: If neither selector nor xpath is provided, or both are.
        """
        if not self.selector and not self.xpath:
            raise ValueError("Either selector or xpath must be provided")
        if self.selector and self.xpath:
            raise ValueError("Cannot use both selector and xpath")
        instruction = {
            "action": "scroll_into_view",
            "timeout": self.timeout,
        }
        if self.selector:
            instruction["selector"] = self.selector
        elif self.xpath:
            instruction["xpath"] = self.xpath
            instruction["index"] = self.index
        return instruction

Instruction = Union[SendKeys, Click, Wait, ScrollIntoView, MouseClick]