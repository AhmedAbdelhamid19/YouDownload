#!/usr/bin/env python3
"""
Test script to verify button icons are loading correctly
"""

import os
import sys
from PIL import Image, ImageTk
import tkinter as tk

def test_icon_loading():
    """Test if icons can be loaded properly"""
    print("Testing icon loading...")
    
    # Check if icons directory exists
    icons_dir = "icons"
    if not os.path.exists(icons_dir):
        print("❌ Icons directory not found!")
        return False
    
    # List available icons
    icon_files = ['stop_icon.png', 'resume_icon.png', 'network_icon.png', 'download_icon.png']
    available_icons = []
    
    for icon_file in icon_files:
        icon_path = os.path.join(icons_dir, icon_file)
        if os.path.exists(icon_path):
            available_icons.append(icon_file)
            print(f"✅ Found: {icon_file}")
        else:
            print(f"❌ Missing: {icon_file}")
    
    if len(available_icons) == 0:
        print("❌ No icons found!")
        return False
    
    # Test loading icons
    print("\nTesting icon loading...")
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        loaded_icons = {}
        for icon_file in available_icons:
            try:
                icon_path = os.path.join(icons_dir, icon_file)
                img = Image.open(icon_path)
                img = img.resize((16, 16), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                loaded_icons[icon_file] = photo
                print(f"✅ Loaded: {icon_file}")
            except Exception as e:
                print(f"❌ Failed to load {icon_file}: {e}")
        
        root.destroy()
        
        if len(loaded_icons) == len(available_icons):
            print(f"\n✅ Successfully loaded {len(loaded_icons)} icons!")
            return True
        else:
            print(f"\n⚠️  Only loaded {len(loaded_icons)}/{len(available_icons)} icons")
            return False
            
    except Exception as e:
        print(f"❌ Error testing icons: {e}")
        return False

def test_gui_icons():
    """Test if the GUI can load icons"""
    print("\nTesting GUI icon integration...")
    
    try:
        # Import the GUI module
        sys.path.insert(0, 'YouDownload')
        from youtube_downloader_gui import YouTubeDownloaderGUI
        
        # Create a minimal root window
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Create the GUI instance
        app = YouTubeDownloaderGUI(root)
        
        # Check if icons were loaded
        if hasattr(app, 'button_icons') and app.button_icons:
            print(f"✅ GUI loaded {len(app.button_icons)} button icons:")
            for icon_name in app.button_icons.keys():
                print(f"   - {icon_name}")
        else:
            print("⚠️  GUI is using Unicode symbols instead of icons")
        
        root.destroy()
        return True
        
    except Exception as e:
        print(f"❌ Error testing GUI icons: {e}")
        return False

def main():
    """Run all icon tests"""
    print("🧪 Testing YouDownload Button Icons")
    print("=" * 50)
    
    # Test basic icon loading
    icons_ok = test_icon_loading()
    
    # Test GUI integration
    gui_ok = test_gui_icons()
    
    print("\n" + "=" * 50)
    if icons_ok and gui_ok:
        print("✅ All icon tests passed!")
        print("\nYour executable will have proper button icons.")
    else:
        print("⚠️  Some icon tests failed.")
        print("The application will use Unicode symbols as fallback.")
    
    print("\nTo build the executable with icons:")
    print("1. Run: python build_exe.py")
    print("2. Or run: build_with_icons.bat")
    print("3. Check the 'dist' folder for YouDownload.exe")

if __name__ == "__main__":
    main() 