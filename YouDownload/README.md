# YouDownload - YouTube Video Downloader

A modern, user-friendly YouTube video and playlist downloader built with Python and tkinter.

## Features

- 🎥 Download individual YouTube videos
- 📚 Download entire playlists with selective video choice
- 🎨 Multiple quality options (1080p, 720p, 480p, 360p, Audio Only)
- 🎯 Resume interrupted downloads
- 🌙 Dark/Light theme support
- 📁 Custom download location
- 🔄 Network error handling with automatic retry
- 📊 Real-time download progress
- 🖼️ Thumbnail previews for playlist videos

## Requirements

- **Python 3.7+**
- **FFmpeg** (required for video processing)
- **Internet connection**

## Installation

### Option 1: Run from Source

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install FFmpeg:
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Ubuntu/Debian)
4. Run the application:
   ```bash
   python youtube_downloader_gui.py
   ```

### Option 2: Build Executable

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Run the build script:
   ```bash
   python build_exe.py
   ```
3. The executable will be created in the `dist/` folder
4. **Important**: Copy `ffmpeg.exe` to the same folder as `YouDownload.exe`

### Option 3: Use Build Script (Windows)

1. Double-click `build_and_test.bat`
2. Follow the on-screen instructions
3. Copy `ffmpeg.exe` to the `dist/` folder

## Usage

1. **Launch the application**
2. **Enter YouTube URL**: Paste a YouTube video or playlist URL
3. **Test URL**: Click "Test URL" to verify and load video information
4. **Select Quality**: Choose your preferred video quality
5. **Choose Location**: Select where to save downloaded files
6. **Download**: Click "Start Download" to begin

### For Playlists

- Use "Select All" to download all videos
- Use "Deselect All" to clear selection
- Check individual videos you want to download
- Click thumbnails to preview video thumbnails

## Troubleshooting

### Common Issues

#### 1. "Please select at least one video to download" Error

**Cause**: This happens when the application can't properly detect video selection.

**Solution**: 
- Make sure you've clicked "Test URL" first
- For single videos, the error shouldn't occur
- For playlists, ensure at least one video is checked

#### 2. Application Won't Start or Shows Blank Screen

**Cause**: Missing dependencies or resource files.

**Solution**:
- Run `python test_app.py` to check dependencies
- Ensure all required packages are installed
- Check if `ffmpeg.exe` is in the same folder as the executable

#### 3. Icons Not Displaying

**Cause**: Icon files not found or path issues.

**Solution**:
- Ensure the `icons/` folder is in the same directory as the executable
- Check if icon files exist: `stop_icon.png`, `resume_icon.png`, etc.
- The application will fall back to text-based buttons if icons fail to load

#### 4. Download Fails with Network Errors

**Cause**: Internet connection issues or YouTube restrictions.

**Solution**:
- Check your internet connection
- Try using a VPN if YouTube is blocked in your region
- Wait a few minutes and try again
- Check if the video is available in your country

#### 5. FFmpeg Not Found Error

**Cause**: FFmpeg is not installed or not in PATH.

**Solution**:
- Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
- Extract and place `ffmpeg.exe` in the same folder as `YouDownload.exe`
- Or add FFmpeg to your system PATH

### Testing Your Installation

Run the test script to verify everything is working:

```bash
python test_app.py
```

This will check:
- ✅ Module imports
- ✅ Resource file paths
- ✅ yt-dlp functionality
- ✅ PIL image processing

### Debug Mode

If you're experiencing issues, the application logs errors to `error_log.txt`. Check this file for detailed error information.

## File Structure

```
YouDownload/
├── youtube_downloader_gui.py    # Main application
├── requirements.txt             # Python dependencies
├── build_exe.py                # Executable builder
├── build_and_test.bat          # Windows build script
├── test_app.py                 # Testing script
├── icons/                      # Button icons
│   ├── download_icon.png
│   ├── stop_icon.png
│   ├── resume_icon.png
│   └── network_icon.png
├── youtube_downloader_logo.png # Application logo
└── README.md                   # This file
```

## Building from Source

### Prerequisites

- Python 3.7+
- pip
- PyInstaller

### Build Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Build executable
python build_exe.py

# Or use the Windows batch file
build_and_test.bat
```

### Build Options

The build script creates a single-file executable with:
- All dependencies bundled
- Icons and resources included
- Windows-compatible format
- No console window (--windowed)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use, modify, and distribute.

## Support

If you encounter issues:

1. Check this README for troubleshooting steps
2. Run `python test_app.py` to diagnose problems
3. Check the `error_log.txt` file for error details
4. Ensure FFmpeg is properly installed
5. Verify all dependencies are installed

## Version History

- **v2.1**: Enhanced error handling, improved playlist support, better resource management
- **v2.0**: Added playlist support, improved UI, better error handling
- **v1.0**: Initial release with basic video download functionality

---

**Note**: This application is for personal use only. Please respect YouTube's terms of service and copyright laws.
