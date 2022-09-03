"""Run brainfuck code."""

try:
    from zombies_speed import BF
except ImportError:
    from .zombies import BF


__all__ = "BF"


__name__ = "zombies"
__author__ = "The Master"
__version__ = "1.0.0a"
__license__ = "MIT"
