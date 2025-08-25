import subprocess
import sys
import os

def build_exe():
    print("Building YouDownload executable...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("PyInstaller found")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build main app with proper dependencies and data files
    print("\nBuilding YouDownload.exe...")
    main_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=youtube_downloader_logo.ico",
        "--name=YouDownload",
        "--add-data=youtube_downloader_logo.png;.",
        "--add-data=youtube_downloader_logo.ico;.",
        "--add-data=icons;icons",
        "--hidden-import=PIL._tkinter_finder",
        "--hidden-import=tkinter",
        "--hidden-import=tkinter.ttk",
        "--hidden-import=yt_dlp",
        "--hidden-import=sv_ttk",
        "--hidden-import=requests",
        "--hidden-import=PIL",
        "--hidden-import=PIL.Image",
        "--hidden-import=PIL.ImageTk",
        "--collect-all=yt_dlp",
        "--collect-all=sv_ttk",
        "--collect-all=PIL",
        "YouDownload/youtube_downloader_gui.py"
    ]
    
    result = subprocess.run(main_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ YouDownload.exe built successfully!")
    else:
        print(f"❌ Error building YouDownload.exe: {result.stderr}")
        return False
    
    print("\n🎉 YouDownload.exe built successfully!")
    print("File created: dist/YouDownload.exe")
    print("\nNote: Make sure ffmpeg is installed on the target system or included in the same folder.")
    
    return True

if __name__ == "__main__":
    build_exe()
