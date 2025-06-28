# YouDownload - YouTube Video Downloader Desktop App

A simple and user-friendly desktop application for downloading YouTube videos with a graphical interface.

## 🚀 Quick Start

### Option 1: Run with Python (Recommended)
1. **Double-click** `YouDownload.bat` (Windows) or run `python launcher.py`
2. The application will automatically install dependencies if needed
3. Enjoy downloading YouTube videos!

### Option 2: Build Executable
1. Run `python build_exe.py`
2. Find your executable in the `dist` folder
3. Double-click `YouDownload.exe` to run

## 📋 Requirements

- Python 3.7 or higher
- Internet connection
- Windows 10/11 (for .bat file)

## 🛠️ Installation

### Automatic Installation
The launcher will automatically install required packages when you first run it.

### Manual Installation
```bash
pip install -r requirements.txt
```

## 🎯 Features

- **User-friendly GUI**: Simple and intuitive interface
- **Multiple Quality Options**: Choose from various video qualities
- **Audio Extraction**: Download audio-only as MP3
- **Progress Tracking**: Real-time download progress
- **Video Information**: Preview video details before downloading
- **Custom Download Location**: Choose where to save your files

## 📖 How to Use

1. **Launch the Application**
   - Double-click `YouDownload.bat` (Windows)
   - Or run `python launcher.py`

2. **Enter YouTube URL**
   - Paste any YouTube video URL
   - Click "Test URL" to verify and get video info

3. **Choose Download Location**
   - Click "Browse" to select where to save files
   - Default location: Downloads folder

4. **Select Quality**
   - Choose from available quality options
   - "Best Quality" for highest available
   - "Audio Only (MP3)" for audio extraction

5. **Download**
   - Click "Download Video"
   - Watch the progress bar
   - Files will be saved to your chosen location

## 🔧 Troubleshooting

### Common Issues

**Python not found:**
- Install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

**Dependencies missing:**
- Run `pip install -r requirements.txt`
- Or let the launcher install them automatically

**Download fails:**
- Check your internet connection
- Verify the YouTube URL is valid
- Try a different video quality

**Permission errors:**
- Run as administrator if needed
- Check folder permissions

## 📁 File Structure

```
YouDownload/
├── YouDownload.bat          # Windows launcher
├── YouDownload.ps1          # PowerShell launcher
├── launcher.py              # Python launcher
├── build_exe.py             # Executable builder
├── requirements.txt         # Dependencies
├── README.md               # This file
└── YouDownload/            # Main application
    ├── youtube_downloader_gui.py
    ├── requirements.txt
    └── README.md
```

## 🎨 Screenshots

The application features a clean, modern interface with:
- URL input field with validation
- Download location selector
- Quality selection dropdown
- Video information display
- Progress bar with status updates
- Error handling and user feedback

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

**Enjoy downloading your favorite YouTube videos! 🎬**
