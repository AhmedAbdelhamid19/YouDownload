@echo off
title YouDownload - YouTube Video Downloader
echo.
echo ========================================
echo    YouDownload - YouTube Downloader
echo ========================================
echo.
echo Starting application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

REM Run the launcher
python launcher.py

REM If there was an error, pause so user can see the message
if errorlevel 1 (
    echo.
    echo Application exited with an error.
    pause
) 