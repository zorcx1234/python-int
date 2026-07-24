"""
Exceptions erheben: raise
"""

import logging

logger = logging.getLogger(__name__)


class AreaException(Exception):
    pass


def area(a: float, b: float) -> float:
    """Fläche eines Rechtecks.

    Raises:
        ValueError, wenn a oder b < 0
    """
    if a < 0 or b < 0:
        logger.error("Ein Fehler ist aufgetretetn")
        raise AreaException(
            "Eine Fläche aus negativer Seitenlänge kann nicht berechnet werden"
        )

    return a * b


try:
    result = area(-1, 1)
except ValueError as e:
    print(e)
except AreaException as e:
    print("Area Excpetion", e)
