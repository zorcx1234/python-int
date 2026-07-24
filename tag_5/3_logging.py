"""
Logging in Python
Alternative: loguru (https://github.com/delgan/loguru)

Severity Grades
----------------
DEBUG
INFO
WARNING << ab hier und aufwärts
ERROR
CRITICAL

logger -> 1 oder mehrere Handler (FileHandler, StreamHanlder) -> Formatter
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # von DEBUG bis CRITICAL

handler = logging.FileHandler("debug.log")  # auf Konsole
handler.setLevel(logging.DEBUG)  # von DEBUG bis CRITICAL

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.error("Fehler ist aufgetreten!")
logger.info("DAs ist eine Info")
