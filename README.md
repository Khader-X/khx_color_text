# khx_color_text

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![PyPI version](https://badge.fury.io/py/khx-color-text.svg)](https://badge.fury.io/py/khx-color-text)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CI Status](https://img.shields.io/badge/CI-passing-green.svg)](https://github.com/Khader-X/khx_color_text/actions)
[![Downloads](https://pepy.tech/badge/khx-color-text)](https://pepy.tech/project/khx-color-text)

A minimal Python package for printing colored text in the terminal with exactly five basic colors.

**🎉 Now available on PyPI!** Install with: `pip install khx_color_text`

## Installation

```bash
pip install khx_color_text
```

## Usage

### Python API

```python
from khx_color_text import cprint

# Print text in different colors
cprint("Hello World!", "red")
cprint("Success message", "green")
cprint("Information", "blue")
cprint("Warning", "yellow")
cprint("Highlight", "cyan")
```

### Command Line Interface

```bash
# Basic usage
khx-ct "Hello World!" --color red

# Default color is cyan
khx-ct "Hello World!"

# All available colors
khx-ct "Red text" --color red
khx-ct "Green text" --color green
khx-ct "Blue text" --color blue
khx-ct "Yellow text" --color yellow
khx-ct "Cyan text" --color cyan
```

## Examples

### Red
```python
cprint("Hello from khx_color_text in red!", "red")
```
<img src="docs/assets/color_red.svg" alt="Red example" width="520">

### Green
```python
cprint("Hello from khx_color_text in green!", "green")
```
<img src="docs/assets/color_green.svg" alt="Green example" width="520">

### Blue
```python
cprint("Hello from khx_color_text in blue!", "blue")
```
<img src="docs/assets/color_blue.svg" alt="Blue example" width="520">

### Yellow
```python
cprint("Hello from khx_color_text in yellow!", "yellow")
```
<img src="docs/assets/color_yellow.svg" alt="Yellow example" width="520">

### Cyan
```python
cprint("Hello from khx_color_text in cyan!", "cyan")
```
<img src="docs/assets/color_cyan.svg" alt="Cyan example" width="520">

## How Previews Are Generated

The SVG previews above are generated deterministically using the `scripts/gen_assets.py` script. This script uses Rich Console with a fixed width (60 characters) to capture the colored output and export it as SVG files. The previews are automatically regenerated on each push to the main branch via GitHub Actions.

To regenerate the previews locally:

```bash
pip install -e .[docs]
python scripts/gen_assets.py
```

## Supported Colors

The package supports exactly five colors:
- `red`
- `green` 
- `blue`
- `yellow`
- `cyan`

## Cross-Platform Support

This package uses `colorama` to ensure colored output works correctly on Windows, macOS, and Linux terminals.

## Package Statistics

- **PyPI**: https://pypi.org/project/khx-color-text/
- **Source Code**: https://github.com/Khader-X/khx_color_text
- **Documentation**: https://khader-x.github.io/khx_color_text/
- **Issues**: https://github.com/Khader-X/khx_color_text/issues

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details.

## Author

**ABUELTAYEF Khader**
- Email: abueltayef.khader@gmail.com
- GitHub Personal: [@Khader20](https://github.com/Khader20)
- GitHub Organization: [@Khader-X](https://github.com/Khader-X)
- PyPI: [Khader20](https://pypi.org/user/Khader20/)