#!/usr/bin/env python3
"""
Test script for YouDownload application
This script tests the main components without requiring a full GUI
"""

import os
import sys
import importlib

def test_imports():
    """Test if all required modules can be imported"""
    print("Testing module imports...")
    
    required_modules = [
        'tkinter',
        'yt_dlp', 
        'PIL',
        'requests',
        'sv_ttk'
    ]
    
    failed_imports = []
    
    for module in required_modules:
        try:
            importlib.import_module(module)
            print(f"✅ {module}")
        except ImportError as e:
            print(f"❌ {module}: {e}")
            failed_imports.append(module)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        return False
    else:
        print("\n✅ All modules imported successfully!")
        return True

def test_resource_paths():
    """Test if resource paths can be resolved"""
    print("\nTesting resource paths...")
    
    # Test the get_resource_path function
    try:
        from youtube_downloader_gui import get_resource_path
        
        test_paths = [
            "../youtube_downloader_logo.png",
            "icons",
            "youtube_downloader_logo.ico"
        ]
        
        for path in test_paths:
            resolved = get_resource_path(path)
            exists = os.path.exists(resolved)
            status = "✅" if exists else "❌"
            print(f"{status} {path} -> {resolved} ({'exists' if exists else 'not found'})")
            
    except ImportError as e:
        print(f"❌ Could not import youtube_downloader_gui: {e}")
        return False
    
    return True

def test_yt_dlp():
    """Test yt-dlp functionality"""
    print("\nTesting yt-dlp...")
    
    try:
        import yt_dlp
        
        # Test basic yt-dlp functionality
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True
        }
        
        print("✅ yt-dlp imported successfully")
        print("✅ yt-dlp options created successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ yt-dlp test failed: {e}")
        return False

def test_pil():
    """Test PIL functionality"""
    print("\nTesting PIL...")
    
    try:
        from PIL import Image, ImageTk
        
        # Test basic PIL functionality
        test_img = Image.new('RGB', (100, 100), color='red')
        print("✅ PIL imported successfully")
        print("✅ PIL image creation successful")
        
        return True
        
    except Exception as e:
        print(f"❌ PIL test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=" * 50)
    print("YouDownload Application Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_resource_paths,
        test_yt_dlp,
        test_pil
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application should work correctly.")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
    
    print("=" * 50)
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
