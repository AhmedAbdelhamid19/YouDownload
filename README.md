# YouDownload - YouTube Video Downloader

A simple and modern GUI application for downloading YouTube videos and playlists.

## Features

- Download single videos or entire playlists
- Multiple quality options (1080p, 720p, 480p, 360p, Best Quality)
- Audio-only downloads with embedded album art
- Video selection for playlists with thumbnails
- Modern, user-friendly interface
- Progress tracking with file size information

## Quick Start

### Prerequisites

1. **Python 3.7 or higher** - Download from [python.org](https://www.python.org/downloads/)
2. **FFmpeg** - Required for video processing and audio conversion

### Installation Steps

1. **Download the project**
   ```bash
   git clone https://github.com/yourusername/YouDownload.git
   cd YouDownload
   ```

2. **Install Python dependencies**
   ```bash
   cd YouDownload
   pip install -r requirements.txt
   ```

3. **Install FFmpeg** (if not already installed)
   
   **Windows:**
   - Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - Extract to a folder (e.g., `C:\ffmpeg`)
   - Add to PATH: Add `C:\ffmpeg\bin` to your system PATH environment variable
   
   **Alternative (Windows):**
   - Use Chocolatey: `choco install ffmpeg`
   - Use Winget: `winget install ffmpeg`

   **macOS:**
   ```bash
   brew install ffmpeg
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

4. **Run the application**
   ```bash
   python youtube_downloader_gui.py
   ```

## How to Use

1. **Enter a YouTube URL** - Paste any YouTube video or playlist URL
2. **Click "Test URL"** - This will fetch video information and show available options
3. **Select quality** - Choose from the dropdown menu
4. **Choose download location** - Click "Browse" to select where to save files
5. **For playlists** - Select which videos you want to download
6. **Click "Download"** - Start the download process

## Audio Downloads

When selecting "Audio Only (MP3)", the app will:
- Download the best available audio
- Convert to MP3 format
- Embed the video thumbnail as album art
- Add metadata (title, artist, etc.)

## Troubleshooting

**"yt-dlp is not installed"**
```bash
pip install yt-dlp
```

**"FFmpeg is not installed"**
- Follow the FFmpeg installation steps above
- Restart your terminal/command prompt after adding to PATH

**Download fails**
- Check your internet connection
- Ensure the YouTube URL is valid
- Try a different video (some may have restrictions)

## Requirements

- Python 3.7+
- yt-dlp
- Pillow (PIL)
- requests
- FFmpeg

## License

This project is open source. Feel free to use and modify as needed. 