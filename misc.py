import math
from typing import Tuple


def roots(a: float, b: float, c: float) -> Tuple[float, float]:
    d = math.sqrt(b ** 2 - (4 * a * c))
    p = ((-1 * b) + d) / (2 * a)
    m = ((-1 * b) - d) / (2 * a)
    return p, m

