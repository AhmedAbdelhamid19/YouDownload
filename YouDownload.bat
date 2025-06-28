@echo off
title YouDownload - YouTube Video Downloader
echo Starting YouDownload...
echo.

cd /d "%~dp0"
cd YouDownload

if exist "dist\YouDownload.exe" (
    echo Launching YouDownload...
    start "" "dist\YouDownload.exe"
) else (
    echo YouDownload.exe not found in dist folder.
    echo Please run the installer first: run_installer.bat
    echo.
    pause
) 