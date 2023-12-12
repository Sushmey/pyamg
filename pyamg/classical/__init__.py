"""Classical AMG."""

from . import air
from . import classical
from . import split
from . import interpolate
from . import cr

from .classical import ruge_stuben_solver
from .air import air_solver
from .air_schwarz import air_schwarz_solver

__all__ = [
    'air',
    'classical',
    'split',
    'interpolate',
    'cr',
    'ruge_stuben_solver',
    'air_solver',
    'air_schwarz_solver'
]
