import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import os
import yt_dlp
from urllib.parse import urlparse
import traceback
import shutil
from PIL import Image, ImageTk
import requests
from io import BytesIO

APP_VERSION = "v2.0"  # Update as needed

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        self.root.configure(bg="#f7fafd")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#f7fafd")
        style.configure("TLabel", background="#f7fafd", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("Accent.TButton", background="#1976d2", foreground="white", font=("Segoe UI", 11, "bold"), padding=8)
        style.map("Accent.TButton", background=[("active", "#1565c0")])
        style.configure("TEntry", font=("Segoe UI", 11))
        style.configure("TCombobox", font=("Segoe UI", 11))
        style.configure("TLabelframe", background="#f7fafd", font=("Segoe UI", 11, "bold"))
        style.configure("TLabelframe.Label", font=("Segoe UI", 11, "bold"), foreground="#1976d2")
        style.configure("TCheckbutton", background="#f7fafd", font=("Segoe UI", 10))
        
        # Variables
        self.download_path = tk.StringVar()
        self.youtube_url = tk.StringVar()
        self.selected_quality = tk.StringVar()
        self.download_progress = tk.DoubleVar()
        self.overall_progress = tk.DoubleVar()
        self.status_text = tk.StringVar(value="Ready to download")
        self.overall_status = tk.StringVar(value="")
        
        # Playlist variables
        self.playlist_videos = []
        self.selected_videos = []
        self.is_playlist = False
        
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
        self.check_dependencies()
        
    def check_dependencies(self):
        """Check for yt-dlp and ffmpeg, disable download if missing."""
        errors = []
        # Check yt-dlp
        try:
            import yt_dlp
        except ImportError:
            errors.append("yt-dlp is not installed. Please run: pip install yt-dlp")
        # Check ffmpeg
        if shutil.which("ffmpeg") is None:
            errors.append("FFmpeg is not installed or not in PATH. Please install FFmpeg.")
        if errors:
            self.download_btn.config(state="disabled")
            self.status_text.set("Dependency error!")
            self.show_error("\n".join(errors), log_only=True)
        else:
            self.download_btn.config(state="normal")
        
    def setup_ui(self):
        # Main frame with scrollbar
        main_canvas = tk.Canvas(self.root, bg="#f7fafd", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=main_canvas.yview)
        scrollable_frame = ttk.Frame(main_canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
        )

        main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        main_canvas.configure(yscrollcommand=scrollbar.set)

        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        main_canvas.pack(side="left", fill="both", expand=True)

        # Main frame
        main_frame = ttk.Frame(scrollable_frame, padding="24 18 24 18")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(1, weight=1)
        
        # Logo at the top
        logo_path = os.path.join(os.path.dirname(__file__), "../youtube_downloader_logo.png")
        if os.path.exists(logo_path):
            try:
                logo_img = Image.open(logo_path)
                logo_img = logo_img.resize((64, 64), Image.Resampling.LANCZOS)
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                logo_label = ttk.Label(main_frame, image=self.logo_photo, background="#f7fafd")
                logo_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)
            except Exception:
                pass

        # Title
        title_label = ttk.Label(main_frame, text="YouDownload", font=("Segoe UI", 22, "bold"), foreground="#1976d2", background="#f7fafd")
        title_label.grid(row=0, column=1, columnspan=2, pady=(0, 10), sticky=tk.W)

        # Subtitle
        subtitle = ttk.Label(main_frame, text="Download YouTube videos and playlists easily", font=("Segoe UI", 12), background="#f7fafd", foreground="#555")
        subtitle.grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=(0, 18))
        
        # YouTube URL Section
        url_frame = ttk.Labelframe(main_frame, text="YouTube Video/Playlist URL", padding="14 10 14 10")
        url_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        url_frame.columnconfigure(0, weight=1)
        
        ttk.Label(url_frame, text="Paste YouTube URL:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        url_entry = ttk.Entry(url_frame, textvariable=self.youtube_url, width=60)
        url_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5), ipady=3)
        
        test_btn = ttk.Button(url_frame, text="Test URL", command=self.test_url, style="Accent.TButton")
        test_btn.grid(row=1, column=1, padx=(10, 0))
        
        # Download Location Section
        location_frame = ttk.Labelframe(main_frame, text="Download Location", padding="14 10 14 10")
        location_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        location_frame.columnconfigure(0, weight=1)
        
        ttk.Label(location_frame, text="Choose download folder:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        location_entry = ttk.Entry(location_frame, textvariable=self.download_path, width=50)
        location_entry.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 5), ipady=3)
        
        browse_btn = ttk.Button(location_frame, text="Browse", command=self.browse_location)
        browse_btn.grid(row=1, column=1, padx=(10, 0))
        
        # Quality Selection Section
        quality_frame = ttk.Labelframe(main_frame, text="Video Quality", padding="14 10 14 10")
        quality_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        
        ttk.Label(quality_frame, text="Select quality:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        quality_combo = ttk.Combobox(quality_frame, textvariable=self.selected_quality, 
                                    values=self.qualities, state="readonly", width=30)
        quality_combo.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        quality_combo.set("Best Quality")  # Default selection
        
        # Video/Playlist Info Section
        self.info_frame = ttk.Labelframe(main_frame, text="Video/Playlist Information", padding="14 10 14 10")
        self.info_frame.grid(row=5, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        self.info_frame.columnconfigure(0, weight=1)
        
        # Create a frame for info with scrollbar
        info_canvas = tk.Canvas(self.info_frame, height=220, bg="#f7fafd", highlightthickness=0)
        info_scrollbar = ttk.Scrollbar(self.info_frame, orient="vertical", command=info_canvas.yview)
        self.info_scrollable_frame = ttk.Frame(info_canvas)
        
        self.info_scrollable_frame.bind(
            "<Configure>",
            lambda e: info_canvas.configure(scrollregion=info_canvas.bbox("all"))
        )
        
        info_canvas.create_window((0, 0), window=self.info_scrollable_frame, anchor="nw")
        info_canvas.configure(yscrollcommand=info_scrollbar.set)
        
        info_canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        info_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.info_frame.rowconfigure(0, weight=1)
        self.info_frame.columnconfigure(0, weight=1)
        
        # Loading indicator
        self.loading_label = ttk.Label(self.info_frame, text="", font=("Segoe UI", 10, "italic"), background="#f7fafd")
        self.loading_label.grid(row=1, column=0, pady=(5, 0))
        
        # Overall Progress Section
        overall_frame = ttk.Labelframe(main_frame, text="Overall Progress", padding="14 10 14 10")
        overall_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        overall_frame.columnconfigure(0, weight=1)
        
        self.overall_progress_bar = ttk.Progressbar(overall_frame, variable=self.overall_progress, 
                                                   maximum=100, length=400)
        self.overall_progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.overall_status_label = ttk.Label(overall_frame, textvariable=self.overall_status, background="#f7fafd")
        self.overall_status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Individual Progress Section
        progress_frame = ttk.Labelframe(main_frame, text="Current Download Progress", padding="14 10 14 10")
        progress_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 15))
        progress_frame.columnconfigure(0, weight=1)
        
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.download_progress, 
                                           maximum=100, length=400)
        self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 5))
        
        self.status_label = ttk.Label(progress_frame, textvariable=self.status_text, background="#f7fafd")
        self.status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Download Button
        self.download_btn = ttk.Button(main_frame, text="Download Video", 
                                      command=self.start_download, style="Accent.TButton")
        self.download_btn.grid(row=8, column=0, columnspan=3, pady=(10, 0), ipadx=10, ipady=4)
        
        # Version label at the bottom
        version_label = ttk.Label(main_frame, text=f"Version: {APP_VERSION}", font=("Segoe UI", 9, "italic"), background="#f7fafd", foreground="#888")
        version_label.grid(row=9, column=0, columnspan=3, pady=(30, 0), sticky=tk.E)
        
        # Set default download path
        self.download_path.set(os.path.expanduser("~/Downloads"))
        
    def browse_location(self):
        """Open file dialog to select download location"""
        folder = filedialog.askdirectory(title="Select Download Folder")
        if folder:
            self.download_path.set(folder)
            
    def test_url(self):
        """Test if the YouTube URL is valid and get video/playlist info"""
        url = self.youtube_url.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        if not self.is_valid_youtube_url(url):
            messagebox.showerror("Error", "Please enter a valid YouTube URL")
            return
            
        self.status_text.set("Fetching video/playlist information...")
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
        """Fetch video/playlist information from YouTube"""
        try:
            # Show loading message
            self.root.after(0, lambda: self.loading_label.config(text="Fetching information... Please wait..."))
            
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': True,  # Extract playlist info
                'playlist_items': '1-50',  # Limit to first 50 videos for speed
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Update GUI in main thread
                self.root.after(0, self.update_video_info, info)
                
        except Exception as e:
            tb = traceback.format_exc()
            self.root.after(0, lambda: self.show_error(f"Error fetching video info: {str(e)}\n\n{tb}"))
        finally:
            self.root.after(0, lambda: self.download_btn.config(state="normal"))
            self.root.after(0, lambda: self.loading_label.config(text=""))
            
    def update_video_info(self, info):
        """Update the video/playlist information display"""
        # Clear previous content
        for widget in self.info_scrollable_frame.winfo_children():
            widget.destroy()
        
        self.playlist_videos = []
        self.selected_videos = []
        
        if info.get('_type') == 'playlist':
            self.is_playlist = True
            self.download_btn.config(text="Download Selected Videos")
            
            playlist_info = f"Playlist: {info.get('title', 'Unknown')}\n"
            playlist_info += f"Videos: {len(info.get('entries', []))}\n"
            playlist_info += f"Uploader: {info.get('uploader', 'Unknown')}\n\n"
            playlist_info += "Select videos to download:"
            
            info_label = ttk.Label(self.info_scrollable_frame, text=playlist_info, font=("Segoe UI", 10, "bold"))
            info_label.grid(row=0, column=0, columnspan=3, sticky=tk.W, pady=(0, 10))
            
            row = 1
            for i, entry in enumerate(info.get('entries', [])):
                if entry:
                    video_frame = ttk.Frame(self.info_scrollable_frame)
                    video_frame.grid(row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=2, padx=2)
                    video_frame.columnconfigure(2, weight=1)
                    
                    var = tk.BooleanVar(value=True)
                    checkbox = ttk.Checkbutton(video_frame, variable=var)
                    checkbox.grid(row=0, column=0, padx=(0, 8))
                    
                    # Thumbnail icon (clickable)
                    thumb_btn = ttk.Button(video_frame, text="🖼️", width=2, style="TButton")
                    thumb_btn.grid(row=0, column=1, padx=(0, 8))
                    
                    # Video title
                    title = entry.get('title', 'Unknown Title')
                    title_label = ttk.Label(video_frame, text=title, wraplength=400, font=("Segoe UI", 10, "bold" if var.get() else "normal"))
                    title_label.grid(row=0, column=2, sticky=tk.W)
                    
                    # Store video info
                    video_info = {
                        'id': entry.get('id'),
                        'title': title,
                        'duration': entry.get('duration'),
                        'thumbnail': entry.get('thumbnail'),
                        'checkbox_var': var,
                        'thumb_btn': thumb_btn,
                        'video_frame': video_frame,
                        'thumbnail_loaded': False,
                        'thumbnail_label': None
                    }
                    self.playlist_videos.append(video_info)
                    
                    # Bind click to load thumbnail for this video
                    def make_thumb_loader(vidx):
                        return lambda: self.load_single_thumbnail(vidx)
                    thumb_btn.config(command=make_thumb_loader(i))
                    
                    row += 1
            
            self.status_text.set(f"Playlist loaded: {len(self.playlist_videos)} videos")
            
        else:
            # This is a single video
            self.is_playlist = False
            self.download_btn.config(text="Download Video")
            
            # Single video info
            info_text = f"Title: {info.get('title', 'Unknown')}\n"
            info_text += f"Duration: {self.format_duration(info.get('duration', 0))}\n"
            info_text += f"Uploader: {info.get('uploader', 'Unknown')}\n"
            info_text += f"Views: {info.get('view_count', 'Unknown'):,}\n"
            info_text += f"Upload Date: {info.get('upload_date', 'Unknown')}\n"
            
            # Get available formats
            formats = info.get('formats', [])
            if formats:
                info_text += f"\nAvailable formats: {len(formats)}"
            
            info_label = ttk.Label(self.info_scrollable_frame, text=info_text)
            info_label.grid(row=0, column=0, sticky=tk.W)
            
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
        
        if self.is_playlist:
            # Get selected videos
            self.selected_videos = [video for video in self.playlist_videos if video['checkbox_var'].get()]
            if not self.selected_videos:
                messagebox.showerror("Error", "Please select at least one video to download")
                return
        
        # Disable download button
        self.download_btn.config(state="disabled")
        self.status_text.set("Starting download...")
        self.download_progress.set(0)
        self.overall_progress.set(0)
        
        # Run download in separate thread
        thread = threading.Thread(target=self.download_video, args=(url, download_path, quality))
        thread.daemon = True
        thread.start()
        
    def download_video(self, url, download_path, quality):
        """Download the video(s) in a separate thread"""
        try:
            if self.is_playlist:
                self.download_playlist(url, download_path, quality)
            else:
                self.download_single_video(url, download_path, quality)
                
        except Exception as e:
            tb = traceback.format_exc()
            self.root.after(0, lambda: self.show_error(f"Download failed: {str(e)}\n\n{tb}"))
        finally:
            self.root.after(0, lambda: self.download_btn.config(state="normal"))
    
    def download_single_video(self, url, download_path, quality):
        """Download a single video"""
        ydl_opts = self.get_ydl_options(download_path, quality)
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        self.root.after(0, self.download_completed)
    
    def download_playlist(self, url, download_path, quality):
        """Download selected videos from playlist"""
        total_videos = len(self.selected_videos)
        downloaded_videos = 0
        
        for i, video in enumerate(self.selected_videos):
            # Update overall progress
            overall_percent = (i / total_videos) * 100
            self.root.after(0, lambda p=overall_percent: self.overall_progress.set(p))
            self.root.after(0, lambda v=video: self.overall_status.set(f"Downloading: {v['title'][:50]}... ({i+1}/{total_videos})"))
            
            # Download individual video
            video_url = f"https://www.youtube.com/watch?v={video['id']}"
            ydl_opts = self.get_ydl_options(download_path, quality)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])
            
            downloaded_videos += 1
        
        # Complete overall progress
        self.root.after(0, lambda: self.overall_progress.set(100))
        self.root.after(0, lambda: self.overall_status.set(f"Downloaded {downloaded_videos} videos successfully!"))
        self.root.after(0, self.download_completed)
    
    def get_ydl_options(self, download_path, quality):
        """Get yt-dlp options based on quality selection"""
        ydl_opts = {
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'noplaylist': True,
            'concurrent_fragment_downloads': 4,
        }
        
        if quality == "Audio Only (MP3)":
            ydl_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [
                    {
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    },
                    {
                        'key': 'EmbedThumbnail',  # Embed thumbnail as album art
                    },
                    {
                        'key': 'FFmpegMetadata',  # Ensure metadata is written
                    }
                ],
                'writethumbnail': True,  # Download thumbnail
                'embedthumbnail': True,  # Explicitly request embedding
                'addmetadata': True,     # Add metadata
            })
        elif quality == "Best Quality":
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        elif quality == "1080p":
            ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]/best'
        elif quality == "720p":
            ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]/best'
        elif quality == "480p":
            ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]/best'
        elif quality == "360p":
            ydl_opts['format'] = 'bestvideo[height<=360]+bestaudio/best[height<=360]/best'
        else:
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        
        return ydl_opts
            
    def progress_hook(self, d):
        """Progress hook for yt-dlp"""
        if d['status'] == 'downloading':
            # Update progress bar
            percent = 0
            mb_downloaded = 0
            mb_total = 0
            if 'total_bytes' in d and d['total_bytes']:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                mb_downloaded = d['downloaded_bytes'] / (1024 * 1024)
                mb_total = d['total_bytes'] / (1024 * 1024)
                self.root.after(0, lambda: self.download_progress.set(percent))
            else:
                # Fallback for unknown total size
                if 'downloaded_bytes' in d:
                    mb_downloaded = d['downloaded_bytes'] / (1024 * 1024)
            
            # Update status
            status = f"Downloading: {percent:.1f}% ({mb_downloaded:.2f} MB / {mb_total:.2f} MB)"
            self.root.after(0, lambda: self.status_text.set(status))
            
        elif d['status'] == 'finished':
            self.root.after(0, lambda: self.status_text.set("Processing video..."))
            
    def download_completed(self):
        """Called when download is completed"""
        self.download_progress.set(100)
        if self.is_playlist:
            self.status_text.set("All selected videos downloaded successfully!")
        else:
            self.status_text.set("Download completed successfully!")
        messagebox.showinfo("Success", "Download completed successfully!")
        
    def show_error(self, message, log_only=False):
        """Show error message"""
        self.status_text.set("Error occurred")
        # Log error to file
        with open("error_log.txt", "a", encoding="utf-8") as f:
            f.write(message + "\n" + ("-"*60) + "\n")
        # Show in info box
        if not log_only:
            messagebox.showerror("Error", message)

    def load_single_thumbnail(self, idx):
        """Load thumbnail for a single video by index"""
        video = self.playlist_videos[idx]
        if video['thumbnail_loaded']:
            return  # Already loaded
        thumb_url = video.get('thumbnail', '')
        if not thumb_url:
            return
        try:
            response = requests.get(thumb_url, timeout=5)
            img = Image.open(BytesIO(response.content))
            img = img.resize((80, 45), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            # Remove button and show image
            video['thumb_btn'].destroy()
            thumb_label = ttk.Label(video['video_frame'], image=photo)
            thumb_label.image = photo
            thumb_label.grid(row=0, column=1, padx=(0, 8))
            video['thumbnail_label'] = thumb_label
            video['thumbnail_loaded'] = True
        except Exception as e:
            print(f"Failed to load thumbnail for {video['title']}: {e}")

def main():
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 