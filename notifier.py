from typing import Collection

from telethon import TelegramClient

from logger import logger


class Notifier:
    def __init__(self, client: TelegramClient, users_to_notify: Collection[str]):
        self.client = client
        self.users_to_notify = users_to_notify

    async def notify(self, message: str):
        logger.info("Start notifying...")
        for index, user in enumerate(self.users_to_notify):
            await self.client.send_message(user, message)
            logger.info(f"{index + 1}/{len(self.users_to_notify)} Notified {user}")
        logger.info("End notifying")
