import logging

import coloredlogs

_format = "%(asctime)s [%(levelname)s] %(message)s"
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG', fmt=_format, logger=logger)
