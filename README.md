<<<<<<< HEAD
# YouTube Video Downloader

A Python application that downloads YouTube videos to a specified location on your PC.

## Features

- Download YouTube videos in the best available quality
- Specify custom download location
- Support for both pytube and yt-dlp libraries
- Simple configuration with variables in the script

## Requirements

- Python 3.x
- pytube
- yt-dlp

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

## Usage

### Method 1: Using yt-dlp (Recommended)
Edit the variables in `download_youtube_v2.py`:
```python
YOUTUBE_URL = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
DEST_FOLDER = r"C:\Your\Desired\Path"
```

Then run:
```bash
python download_youtube_v2.py
```

### Method 2: Command Line Arguments (Legacy)
```bash
python download_youtube.py <YouTube_URL> <Destination_Folder>
```

## Files

- `download_youtube_v2.py` - Main downloader using yt-dlp (recommended)
- `download_youtube.py` - Legacy downloader using pytube
- `requirements.txt` - Python dependencies
- `README.md` - This file

## Example

```python
# Set your YouTube URL and destination folder here
YOUTUBE_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
DEST_FOLDER = r"C:\Users\YourName\Downloads\Videos"
```

## Troubleshooting

- If you get HTTP 400 errors with pytube, use the yt-dlp version instead
- Make sure you have a stable internet connection
- Some videos may be restricted and cannot be downloaded

## License

This project is open source and available under the MIT License. 
=======
# Youtube-download
download videos from youtube
>>>>>>> bf62f5162fa112e57a67eb6c49c55043649fdecc
