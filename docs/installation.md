# Installation

## From PyPI (Recommended)

**khx_color_text** is available on the Python Package Index (PyPI). Install it using pip:

```bash
pip install khx_color_text
```

This will install the latest stable version along with its dependencies.

## Verify Installation

After installation, verify that everything works:

```bash
# Test the CLI
khx-ct "Hello World!" --color cyan

# Test in Python
python -c "from khx_color_text import cprint; cprint('Success!', 'green')"
```

## Requirements

- Python 3.9 or higher
- Windows, macOS, or Linux

## Dependencies

The package has minimal dependencies:
- `colorama>=0.4.6` - for cross-platform colored terminal output

## Development Installation

If you want to contribute or modify the package:

```bash
# Clone the repository
git clone https://github.com/Khader-X/khx_color_text.git
cd khx_color_text

# Install in development mode
pip install -e .[test,docs]

# Run tests
pytest -v
```

## Upgrading

To upgrade to the latest version:

```bash
pip install --upgrade khx_color_text
```

## Uninstalling

To remove the package:

```bash
pip uninstall khx_color_text
```