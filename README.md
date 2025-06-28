# YouDownload - YouTube Video Downloader

A modern, user-friendly YouTube video downloader with a beautiful GUI interface.

## 🚀 Quick Start

### For Non-Technical Users (Recommended)

1. **Download and Install:**
   - Download this repository
   - Double-click `run_installer.bat` to start the installation wizard
   - Follow the "Next, Next, Next..." installation process
   - The installer will automatically download FFmpeg and create shortcuts

2. **Launch YouDownload:**
   - **Desktop Shortcut:** Double-click the "YouDownload" icon on your desktop
   - **Start Menu:** Search for "YouDownload" in the Windows Start Menu
   - **Direct Launch:** Double-click `YouDownload.bat` in the project folder

### For Technical Users

1. **Manual Installation:**
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/YouDownload.git
   cd YouDownload
   
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Install FFmpeg (required for video processing)
   # Download from: https://ffmpeg.org/download.html
   # Add to PATH or place in the same directory as the script
   ```

2. **Run the Application:**
   ```bash
   # Option 1: Run directly with Python
   python YouDownload/youtube_downloader_gui.py
   
   # Option 2: Use the batch launcher
   YouDownload.bat
   
   # Option 3: Use the PowerShell launcher
   YouDownload.ps1
   ```

## 📋 Requirements

### For Simple Installation Wizard:
- **Windows 10/11** (64-bit)
- **Python 3.7+** (for the installer)
- **FFmpeg** (for audio/video processing) - [Installation Guide](#ffmpeg-installation)

### For Pre-built Executable:
- **Windows 10/11** (64-bit)
- **FFmpeg** (for audio/video processing) - [Installation Guide](#ffmpeg-installation)

### For Building from Source:
- **Python 3.7+**
- **pip** (Python package manager)
- **FFmpeg** (for audio/video processing)

## 🔧 FFmpeg Installation

FFmpeg is required for audio extraction and video processing.

### Windows Installation:
1. **Download** FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. **Extract** to `C:\ffmpeg`
3. **Add to PATH**:
   - Open System Properties → Environment Variables
   - Add `C:\ffmpeg\bin` to System PATH
4. **Restart** your computer
5. **Test**: Open Command Prompt and type `ffmpeg -version`

### Alternative: Use Chocolatey
```bash
choco install ffmpeg
```

## 🎯 Features

- 🎥 **Multiple Quality Options**: 1080p, 720p, 480p, 360p, Best Quality
- 🎵 **Audio Downloads**: Extract audio as MP3 files
- 🖥️ **Modern GUI**: Clean, intuitive interface
- 📁 **Easy File Management**: Choose download location
- 🔍 **Video Information**: Preview video details before downloading
- ✅ **URL Validation**: Automatic YouTube URL validation
- 📊 **Progress Tracking**: Real-time download progress

## 📖 How to Use

1. **Launch** YouDownload
2. **Paste** a YouTube URL
3. **Click** "Test URL" to see video information
4. **Choose** download location
5. **Select** video quality
6. **Click** "Download Video"

## 🎨 Quality Options

- **Best Quality**: Highest available quality
- **1080p**: Full HD (1920x1080)
- **720p**: HD (1280x720)
- **480p**: Standard definition
- **360p**: Low definition
- **Audio Only (MP3)**: Audio extraction

## 📁 Project Structure

```
YouDownload/
├── YouDownload/
│   ├── youtube_downloader_gui.py    # Main GUI application
│   └── requirements.txt             # Python dependencies
├── dist/
│   └── YouDownload.exe              # Pre-built executable
├── simple_installer.py              # Python installation wizard
├── run_installer.bat                # Simple installer launcher
├── youtube_downloader_logo.png      # App logo
├── youtube_downloader_logo.ico      # App icon
├── LICENSE.txt                      # MIT license
├── requirements.txt                 # Main dependencies
└── README.md                        # Documentation
```

## 🛠️ Troubleshooting

### Common Issues

**"FFmpeg not found"**
- Install FFmpeg and add to PATH
- Restart your computer

**"Download failed"**
- Check your internet connection
- Verify the YouTube URL is valid
- Try a different video quality

**"App won't start"**
- Make sure Python is installed (for source version)
- Install dependencies: `pip install -r requirements.txt`

**"Permission denied"**
- Run as administrator if needed
- Check folder permissions

### Error Logs
If you encounter issues, check the `error_log.txt` file in the app directory for detailed error information.

## 🔄 Building from Source

### Build Executable:
1. **Install build tools**:
   ```bash
   pip install pyinstaller pillow
   ```

2. **Create logo and build**:
   ```bash
   python create_logo.py
   python build_exe.py
   ```

3. **Find executable** in the `dist/` folder

### Run Simple Installer:
1. **Double-click** `run_installer.bat`
2. **Follow** the installation wizard

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## ⚠️ Disclaimer

This tool is for educational purposes. Please respect YouTube's Terms of Service and only download content you have permission to download.

---

**Enjoy downloading your favorite YouTube videos! 🎬**
