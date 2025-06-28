#!/usr/bin/env python3
"""
Create Desktop Shortcut for YouDownload
Creates a desktop shortcut that users can double-click to run the application
"""

import os
import sys
import subprocess
from pathlib import Path

def create_desktop_shortcut():
    """Create a desktop shortcut for the YouDownload application"""
    
    # Get the desktop path
    desktop_path = Path.home() / "Desktop"
    
    # Get the current script directory
    script_dir = Path(__file__).parent.absolute()
    
    # Path to the batch file
    batch_file = script_dir / "YouDownload.bat"
    
    # Create the shortcut content
    shortcut_content = f"""@echo off
cd /d "{script_dir}"
start "" "{batch_file}"
"""
    
    # Create the shortcut file
    shortcut_path = desktop_path / "YouDownload.bat"
    
    try:
        with open(shortcut_path, 'w') as f:
            f.write(shortcut_content)
        
        print(f"✅ Desktop shortcut created: {shortcut_path}")
        print("🚀 You can now double-click 'YouDownload.bat' on your desktop!")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating shortcut: {e}")
        return False

def main():
    """Main function"""
    print("🔧 Creating YouDownload Desktop Shortcut...")
    print("")
    
    if create_desktop_shortcut():
        print("")
        print("🎉 Setup completed successfully!")
        print("📋 Next steps:")
        print("   1. Double-click 'YouDownload.bat' on your desktop")
        print("   2. Or use the batch file in this folder")
        print("   3. The app will install dependencies automatically")
    else:
        print("")
        print("❌ Failed to create shortcut")
        print("💡 You can still run the app by double-clicking 'YouDownload.bat' in this folder")

if __name__ == "__main__":
    main() 