from dataclasses import dataclass
from typing import Optional


@dataclass
class BotInfo:
    username: int
    check_command: str
    response_message_text: Optional[str] = None
    ignore_response_message_text: Optional[bool] = False

    def __post_init__(self):
        if not self.response_message_text:
            self.ignore_response_message_text = True
