import subprocess
import sys
import os

def build_exe():
    print("Building YouDownload executables...")
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("PyInstaller found")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build main app
    print("\nBuilding YouDownload.exe...")
    main_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=youtube_downloader_logo.ico",
        "--name=YouDownload",
        "--add-data=YouDownload/youtube_downloader_logo.png;YouDownload",
        "--add-data=youtube_downloader_logo.ico;.",
        "YouDownload/youtube_downloader_gui.py"
    ]
    
    result = subprocess.run(main_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ YouDownload.exe built successfully!")
    else:
        print(f"❌ Error building YouDownload.exe: {result.stderr}")
        return False
    
    # Build installer
    print("\nBuilding YouDownload-Installer.exe...")
    installer_cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--windowed",
        "--icon=youtube_downloader_logo.ico",
        "--name=YouDownload-Installer",
        "--add-data=YouDownload;YouDownload",
        "--add-data=youtube_downloader_logo.ico;.",
        "--add-data=youtube_downloader_logo.png;.",
        "install.py"
    ]
    
    result = subprocess.run(installer_cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ YouDownload-Installer.exe built successfully!")
    else:
        print(f"❌ Error building YouDownload-Installer.exe: {result.stderr}")
        return False
    
    print("\n🎉 Both executables built successfully!")
    print("Files created:")
    print("- dist/YouDownload.exe")
    print("- dist/YouDownload-Installer.exe")
    
    return True

if __name__ == "__main__":
    build_exe() 