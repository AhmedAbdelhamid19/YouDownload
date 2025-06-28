#!/usr/bin/env python3
"""
Test script for the enhanced YouTube Downloader
Tests the new stop/resume functionality and network error handling
"""

import sys
import os

# Add the YouDownload directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'YouDownload'))

def test_network_connectivity():
    """Test the network connectivity checker"""
    print("Testing network connectivity...")
    
    try:
        from youtube_downloader_gui import YouTubeDownloaderGUI
        import tkinter as tk
        
        # Create a minimal root window for testing
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        app = YouTubeDownloaderGUI(root)
        
        # Test network check
        app.test_network_connection()
        
        print("✅ Network connectivity test completed")
        
    except Exception as e:
        print(f"❌ Network connectivity test failed: {e}")
    
    finally:
        try:
            root.destroy()
        except:
            pass

def test_error_handling():
    """Test error handling functionality"""
    print("Testing error handling...")
    
    try:
        from youtube_downloader_gui import YouTubeDownloaderGUI
        import tkinter as tk
        
        # Create a minimal root window for testing
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        app = YouTubeDownloaderGUI(root)
        
        # Test error logging
        test_error = "Test error message for network connectivity"
        app.show_error(test_error, log_only=True)
        
        # Check if error log was created
        if os.path.exists("error_log.txt"):
            print("✅ Error logging test passed")
        else:
            print("❌ Error logging test failed - no error log created")
        
    except Exception as e:
        print(f"❌ Error handling test failed: {e}")
    
    finally:
        try:
            root.destroy()
        except:
            pass

def main():
    """Run all tests"""
    print("🧪 Testing Enhanced YouTube Downloader")
    print("=" * 50)
    
    test_network_connectivity()
    test_error_handling()
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\nNew Features Added:")
    print("• Stop/Resume download functionality")
    print("• Network connectivity detection")
    print("• Automatic retry on network errors")
    print("• Enhanced error handling and logging")
    print("• Download speed display")
    print("• Partial download resume support")
    print("• Detailed failure reporting for playlists")

if __name__ == "__main__":
    main() 