@echo off
title YouDownload Installer
echo Starting YouDownload Installer...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM Run the installer
python install.py

echo.
echo Installation completed!
pause 