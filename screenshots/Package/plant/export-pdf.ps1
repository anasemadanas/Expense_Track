param(
  [string]$PlantUmlJar = (Join-Path $PSScriptRoot "plantuml.jar"),
  [string]$ChromePath = "",
  [string]$SvgOutDir = (Join-Path $PSScriptRoot "out\\svg"),
  [string]$PdfOutDir = (Join-Path $PSScriptRoot "out\\pdf"),
  [string[]]$InputFiles = @()
)

$ErrorActionPreference = "Stop"

function Resolve-ChromePath {
  param([string]$ExplicitPath)

  if ($ExplicitPath) {
    if (Test-Path -LiteralPath $ExplicitPath) { return $ExplicitPath }
    throw "Chrome not found at: $ExplicitPath"
  }

  $candidates = @(
    (Join-Path $env:ProgramFiles "Google\\Chrome\\Application\\chrome.exe"),
    (Join-Path ${env:ProgramFiles(x86)} "Google\\Chrome\\Application\\chrome.exe"),
    (Join-Path $env:LocalAppData "Google\\Chrome\\Application\\chrome.exe")
  ) | Where-Object { $_ -and (Test-Path -LiteralPath $_) }

  if ($candidates.Count -gt 0) { return $candidates[0] }
  throw "Chrome not found. Install Google Chrome or pass -ChromePath."
}

if (-not (Test-Path -LiteralPath $PlantUmlJar)) {
  throw "PlantUML jar not found: $PlantUmlJar"
}

if ($InputFiles.Count -eq 0) {
  $InputFiles = @(Get-ChildItem -LiteralPath $PSScriptRoot -File -Filter *.puml | ForEach-Object FullName)
}
if ($InputFiles.Count -eq 0) {
  throw "No .puml files found in: $PSScriptRoot"
}

$ChromePath = Resolve-ChromePath -ExplicitPath $ChromePath

New-Item -ItemType Directory -Force -Path $SvgOutDir | Out-Null
New-Item -ItemType Directory -Force -Path $PdfOutDir | Out-Null
$chromeUserDataDir = Join-Path $PSScriptRoot "out\\chrome-profile"
New-Item -ItemType Directory -Force -Path $chromeUserDataDir | Out-Null

# 1) Generate SVGs (PlantUML PDF export needs extra deps; SVG is always supported)
& java -jar $PlantUmlJar -tsvg -o $SvgOutDir @InputFiles | Out-Null

# 2) Wrap each SVG in a tiny HTML file and let Chrome print it to PDF
$svgFiles = Get-ChildItem -LiteralPath $SvgOutDir -File -Filter *.svg
foreach ($svgFile in $svgFiles) {
  $svg = Get-Content -LiteralPath $svgFile.FullName -Raw

  $html = @"
<!doctype html>
<html>
  <head>
    <meta charset="utf-8" />
    <style>
      @page { margin: 0; }
      html, body { margin: 0; padding: 0; background: #fff; }
      svg { display: block; width: 100vw; height: auto; }
    </style>
  </head>
  <body>
    $svg
  </body>
</html>
"@

  $htmlPath = Join-Path $SvgOutDir ($svgFile.BaseName + ".html")
  Set-Content -LiteralPath $htmlPath -Value $html -Encoding UTF8

  $pdfPath = Join-Path $PdfOutDir ($svgFile.BaseName + ".pdf")
  $chromeArgs = @(
    "--headless",
    "--disable-gpu",
    "--no-first-run",
    "--no-default-browser-check",
    "--user-data-dir=$chromeUserDataDir",
    "--print-to-pdf=$pdfPath",
    $htmlPath
  )
  Start-Process -FilePath $ChromePath -ArgumentList $chromeArgs -NoNewWindow -Wait | Out-Null
}

Write-Host ("Generated {0} PDF(s) in: {1}" -f $svgFiles.Count, $PdfOutDir)
