# YouDownload Launcher
# This script launches YouDownload with proper icon and window title

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "    YouDownload - YouTube Downloader" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptPath

# Check if executable exists
$exePath = "YouDownload\dist\YouDownload.exe"
if (Test-Path $exePath) {
    Write-Host "Launching YouDownload..." -ForegroundColor Green
    
    # Launch the application
    Start-Process -FilePath $exePath -WindowStyle Normal
    
    Write-Host "YouDownload is starting..." -ForegroundColor Yellow
} else {
    Write-Host "YouDownload.exe not found!" -ForegroundColor Red
    Write-Host "Please run the installer first: run_installer.bat" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
} 