@echo off
echo ========================================
echo    YouDownload - Installation Wizard
echo ========================================
echo.
echo Starting installation wizard...
echo.

python simple_installer.py

if %errorlevel% neq 0 (
    echo.
    echo Error: Could not run the installer.
    echo Please make sure Python is installed and try again.
    pause
) 