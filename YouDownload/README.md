# YouTube Video Downloader

A Python application that downloads YouTube videos to a specified location on your PC. Available in both GUI and command-line versions.

## Features

- **GUI Interface**: Modern, user-friendly interface with drag-and-drop functionality
- **Multiple Quality Options**: Choose from various video qualities (1080p, 720p, 480p, 360p) or audio-only MP3
- **File Browser**: Easy selection of download location
- **Progress Tracking**: Real-time download progress with percentage
- **Video Information**: Preview video details before downloading
- **URL Validation**: Automatic YouTube URL validation
- **Cross-platform**: Works on Windows, macOS, and Linux

## Requirements

- Python 3.x
- pytube
- yt-dlp
- ffmpeg-python (for audio processing)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/AhmedAbdelhamid19/Youtube-download.git
cd Youtube-download
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Install FFmpeg for audio processing:
   - **Windows**: Download from https://ffmpeg.org/download.html
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

## Usage

### GUI Version (Recommended)
Run the graphical interface:
```bash
python youtube_downloader_gui.py
```

**Features:**
- Paste YouTube URL in the text field
- Click "Test URL" to validate and get video information
- Choose download location using the "Browse" button
- Select video quality from the dropdown menu
- Click "Download Video" to start downloading
- Monitor progress with the progress bar

### Command Line Version
Edit the variables in `download_youtube_v2.py`:
```python
YOUTUBE_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
DEST_FOLDER = r"C:\Your\Desired\Path"
```

Then run:
```bash
python download_youtube_v2.py
```

### Legacy Version
```bash
python download_youtube.py <YouTube_URL> <Destination_Folder>
```

## Files

- `youtube_downloader_gui.py` - **Main GUI application** (recommended)
- `download_youtube_v2.py` - Command-line version using yt-dlp
- `download_youtube.py` - Legacy command-line version using pytube
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Quality Options

- **Best Quality**: Downloads the highest available quality
- **1080p**: Full HD video
- **720p**: HD video
- **480p**: Standard definition
- **360p**: Low definition
- **Audio Only (MP3)**: Extracts audio and converts to MP3

## Example Usage

1. **GUI Version:**
   - Launch the application
   - Paste: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
   - Click "Test URL" to see video info
   - Choose your download folder
   - Select "720p" quality
   - Click "Download Video"

2. **Command Line:**
   ```python
   YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
   DEST_FOLDER = r"C:\Users\YourName\Downloads\Videos"
   ```

## Troubleshooting

- **HTTP 400 errors**: Use the yt-dlp version instead of pytube
- **Audio conversion fails**: Install FFmpeg
- **GUI not responding**: Check your internet connection
- **Permission errors**: Run as administrator or change download location

## Screenshots

The GUI includes:
- URL input field with validation
- File browser for download location
- Quality selection dropdown
- Video information display
- Progress bar with status updates
- Error handling with user-friendly messages

## License

This project is open source and available under the MIT License. 