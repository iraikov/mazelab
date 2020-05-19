
from dataclasses import dataclass
from typing import Tuple

@dataclass
class VonNeumannMotion:
    north: Tuple[int, int] = (-1, 0)
    south: Tuple[int, int] = (1, 0)
    west: Tuple[int, int] = (0, -1)
    east: Tuple[int, int] = (0, 1)

@dataclass
class MooreMotion:
    north: Tuple[int, int] = (-1, 0)
    south: Tuple[int, int] = (1, 0)
    west: Tuple[int, int] = (0, -1)
    east: Tuple[int, int] = (0, 1)
    northwest: Tuple[int, int] = (-1, -1)
    northeast: Tuple[int, int] = (-1, 1)
    southwest: Tuple[int, int] = (1, -1)
    southeast: Tuple[int, int] = (1, 1)
