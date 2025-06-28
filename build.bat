@echo off
title YouDownload Builder
echo Building YouDownload executables...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://python.org/downloads/
    pause
    exit /b 1
)

REM Run the build script
python build_exe.py

echo.
echo Build process completed!
echo Check the dist/ folder for the executables.
pause 