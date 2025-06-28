@echo off
echo Building YouDownload with icons...
echo.

REM Create icons first
echo Creating button icons...
python create_button_icons.py
if errorlevel 1 (
    echo Error creating icons!
    pause
    exit /b 1
)

echo.
echo Building executable...
python build_exe.py
if errorlevel 1 (
    echo Error building executable!
    pause
    exit /b 1
)

echo.
echo Build completed successfully!
echo Check the 'dist' folder for your executables.
pause 