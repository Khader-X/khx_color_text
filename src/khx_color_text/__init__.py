"""khx_color_text - A comprehensive package for printing colored and styled text in the terminal."""

from .core import cprint
from .colors.predefined import PREDEFINED_COLORS
from .styles.text_styles import TextStyle

__version__ = "0.2.0"
__all__ = ["cprint", "PREDEFINED_COLORS", "TextStyle"]
