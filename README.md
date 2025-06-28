# YouDownload - Enhanced YouTube Video Downloader

A modern, user-friendly YouTube video and playlist downloader with advanced features including stop/resume functionality, network error protection, and automatic retry mechanisms.

## ✨ New Features in v2.1

### 🛑 Stop and Resume Functionality
- **Stop Download**: Pause downloads at any time with the red "Stop Download" button
- **Resume Download**: Continue downloads from where they left off with the green "Resume Download" button
- **Partial Download Resume**: Automatically resumes interrupted downloads using yt-dlp's built-in resume capability

### 🌐 Network Error Protection
- **Automatic Retry**: Automatically retries failed downloads up to 3 times with 5-second delays
- **Network Detection**: Detects network connectivity issues and provides helpful error messages
- **Connection Testing**: Built-in network test button to verify internet connectivity
- **Smart Error Handling**: Distinguishes between network errors and other issues

### 📊 Enhanced Progress Tracking
- **Download Speed**: Shows real-time download speed in MB/s
- **Dual Progress Bars**: Overall progress for playlists and individual video progress
- **Detailed Status**: Comprehensive status messages with retry attempts and error details
- **Failure Reporting**: Detailed reports for playlist downloads showing which videos failed

## 🚀 Features

### Core Functionality
- **Single Video Download**: Download individual YouTube videos in various qualities
- **Playlist Support**: Download entire playlists or select specific videos
- **Quality Selection**: Choose from multiple video qualities (360p to 1080p)
- **Audio Extraction**: Download audio-only files in MP3 format with embedded album art
- **Thumbnail Support**: View video thumbnails in playlist selection

### User Interface
- **Modern Design**: Clean, professional interface with custom styling
- **Responsive Layout**: Adapts to different window sizes
- **Progress Visualization**: Real-time progress bars and status updates
- **Error Logging**: Detailed error logs for troubleshooting

### Technical Features
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Dependency Management**: Automatic checks for required software (yt-dlp, FFmpeg)
- **Threading**: Non-blocking downloads with background processing
- **Error Recovery**: Robust error handling and recovery mechanisms

## 📋 Requirements

### Software Dependencies
- **Python 3.7+**: Required for running the application
- **yt-dlp**: YouTube downloader library (automatically installed)
- **FFmpeg**: Media processing tool (required for audio extraction and video processing)

### Python Packages
```
yt-dlp>=2023.12.30
Pillow>=9.0.0
requests>=2.25.0
```

## 🛠️ Installation

### Option 1: Quick Install (Recommended)
1. **Download the installer**: Use the provided Windows installer for easy setup
2. **Run installer**: Double-click the installer and follow the wizard
3. **Launch application**: Use the desktop shortcut or start menu entry

### Option 2: Manual Installation
1. **Clone or download** this repository
2. **Install Python dependencies**:
   ```bash
   cd YouDownload
   pip install -r requirements.txt
   ```
3. **Install FFmpeg** (if not already installed):
   ```bash
   # Windows: Download from https://ffmpeg.org/download.html
   # macOS: brew install ffmpeg
   # Linux: sudo apt install ffmpeg
   ```
4. **Run the application**:
   ```bash
   python youtube_downloader_gui.py
   ```

### Option 3: Build Executable
1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. **Build executable**:
   ```bash
   python build_exe.py
   ```
3. **Find the executable** in the `dist` folder

## 🎯 Usage

### Basic Download
1. **Paste YouTube URL**: Enter a video or playlist URL
2. **Select Quality**: Choose your preferred video quality
3. **Choose Location**: Select download folder
4. **Start Download**: Click "Start Download"

### Advanced Features
- **Test URL**: Verify the URL is valid before downloading
- **Test Network**: Check internet connectivity
- **Stop/Resume**: Control download progress
- **Playlist Selection**: Choose specific videos from playlists

### Network Error Handling
- **Automatic Retry**: Downloads automatically retry on network errors
- **Manual Retry**: Use the "Resume Download" button after stopping
- **Error Logs**: Check `error_log.txt` for detailed error information

## 🔧 Troubleshooting

### Common Issues

#### "FFmpeg not found" Error
- **Solution**: Install FFmpeg and add it to your system PATH
- **Windows**: Download from https://ffmpeg.org/download.html
- **macOS**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

#### Network Connection Errors
- **Check Internet**: Use the "Test Network" button
- **Retry Automatically**: The app will retry failed downloads
- **Manual Resume**: Stop and resume downloads if needed

#### Download Failures
- **Check Error Log**: Review `error_log.txt` for details
- **Verify URL**: Ensure the YouTube URL is valid and accessible
- **Try Different Quality**: Some videos may not be available in all qualities

### Error Logs
The application creates detailed error logs in `error_log.txt` for troubleshooting:
- Network connectivity issues
- Download failures
- Processing errors
- Dependency problems

## 🏗️ Development

### Project Structure
```
YouDownload/
├── youtube_downloader_gui.py    # Main application
├── requirements.txt             # Python dependencies
├── build_exe.py                # Executable builder
├── install.py                  # Installation script
├── test_downloader.py          # Test script
└── README.md                   # This file
```

### Building from Source
1. **Clone repository**:
   ```bash
   git clone <repository-url>
   cd YouDownload
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run tests**:
   ```bash
   python test_downloader.py
   ```
4. **Build executable**:
   ```bash
   python build_exe.py
   ```

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Support

For issues, questions, or contributions:
1. Check the troubleshooting section
2. Review error logs
3. Create an issue with detailed information
4. Include system information and error messages

## 🔄 Version History

### v2.1 (Current)
- ✅ Added stop/resume functionality
- ✅ Enhanced network error handling
- ✅ Automatic retry mechanisms
- ✅ Network connectivity testing
- ✅ Download speed display
- ✅ Improved error reporting
- ✅ Partial download resume support

### v2.0
- ✅ Playlist support with video selection
- ✅ Thumbnail display
- ✅ Audio downloads with album art
- ✅ Modern GUI design
- ✅ Progress tracking

### v1.0
- ✅ Basic video downloading
- ✅ Quality selection
- ✅ Simple GUI interface 