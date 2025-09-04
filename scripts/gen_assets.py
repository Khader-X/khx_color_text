"""Generate comprehensive SVG assets for documentation."""

import os
import sys
from pathlib import Path

# Add the src directory to Python path so we can import our package
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rich.console import Console
from rich.text import Text
from khx_color_text.colors.predefined import PREDEFINED_COLORS


def generate_svg_assets():
    """Generate SVG previews for colors, styles, and combinations."""
    # Create assets directory if it doesn't exist
    assets_dir = Path("docs/assets")
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Define pure, vibrant colors for better visual impact
    pure_colors = {
        "red": "#FF0000",
        "green": "#00FF00",
        "blue": "#0000FF",
        "yellow": "#FFFF00",
        "cyan": "#00FFFF",
        "magenta": "#FF00FF",
        "white": "#FFFFFF",
        "black": "#000000",
        "bright_red": "#FF5555",
        "bright_green": "#55FF55",
        "bright_blue": "#5555FF",
        "bright_yellow": "#FFFF55",
        "bright_cyan": "#55FFFF",
        "bright_magenta": "#FF55FF",
        "orange": "#FFA500",
        "purple": "#800080",
        "pink": "#FFC0CB",
        "gray": "#808080",
        "grey": "#808080",
    }

    generated_files = []

    # Generate individual color previews
    print("Generating color previews...")
    for color in sorted(PREDEFINED_COLORS.keys()):
        console = Console(record=True, width=80)

        hex_color = pure_colors.get(color, "#FFFFFF")
        text = Text(f"khx_color_text: {color} color example", style=hex_color)
        console.print(text)

        svg_path = assets_dir / f"color_{color}.svg"
        svg_content = console.export_svg(title=f"khx_color_text {color}")

        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated_files.append(svg_path)
        print(f"Generated: {svg_path}")

    # Generate style examples
    print("\nGenerating style examples...")
    styles = {
        "bold": "bold",
        "italic": "italic",
        "underline": "underline",
        "strikethrough": "strike",
        "dim": "dim",
        "bright": "bright",
    }

    for style_name, rich_style in styles.items():
        console = Console(record=True, width=80)

        text = Text(
            f"khx_color_text: {style_name} style example", style=f"blue {rich_style}"
        )
        console.print(text)

        svg_path = assets_dir / f"style_{style_name}.svg"
        svg_content = console.export_svg(title=f"khx_color_text {style_name}")

        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        generated_files.append(svg_path)
        print(f"Generated: {svg_path}")

    # Generate hex color examples
    print("\nGenerating hex color examples...")
    console = Console(record=True, width=100)

    hex_examples = ["#FF6B35", "#8A2BE2", "#FFD700", "#32CD32", "#FF1493"]
    for i, hex_color in enumerate(hex_examples):
        text = Text(f"{hex_color} ", style=hex_color)
        console.print(text, end="")
    console.print()  # New line

    svg_path = assets_dir / "hex_examples.svg"
    svg_content = console.export_svg(title="khx_color_text hex examples")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    generated_files.append(svg_path)
    print(f"Generated: {svg_path}")

    # Generate RGB color examples
    print("\nGenerating RGB color examples...")
    console = Console(record=True, width=100)

    rgb_examples = [
        ((255, 107, 53), "#FF6B35"),
        ((138, 43, 226), "#8A2BE2"),
        ((255, 215, 0), "#FFD700"),
        ((50, 205, 50), "#32CD32"),
        ((255, 20, 147), "#FF1493"),
    ]

    for rgb, hex_color in rgb_examples:
        text = Text(f"RGB{rgb} ", style=hex_color)
        console.print(text, end="")
    console.print()  # New line

    svg_path = assets_dir / "rgb_examples.svg"
    svg_content = console.export_svg(title="khx_color_text RGB examples")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    generated_files.append(svg_path)
    print(f"Generated: {svg_path}")

    # Generate combination examples
    print("\nGenerating combination examples...")
    console = Console(record=True, width=100)

    # Bold red
    text1 = Text("Bold Red ", style="red bold")
    console.print(text1, end="")

    # Italic blue
    text2 = Text("Italic Blue ", style="blue italic")
    console.print(text2, end="")

    # Underlined green
    text3 = Text("Underlined Green", style="green underline")
    console.print(text3)

    svg_path = assets_dir / "combinations.svg"
    svg_content = console.export_svg(title="khx_color_text combinations")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    generated_files.append(svg_path)
    print(f"Generated: {svg_path}")

    # Generate showcase
    print("\nGenerating showcase...")
    console = Console(record=True, width=120)

    console.print(
        "khx_color_text - Comprehensive Color and Style Support", style="bold blue"
    )
    console.print()

    # Show some colors
    basic_colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
    for color in basic_colors:
        hex_color = pure_colors.get(color, "#FFFFFF")
        text = Text(f"{color} ", style=hex_color)
        console.print(text, end="")
    console.print()

    # Show styles
    console.print()
    console.print("Styles: ", end="")
    console.print("bold", style="bold", end=" ")
    console.print("italic", style="italic", end=" ")
    console.print("underline", style="underline")

    svg_path = assets_dir / "showcase.svg"
    svg_content = console.export_svg(title="khx_color_text showcase")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)

    generated_files.append(svg_path)
    print(f"Generated: {svg_path}")

    print(f"\nSuccessfully generated {len(generated_files)} SVG files:")
    for file_path in generated_files:
        print(f"  - {file_path}")


if __name__ == "__main__":
    generate_svg_assets()
