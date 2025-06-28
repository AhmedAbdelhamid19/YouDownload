import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import yt_dlp
from urllib.parse import urlparse

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Variables
        self.download_path = tk.StringVar()
        self.youtube_url = tk.StringVar()
        self.selected_quality = tk.StringVar()
        self.download_progress = tk.DoubleVar()
        self.status_text = tk.StringVar(value="Ready to download")
        
        # Available qualities
        self.qualities = [
            "Best Quality",
            "1080p",
            "720p", 
            "480p",
            "360p",
            "Audio Only (MP3)"
        ]
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="YouTube Video Downloader", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # YouTube URL Section
        url_frame = ttk.LabelFrame(main_frame, text="YouTube Video URL", padding="10")
        url_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        url_frame.columnconfigure(0, weight=1)
        
        ttk.Label(url_frame, text="Paste YouTube URL:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        url_entry = ttk.Entry(url_frame, textvariable=self.youtube_url, width=60)
        url_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        # Test URL button
        test_btn = ttk.Button(url_frame, text="Test URL", command=self.test_url)
        test_btn.grid(row=1, column=1, padx=(10, 0))
        
        # Download Location Section
        location_frame = ttk.LabelFrame(main_frame, text="Download Location", padding="10")
        location_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        location_frame.columnconfigure(0, weight=1)
        
        ttk.Label(location_frame, text="Choose download folder:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        location_entry = ttk.Entry(location_frame, textvariable=self.download_path, width=50)
        location_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        browse_btn = ttk.Button(location_frame, text="Browse", command=self.browse_location)
        browse_btn.grid(row=1, column=1, padx=(10, 0))
        
        # Quality Selection Section
        quality_frame = ttk.LabelFrame(main_frame, text="Video Quality", padding="10")
        quality_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(quality_frame, text="Select quality:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        quality_combo = ttk.Combobox(quality_frame, textvariable=self.selected_quality, 
                                    values=self.qualities, state="readonly", width=30)
        quality_combo.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        quality_combo.set("Best Quality")  # Default selection
        
        # Video Info Section
        self.info_frame = ttk.LabelFrame(main_frame, text="Video Information", padding="10")
        self.info_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        self.info_frame.columnconfigure(0, weight=1)
        
        self.info_text = tk.Text(self.info_frame, height=6, width=70, wrap=tk.WORD, state=tk.DISABLED)
        self.info_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Progress Section
        progress_frame = ttk.LabelFrame(main_frame, text="Download Progress", padding="10")
        progress_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.download_progress, 
                                           maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.status_label = ttk.Label(progress_frame, textvariable=self.status_text)
        self.status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Download Button
        self.download_btn = ttk.Button(main_frame, text="Download Video", 
                                      command=self.start_download, style="Accent.TButton")
        self.download_btn.grid(row=6, column=0, columnspan=3, pady=(10, 0))
        
        # Set default download path
        self.download_path.set(os.path.expanduser("~/Downloads"))
        
    def browse_location(self):
        """Open file dialog to select download location"""
        folder = filedialog.askdirectory(title="Select Download Folder")
        if folder:
            self.download_path.set(folder)
            
    def test_url(self):
        """Test if the YouTube URL is valid and get video info"""
        url = self.youtube_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        if not self.is_valid_youtube_url(url):
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return
            
        self.status_text.set("Fetching video information...")
        self.download_btn.config(state="disabled")
        
        # Run in separate thread to avoid blocking GUI
        thread = threading.Thread(target=self.fetch_video_info, args=(url,))
        thread.daemon = True
        thread.start()
        
    def is_valid_youtube_url(self, url):
        """Check if URL is a valid YouTube URL"""
        try:
            parsed = urlparse(url)
            return 'youtube.com' in parsed.netloc or 'youtu.be' in parsed.netloc
        except:
            return False
            
    def fetch_video_info(self, url):
        """Fetch video information from YouTube"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Update GUI in main thread
                self.root.after(0, self.update_video_info, info)
                
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"Error fetching video info: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.download_btn.config(state="normal"))
            
    def update_video_info(self, info):
        """Update the video information display"""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete(1.0, tk.END)
        
        info_text = f"Title: {info.get('title', 'Unknown')}\n"
        info_text += f"Duration: {self.format_duration(info.get('duration', 0))}\n"
        info_text += f"Uploader: {info.get('uploader', 'Unknown')}\n"
        info_text += f"Views: {info.get('view_count', 'Unknown'):,}\n"
        info_text += f"Upload Date: {info.get('upload_date', 'Unknown')}\n"
        
        # Get available formats
        formats = info.get('formats', [])
        if formats:
            info_text += f"\nAvailable formats: {len(formats)}"
            
        self.info_text.insert(tk.END, info_text)
        self.info_text.config(state=tk.DISABLED)
        
        self.status_text.set("Video information loaded successfully")
        
    def format_duration(self, seconds):
        """Format duration in seconds to HH:MM:SS"""
        if not seconds:
            return "Unknown"
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
            
    def start_download(self):
        """Start the download process"""
        url = self.youtube_url.get().strip()
        download_path = self.download_path.get().strip()
        quality = self.selected_quality.get()
        
        # Validation
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        if not download_path:
            messagebox.showerror("Error", "Please select a download location")
            return
            
        if not os.path.exists(download_path):
            try:
                os.makedirs(download_path)
            except Exception as e:
                messagebox.showerror("Error", f"Cannot create download directory: {str(e)}")
                return
                
        if not self.is_valid_youtube_url(url):
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return
            
        # Disable download button
        self.download_btn.config(state="disabled")
        self.status_text.set("Starting download...")
        self.download_progress.set(0)
        
        # Run download in separate thread
        thread = threading.Thread(target=self.download_video, args=(url, download_path, quality))
        thread.daemon = True
        thread.start()
        
    def download_video(self, url, download_path, quality):
        """Download the video in a separate thread"""
        try:
            # Configure yt-dlp options based on quality selection
            ydl_opts = {
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
                'progress_hooks': [self.progress_hook],
            }
            
            if quality == "Audio Only (MP3)":
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                })
            elif quality == "Best Quality":
                ydl_opts['format'] = 'best'
            else:
                # Extract resolution number (e.g., "1080p" -> "1080")
                resolution = quality.replace('p', '')
                ydl_opts['format'] = f'best[height<={resolution}]'
                
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                
            # Download completed
            self.root.after(0, self.download_completed)
            
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"Download failed: {str(e)}"))
        finally:
            self.root.after(0, lambda: self.download_btn.config(state="normal"))
            
    def progress_hook(self, d):
        """Progress hook for yt-dlp"""
        if d['status'] == 'downloading':
            # Update progress bar
            if 'total_bytes' in d and d['total_bytes']:
                progress = (d['downloaded_bytes'] / d['total_bytes']) * 100
                self.root.after(0, lambda: self.download_progress.set(progress))
                
            # Update status
            if '_percent_str' in d:
                self.root.after(0, lambda: self.status_text.set(f"Downloading: {d['_percent_str']}"))
                
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.status_text.set("Processing video..."))
            
    def download_completed(self):
        """Called when download is completed"""
        self.download_progress.set(100)
        self.status_text.set("Download completed successfully!")
        messagebox.showinfo("Success", "Video downloaded successfully!")
        
    def show_error(self, message):
        """Show error message"""
        self.status_text.set("Error occurred")
        messagebox.showerror("Error", message)

def main():
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 