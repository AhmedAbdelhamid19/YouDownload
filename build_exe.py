import os
import subprocess
import sys

def install_requirements():
    """Install required packages for building the executable"""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")
    
    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",  # Create a single executable file
        "--windowed",  # Don't show console window
        "--name=YouDownload",  # Name of the executable
        "--icon=icon.ico",  # Icon file (if exists)
        "--add-data=requirements.txt;.",  # Include requirements file
        "YouDownload/youtube_downloader_gui.py"
    ]
    
    # Remove icon parameter if icon doesn't exist
    if not os.path.exists("icon.ico"):
        cmd.remove("--icon=icon.ico")
    
    subprocess.check_call(cmd)
    print("Executable built successfully!")

def main():
    try:
        install_requirements()
        build_executable()
        print("\n✅ Build completed successfully!")
        print("📁 Your executable is located in the 'dist' folder")
        print("🚀 You can now run 'YouDownload.exe' by double-clicking it")
        
    except Exception as e:
        print(f"❌ Error during build: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 