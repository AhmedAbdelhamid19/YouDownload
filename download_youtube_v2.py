import os
import yt_dlp

# Set your YouTube URL and destination folder here
YOUTUBE_URL = "https://www.youtube.com/watch?v=vI4GdN5wBTQ&ab_channel=NetNinja"  # Change this to your desired video
DEST_FOLDER = r"C:\Users\AM\Desktop\YouDownload\TestDownload"  # Change this to your desired folder

def main():
    url = YOUTUBE_URL
    dest_folder = DEST_FOLDER
    
    print(f"Attempting to download from: {url}")
    print(f"Destination folder: {dest_folder}")
    
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created directory: {dest_folder}")
    
    # Configure yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(dest_folder, '%(title)s.%(ext)s'),
        'format': 'best',  # Download best quality
        'verbose': True,   # Show detailed output
    }
    
    try:
        print("Starting download with yt-dlp...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            info = ydl.extract_info(url, download=False)
            print(f"Video title: {info.get('title', 'Unknown')}")
            print(f"Video duration: {info.get('duration', 'Unknown')} seconds")
            
            # Download the video
            ydl.download([url])
        
        print(f"Successfully downloaded to {dest_folder}")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print(f"Error type: {type(e).__name__}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 