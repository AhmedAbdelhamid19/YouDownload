@echo off
echo Installing FFmpeg for YouTube Downloader...
echo.
echo This will download and install FFmpeg automatically.
echo You may be prompted for administrator permissions.
echo.
pause

:: Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Running as administrator...
) else (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~dpnx0' -Verb RunAs"
    exit /b
)

:: Change to the script directory
cd /d "%~dp0"

:: Run the Python script
echo.
echo Starting FFmpeg installation...
python install_ffmpeg_windows.py

echo.
echo Installation complete!
echo Please restart your computer for changes to take effect.
echo.
pause 