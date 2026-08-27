from pathlib import Path
import base64

# Gotta get the path to the parent directory this file resides in first
script_parent_dir = Path(__file__).resolve().parent

# For JetBrains Mono Medium version of font.
with open(f"{script_parent_dir}/../images/icon.png", "rb") as ICON_PNG:
    encoded_string_b64_ICON = base64.b64encode(ICON_PNG.read()).decode("utf-8")

# Print them out, copy them and store as variables inside scrappy.py
print("ICON_PNG_B64:", encoded_string_b64_ICON)