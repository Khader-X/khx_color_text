# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-01-09

### 🎉 Major Feature Release

This release transforms khx_color_text from a simple 5-color package into a comprehensive terminal styling solution while maintaining the same simple API.

### ✨ Added

#### Color Support
- **21 predefined colors**: Added magenta, white, black, and bright variants
- **Color aliases**: orange, purple, pink, gray, grey for better usability
- **Hex color support**: Full (#FF0000) and short (#f00) hex formats
- **RGB color support**: RGB tuples like (255, 0, 0)
- **Background colors**: Support for all color formats as backgrounds

#### Text Styling
- **6 text styles**: bold, italic, underline, strikethrough, dim, bright
- **Multiple styles**: Combine multiple styles like ["bold", "underline"]
- **TextStyle enum**: Type-safe styling with TextStyle.BOLD, etc.

#### Enhanced API
- **Backward compatible**: Existing code continues to work unchanged
- **Optional parameters**: color, bg_color, style all optional
- **Standard print parameters**: end, sep, file support
- **Type hints**: Full type safety with Union types

#### CLI Enhancements
- **Multiple color formats**: --hex, --rgb, --bg-hex, --bg-rgb options
- **Style support**: -s/--style with comma-separated multiple styles
- **Built-in examples**: --examples, --advanced-examples, --showcase
- **Color listing**: --list-colors to see all available colors
- **Comprehensive help**: Detailed usage examples in help text

#### Architecture
- **Modular structure**: Organized into colors/, styles/, examples/ modules
- **Color utilities**: hex_to_rgb, rgb_to_ansi, validate_hex, validate_rgb
- **Style utilities**: TextStyle enum, style combination functions
- **Background support**: Unified background color handling

#### Documentation & Testing
- **Comprehensive examples**: 3 example modules with if __name__ == "__main__"
- **Test suite**: 3 test modules covering all functionality (no pytest)
- **Enhanced SVGs**: 31+ SVG assets showing all features
- **Updated docs**: Complete documentation rewrite with visual examples

### 🔧 Changed
- **Version**: Updated from 0.1.0 to 0.2.0
- **Package description**: Updated to reflect comprehensive features
- **Import structure**: Added TextStyle and PREDEFINED_COLORS exports
- **CLI interface**: Complete rewrite with new argument structure
- **SVG generation**: Enhanced script generating comprehensive visual assets

### 🏗️ Technical Details
- **No breaking changes**: All existing code continues to work
- **No new dependencies**: Still only requires colorama
- **Type safety**: No type: ignore comments, clean type hints
- **Cross-platform**: Tested on Windows, maintains macOS/Linux support
- **Performance**: Efficient color processing with caching where appropriate

### 📊 Statistics
- **Colors**: 5 → 21+ predefined colors
- **Formats**: 1 → 3 color formats (predefined, hex, RGB)
- **Styles**: 0 → 6 text styles
- **CLI options**: 3 → 15+ command-line options
- **Test coverage**: Basic → Comprehensive (3 test modules)
- **Documentation**: Minimal → Extensive with visual examples

## [0.1.0] - 2024-12-XX

### 🎉 Initial Release

- **Basic colored text**: Support for 5 colors (red, green, blue, yellow, cyan)
- **Simple API**: Single `cprint(text, color)` function
- **Cross-platform**: Windows, macOS, Linux support via colorama
- **CLI tool**: Basic `khx-ct` command-line interface
- **Type hints**: Full type safety with Literal types
- **Documentation**: Basic README and examples
- **PyPI package**: Published to Python Package Index
- **GitHub Actions**: CI/CD pipeline with automated testing
- **SVG assets**: Basic color preview generation

### Technical Foundation
- **Build system**: Hatchling-based build with PEP 621 compliance
- **Dependencies**: Minimal (only colorama)
- **Testing**: Basic pytest-based test suite
- **Documentation**: MkDocs-based documentation site
- **License**: MIT License
- **Python support**: 3.9+

---

## Migration Guide

### From 0.1.0 to 0.2.0

**✅ No breaking changes!** All existing code continues to work unchanged.

#### What stays the same:
```python
from khx_color_text import cprint

# This still works exactly the same
cprint("Hello World!", "red")
cprint("Success!", "green")
```

#### What you can now do additionally:
```python
from khx_color_text import cprint, TextStyle

# New color formats
cprint("Hex color", "#FF6B35")
cprint("RGB color", (255, 107, 53))

# New predefined colors
cprint("Orange text", "orange")
cprint("Bright red", "bright_red")

# Text styling
cprint("Bold text", "red", style="bold")
cprint("Multiple styles", "blue", style=["bold", "underline"])

# Background colors
cprint("Highlighted", "white", bg_color="red")

# Complex combinations
cprint("Fancy", "#00FF00", bg_color=(50, 50, 50), style=TextStyle.BOLD)
```

#### CLI Migration:
```bash
# Old way (still works)
khx-ct "Hello" --color red

# New capabilities
khx-ct "Hello" -c red              # Shorter option
khx-ct "Custom" --hex "#FF6B35"    # Hex colors
khx-ct "RGB" --rgb "255,0,0"       # RGB colors
khx-ct "Styled" -c blue -s bold    # With styling
khx-ct --examples                  # Built-in examples
```

## Future Roadmap

### Planned for 0.3.0
- **Color themes**: Predefined color schemes
- **Configuration files**: Save preferred colors/styles
- **More background styles**: Patterns, gradients
- **Performance optimizations**: Faster color processing
- **Plugin system**: Extensible color/style plugins

### Under Consideration
- **True color support**: 24-bit color terminals
- **Color palettes**: Import/export color schemes
- **Interactive mode**: Live color picker
- **Template system**: Reusable styled text templates
- **Logging integration**: Colored logging handlers

---

**Full Changelog**: https://github.com/Khader-X/khx_color_text/compare/v0.1.0...v0.2.0