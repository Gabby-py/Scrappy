from pathlib import Path
import base64

# Gotta get the path to the parent directory this file resides in first
script_parent_dir = Path(__file__).resolve().parent

# For JetBrains Mono Medium version of font.
# with open(f"{script_parent_dir}/../fonts/JetBrainsMono-Medium.ttf", "rb") as JB_M_TTF:
#     encoded_string_b64_JB_M = base64.b64encode(JB_M_TTF.read()).decode("utf-8")

# For JetBrains Mono Regular version of font.
with open(f"{script_parent_dir}/../fonts/JetBrainsMono-Regular.ttf", "rb") as JB_R_TTF:
    encoded_string_b64_JB_R = base64.b64encode(JB_R_TTF.read()).decode("utf-8")

# Print them out, copy them and store as variables inside scrappy.py
# print("JETBRAINS_MEDIUM_B64:", encoded_string_b64_JB_M)
# print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("JETBRAINS_REGULAR_B64:", encoded_string_b64_JB_R)

# MEDIUM HAS BEEN SCRAPPED