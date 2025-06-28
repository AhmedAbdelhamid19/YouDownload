# YouDownload PowerShell Launcher
# YouTube Video Downloader Desktop Application

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   YouDownload - YouTube Downloader" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Starting application..." -ForegroundColor Yellow
Write-Host ""

# Run the launcher
try {
    python launcher.py
} catch {
    Write-Host "❌ Error running application: $_" -ForegroundColor Red
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
} 