from environs import Env

from bot_info import BotInfo

env = Env()
env.read_env()


API_ID = env.str("API_ID")
API_HASH = env.str("API_HASH")
SESSION_NAME = env.str("SESSION_NAME")

BOTS: list[BotInfo] = [BotInfo(*bot) for bot in env.json("BOTS")]

TIME_BETWEEN_CHECKS = env.timedelta("TIME_BETWEEN_CHECKS_IN_SECONDS")
RESPONSE_TIME_LIMIT = env.timedelta("RESPONSE_TIME_LIMIT_IN_SECONDS")

USERS_TO_NOTIFY = env.json("USERS_TO_NOTIFY")
