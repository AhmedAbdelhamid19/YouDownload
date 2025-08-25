#!/usr/bin/env python3
"""
Debug launcher for YouDownload
This script provides detailed error information and debugging capabilities
"""

import os
import sys
import traceback
import tkinter as tk
from tkinter import messagebox

def check_environment():
    """Check the Python environment and dependencies"""
    print("=" * 60)
    print("YouDownload Environment Check")
    print("=" * 60)
    
    # Check Python version
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Script location: {os.path.abspath(__file__)}")
    
    # Check if we're running from executable
    if hasattr(sys, '_MEIPASS'):
        print(f"Running from PyInstaller executable: {sys._MEIPASS}")
    else:
        print("Running from source code")
    
    print()

def check_dependencies():
    """Check if all required dependencies are available"""
    print("Checking dependencies...")
    
    dependencies = [
        ('tkinter', 'GUI framework'),
        ('yt_dlp', 'YouTube downloader'),
        ('PIL', 'Image processing'),
        ('requests', 'HTTP requests'),
        ('sv_ttk', 'Modern theme')
    ]
    
    missing = []
    
    for module, description in dependencies:
        try:
            __import__(module)
            print(f"✅ {module} - {description}")
        except ImportError as e:
            print(f"❌ {module} - {description}: {e}")
            missing.append(module)
    
    if missing:
        print(f"\n❌ Missing dependencies: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All dependencies available")
        return True
    
    print()

def check_resources():
    """Check if resource files are accessible"""
    print("Checking resource files...")
    
    resources = [
        ('youtube_downloader_logo.png', 'Application logo'),
        ('youtube_downloader_logo.ico', 'Application icon'),
        ('icons/', 'Icon directory'),
        ('icons/stop_icon.png', 'Stop button icon'),
        ('icons/download_icon.png', 'Download button icon')
    ]
    
    missing_resources = []
    
    for resource, description in resources:
        if os.path.exists(resource):
            print(f"✅ {resource} - {description}")
        else:
            print(f"❌ {resource} - {description}")
            missing_resources.append(resource)
    
    if missing_resources:
        print(f"\n⚠️  Missing resources: {', '.join(missing_resources)}")
        print("The application may not display properly without these files.")
    
    print()

def check_ffmpeg():
    """Check if FFmpeg is available"""
    print("Checking FFmpeg...")
    
    import shutil
    
    # Check multiple possible locations
    ffmpeg_paths = [
        shutil.which("ffmpeg"),
        "ffmpeg.exe",
        os.path.join(os.path.dirname(__file__), "ffmpeg.exe"),
        os.path.join(os.path.dirname(sys.executable), "ffmpeg.exe")
    ]
    
    ffmpeg_found = False
    for path in ffmpeg_paths:
        if path and os.path.exists(path):
            print(f"✅ FFmpeg found at: {path}")
            ffmpeg_found = True
            break
    
    if not ffmpeg_found:
        print("❌ FFmpeg not found")
        print("⚠️  FFmpeg is required for video processing!")
        print("   Download from: https://ffmpeg.org/download.html")
        print("   Place ffmpeg.exe in the same folder as the application")
    
    print()

def launch_application():
    """Launch the main application with error handling"""
    print("Launching YouDownload...")
    print()
    
    try:
        # Import and run the main application
        from youtube_downloader_gui import YouTubeDownloaderGUI, main
        
        print("✅ Application imported successfully")
        print("Starting GUI...")
        
        # Run the main function
        main()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure all dependencies are installed: pip install -r requirements.txt")
        print("2. Check if you're in the correct directory")
        print("3. Verify the youtube_downloader_gui.py file exists")
        
    except Exception as e:
        print(f"❌ Launch error: {e}")
        print("\nFull error details:")
        traceback.print_exc()
        
        # Show error dialog if tkinter is available
        try:
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            messagebox.showerror("Launch Error", f"Failed to launch YouDownload:\n\n{str(e)}\n\nCheck the console for details.")
            root.destroy()
        except:
            pass

def main():
    """Main debug launcher function"""
    try:
        # Run all checks
        check_environment()
        check_dependencies()
        check_resources()
        check_ffmpeg()
        
        print("=" * 60)
        print("Environment check complete!")
        print("=" * 60)
        
        # Ask user if they want to continue
        response = input("\nDo you want to launch the application? (y/n): ").lower().strip()
        
        if response in ['y', 'yes']:
            launch_application()
        else:
            print("Launch cancelled by user.")
            
    except KeyboardInterrupt:
        print("\n\nLaunch cancelled by user.")
    except Exception as e:
        print(f"\n❌ Debug launcher error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
