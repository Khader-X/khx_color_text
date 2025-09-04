# khx_color_text

Welcome to **khx_color_text** - a minimal Python package for printing colored text in the terminal with exactly five basic colors.

**🎉 Now live on PyPI!** 

## Quick Start

Install the package from PyPI:

```bash
pip install khx_color_text
```

[![PyPI version](https://badge.fury.io/py/khx-color-text.svg)](https://pypi.org/project/khx-color-text/)

Use it in Python:

```python
from khx_color_text import cprint

cprint("Hello World!", "cyan")
```

Or from the command line:

```bash
khx-ct "Hello World!" --color cyan
```

## Features

- **Five Colors**: red, green, blue, yellow, cyan
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Simple API**: Just one function `cprint(text, color)`
- **CLI Tool**: `khx-ct` command for terminal use
- **Lightweight**: Minimal dependencies (only colorama)

## Next Steps

- [Installation Guide](installation.md) - Detailed installation instructions
- [Examples](examples.md) - See all colors in action with visual previews
- [GitHub Repository](https://github.com/Khader-X/khx_color_text) - Source code and issues
- [PyPI Package](https://pypi.org/project/khx-color-text/) - Package details and statistics