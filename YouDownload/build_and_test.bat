@echo off
echo Building YouDownload executable...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Install required packages
echo Installing required packages...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install packages
    pause
    exit /b 1
)

REM Build the executable
echo.
echo Building executable...
python build_exe.py
if errorlevel 1 (
    echo Error: Build failed
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo.
echo To test the application:
echo 1. Navigate to the dist folder
echo 2. Copy ffmpeg.exe to the same folder as YouDownload.exe
echo 3. Run YouDownload.exe
echo.
echo Note: You need ffmpeg.exe for video processing
echo You can download it from: https://ffmpeg.org/download.html
echo.
pause
