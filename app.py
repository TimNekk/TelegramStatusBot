import asyncio
import logging

import coloredlogs
from telethon import TelegramClient

from checker import Checker, CheckReport
from config import SESSION_NAME, API_ID, API_HASH, BOTS, RESPONSE_TIME_LIMIT, TIME_BETWEEN_CHECKS, USERS_TO_NOTIFY
from logger import logger
from notifier import Notifier


async def main(telegram_client: TelegramClient):
    checker = Checker(telegram_client, BOTS, RESPONSE_TIME_LIMIT)
    notifier = Notifier(telegram_client, USERS_TO_NOTIFY)

    old_report: CheckReport = CheckReport()

    while True:
        report = await checker.check_bots()

        if report != old_report:
            old_report = report
            await notifier.notify(str(report))

        await asyncio.sleep(TIME_BETWEEN_CHECKS.total_seconds())

if __name__ == "__main__":
    client = TelegramClient(SESSION_NAME, API_ID, API_HASH)
    with client:
        client.loop.run_until_complete(main(client))
