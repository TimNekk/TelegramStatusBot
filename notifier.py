from typing import Collection

from telethon import TelegramClient


class Notifier:
    def __init__(self, client: TelegramClient, users_to_notify: Collection[str]):
        self.client = client
        self.users_to_notify = users_to_notify

    async def notify(self, message: str):
        for user in self.users_to_notify:
            await self.client.send_message(user, message)
