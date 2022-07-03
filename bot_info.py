from dataclasses import dataclass


@dataclass
class BotInfo:
    username: int
    check_command: str
    response_message: str
