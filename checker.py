import asyncio
from datetime import datetime, timedelta
from typing import Collection, Optional

from telethon import TelegramClient

from bot_info import BotInfo


class CheckReport:
    def __init__(self, bots_status: Optional[dict[str, bool]] = None):
        self.bots_status = bots_status or {}

    def __getitem__(self, key):
        return self.bots_status.get(key)

    def __setitem__(self, key, value):
        self.bots_status[key] = value

    def __str__(self):
        result = []
        for bot, is_online in self.bots_status.items():
            result.append(f"{'✅' if is_online else '❌'} {bot}")
        return '\n'.join(result)

    def __eq__(self, other):
        return self.bots_status == other.bots_status

    def __ne__(self, other):
        return not self.__eq__(other)


class Checker:
    def __init__(self,
                 client: TelegramClient,
                 bots: Collection[BotInfo],
                 response_time_limit: timedelta = timedelta(minutes=1)):
        self.client = client
        self.bots = bots
        self.response_time_limit = response_time_limit

    async def check_bots(self) -> CheckReport:
        report = CheckReport()

        for bot in self.bots:
            is_online = await self.check_bot(bot)
            report[bot.username] = is_online

        return report

    async def check_bot(self, bot: BotInfo) -> bool:
        print(f"Checking {bot.username}")
        await self.client.send_message(bot.username, bot.check_command)
        response = await self.get_response(bot)
        return response

    async def get_response(self, bot: BotInfo) -> bool:
        start_time = datetime.utcnow().replace(microsecond=0)

        while datetime.utcnow() - start_time < self.response_time_limit:
            messages = await self.client.get_messages(bot.username)
            response_messages = tuple(filter(lambda m: m.out is False and m.date.timestamp() >= start_time.timestamp(), messages))

            if response_messages and (response_messages[0].text == bot.response_message_text or bot.ignore_response_message_text):
                return True

            await asyncio.sleep(1)

        return False
