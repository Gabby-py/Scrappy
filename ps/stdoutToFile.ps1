Write-Output "ttf to b64 converter errors start here" > "$PSScriptRoot/ps_script_error.txt"
Write-Output "==================================================================" >> "$PSScriptRoot/ps_script_error.txt"
py.exe "$PSScriptRoot/../b64/ttfToB64.py" > "$PSScriptRoot/../b64/font_base64.txt" 2>> "$PSScriptRoot/ps_script_error.txt"

Write-Output "" >> "$PSScriptRoot/ps_script_error.txt"
Write-Output ":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::" >> "$PSScriptRoot/ps_script_error.txt"
Write-Output "" >> "$PSScriptRoot/ps_script_error.txt"

Write-Output "image to b64 converter errors start here" >> "$PSScriptRoot/ps_script_error.txt"
Write-Output "==================================================================" >> "$PSScriptRoot/ps_script_error.txt"
py.exe "$PSScriptRoot/../b64/imageToB64.py" > "$PSScriptRoot/../b64/image_base64.txt" 2>> "$PSScriptRoot/ps_script_error.txt"