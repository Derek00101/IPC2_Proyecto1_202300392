# Render UML Mermaid to PNG & SVG using Mermaid CLI via npx
# Requires Node.js installed (https://nodejs.org/)

$npx = "npx"
$input = "..\docs\uml.mmd"
$outputPng = "..\docs\uml.png"
$outputSvg = "..\docs\uml.svg"

Write-Host "Rendering Mermaid diagram to PNG and SVG..."
& $npx -y @mermaid-js/mermaid-cli -i $input -o $outputPng
& $npx -y @mermaid-js/mermaid-cli -i $input -o $outputSvg

Write-Host "Done. Files generated:" $outputPng ", " $outputSvg
