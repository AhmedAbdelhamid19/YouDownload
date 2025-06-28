#!/usr/bin/env python3
"""
YouDownload Launcher
A simple launcher for the YouTube Downloader GUI application
"""

import sys
import os
import subprocess

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import tkinter
        import yt_dlp
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required dependencies"""
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        return False

def run_app():
    """Run the YouTube downloader GUI application"""
    try:
        # Add the YouDownload directory to Python path
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'YouDownload'))
        
        # Import and run the GUI
        from youtube_downloader_gui import main
        main()
        
    except ImportError as e:
        print(f"Error importing application: {e}")
        return False
    except Exception as e:
        print(f"Error running application: {e}")
        return False
    
    return True

def main():
    """Main launcher function"""
    print("🚀 Starting YouDownload...")
    
    # Check if dependencies are installed
    if not check_dependencies():
        print("Installing missing dependencies...")
        if not install_dependencies():
            print("❌ Failed to install dependencies. Please run: pip install -r requirements.txt")
            input("Press Enter to exit...")
            return 1
    
    # Run the application
    if not run_app():
        print("❌ Failed to start the application")
        input("Press Enter to exit...")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 