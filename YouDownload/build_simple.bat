@echo off
echo Building YouDownload...
echo.

REM Install PyInstaller if not present
pip install pyinstaller

REM Build the executable
pyinstaller --onefile --windowed --icon=youtube_downloader_logo.ico --name=YouDownload --add-data=youtube_downloader_logo.png;. --add-data=icons;icons youtube_downloader_gui.py

echo.
echo Build complete! Check the dist folder for YouDownload.exe
echo.
echo IMPORTANT: Copy ffmpeg.exe to the same folder as YouDownload.exe
echo.
pause
