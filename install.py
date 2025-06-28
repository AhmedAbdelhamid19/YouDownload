import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os
import threading
import webbrowser

class YouDownloadInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouDownload Installer")
        self.root.geometry("600x480")
        self.root.minsize(600, 480)
        self.root.configure(bg="#f7fafd")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#f7fafd")
        style.configure("TLabel", background="#f7fafd", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("Accent.TButton", background="#1976d2", foreground="white", font=("Segoe UI", 11, "bold"), padding=8)
        style.map("Accent.TButton", background=[("active", "#1565c0")])
        
        # Variables
        self.current_step = 0
        self.install_steps = [
            "Welcome",
            "Check Dependencies", 
            "Install Python Dependencies",
            "Install FFmpeg",
            "Create Shortcuts",
            "Finish"
        ]
        
        self.setup_ui()
        self.show_step(0)
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        main_frame.pack_propagate(0)
        
        # Title
        title_label = ttk.Label(main_frame, text="YouDownload Installer", 
                               font=("Segoe UI", 18, "bold"), foreground="#1976d2")
        title_label.pack(pady=(0, 20))
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, length=500, mode='determinate')
        self.progress.pack(pady=(0, 20))
        
        # Step label
        self.step_label = ttk.Label(main_frame, text="", font=("Segoe UI", 12, "bold"))
        self.step_label.pack(pady=(0, 20))
        
        # Content frame
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        self.content_frame.pack_propagate(0)
        
        # Button frame (always at the bottom)
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
        # Buttons
        self.back_btn = ttk.Button(button_frame, text="Back", command=self.previous_step)
        self.back_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.next_btn = ttk.Button(button_frame, text="Next", command=self.next_step, style="Accent.TButton")
        self.next_btn.pack(side=tk.RIGHT)
        
        self.cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.root.quit)
        self.cancel_btn.pack(side=tk.RIGHT, padx=(0, 10))
        
    def show_step(self, step):
        self.current_step = step
        self.progress['value'] = (step / (len(self.install_steps) - 1)) * 100
        self.step_label.config(text=f"Step {step + 1}: {self.install_steps[step]}")
        
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        # Update buttons
        if step == 0:
            self.back_btn.config(state="disabled")
            self.next_btn.config(state="normal")  # Enable Next button on first step
        else:
            self.back_btn.config(state="normal")
            self.next_btn.config(state="normal")  # Enable Next button on all other steps
            
        if step == len(self.install_steps) - 1:
            self.next_btn.config(text="Finish")
        else:
            self.next_btn.config(text="Next")
            
        # Show step content
        if step == 0:
            self.show_welcome()
        elif step == 1:
            self.show_dependency_check()
        elif step == 2:
            self.show_python_deps()
        elif step == 3:
            self.show_ffmpeg_install()
        elif step == 4:
            self.show_shortcuts()
        elif step == 5:
            self.show_finish()
            
    def show_welcome(self):
        welcome_text = """Welcome to YouDownload!

This installer will help you set up YouDownload on your system.

YouDownload is a modern GUI application for downloading YouTube videos and playlists with features like:
• Multiple quality options
• Playlist support with video selection
• Audio downloads with embedded album art
• Progress tracking

Click Next to continue with the installation."""
        
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, height=12, 
                             font=("Segoe UI", 10), bg="#f7fafd", relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, welcome_text)
        text_widget.config(state=tk.DISABLED)
        
    def show_dependency_check(self):
        self.check_label = ttk.Label(self.content_frame, text="Checking system requirements...", 
                                    font=("Segoe UI", 11))
        self.check_label.pack(pady=20)
        
        self.check_progress = ttk.Progressbar(self.content_frame, mode='indeterminate')
        self.check_progress.pack(pady=10)
        self.check_progress.start()
        
        # Run check in thread
        thread = threading.Thread(target=self.check_dependencies)
        thread.daemon = True
        thread.start()
        
    def check_dependencies(self):
        results = {}
        
        # Check Python
        results['python'] = sys.version_info >= (3, 7)
        
        # Check pip
        try:
            subprocess.run([sys.executable, '-m', 'pip', '--version'], 
                         capture_output=True, check=True)
            results['pip'] = True
        except:
            results['pip'] = False
            
        # Check FFmpeg
        try:
            subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
            results['ffmpeg'] = True
        except:
            results['ffmpeg'] = False
            
        self.root.after(0, lambda: self.show_check_results(results))
        
    def show_check_results(self, results):
        self.check_progress.stop()
        self.check_progress.destroy()
        
        result_text = "System Requirements Check:\n\n"
        
        if results['python']:
            result_text += "✅ Python 3.7+ - Found\n"
        else:
            result_text += "❌ Python 3.7+ - Not found\n"
            
        if results['pip']:
            result_text += "✅ pip - Found\n"
        else:
            result_text += "❌ pip - Not found\n"
            
        if results['ffmpeg']:
            result_text += "✅ FFmpeg - Found\n"
        else:
            result_text += "❌ FFmpeg - Not found\n"
            
        result_text += "\n"
        
        if all(results.values()):
            result_text += "All requirements are met! You can proceed with the installation."
            self.next_btn.config(state="normal")
        else:
            result_text += "Some requirements are missing. The installer will help you install them."
            self.next_btn.config(state="normal")
            
        self.check_label.config(text=result_text)
        
    def show_python_deps(self):
        deps_text = """Python Dependencies Installation

The installer will now install the required Python packages:
• yt-dlp (YouTube downloader)
• Pillow (Image processing)
• requests (HTTP requests)

Click Next to install these dependencies."""
        
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, height=8, 
                             font=("Segoe UI", 10), bg="#f7fafd", relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, deps_text)
        text_widget.config(state=tk.DISABLED)
        
        install_btn = ttk.Button(self.content_frame, text="Install Dependencies", 
                                command=self.install_python_deps, style="Accent.TButton")
        install_btn.pack(pady=20)
        
    def install_python_deps(self):
        self.install_label = ttk.Label(self.content_frame, text="Installing Python dependencies...")
        self.install_label.pack(pady=20)
        
        self.install_progress = ttk.Progressbar(self.content_frame, mode='indeterminate')
        self.install_progress.pack(pady=10)
        self.install_progress.start()
        
        thread = threading.Thread(target=self._install_deps)
        thread.daemon = True
        thread.start()
        
    def _install_deps(self):
        try:
            # Install dependencies
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'yt-dlp', 'Pillow', 'requests'], 
                         check=True, capture_output=True)
            self.root.after(0, lambda: self.show_install_success("Python dependencies installed successfully!"))
        except subprocess.CalledProcessError as e:
            self.root.after(0, lambda: self.show_install_error(f"Failed to install dependencies: {e}"))
            
    def show_install_success(self, message):
        self.install_progress.stop()
        self.install_progress.destroy()
        self.install_label.config(text=f"✅ {message}")
        
    def show_install_error(self, message):
        self.install_progress.stop()
        self.install_progress.destroy()
        self.install_label.config(text=f"❌ {message}")
        
    def show_ffmpeg_install(self):
        ffmpeg_text = """FFmpeg Installation

FFmpeg is required for video processing and audio conversion.

If FFmpeg is not installed, you can:
1. Download from ffmpeg.org
2. Use package managers (Chocolatey, Winget, etc.)
3. Follow the instructions in the README

Click Next to continue."""
        
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, height=8, 
                             font=("Segoe UI", 10), bg="#f7fafd", relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, ffmpeg_text)
        text_widget.config(state=tk.DISABLED)
        
        download_btn = ttk.Button(self.content_frame, text="Download FFmpeg", 
                                 command=lambda: webbrowser.open("https://ffmpeg.org/download.html"))
        download_btn.pack(pady=10)
        
    def show_shortcuts(self):
        shortcuts_text = """Create Desktop Shortcuts

The installer can create desktop shortcuts for easy access to YouDownload.

This will create:
• Desktop shortcut
• Start menu entry (Windows)"""
        
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, height=6, 
                             font=("Segoe UI", 10), bg="#f7fafd", relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, shortcuts_text)
        text_widget.config(state=tk.DISABLED)
        
        create_btn = ttk.Button(self.content_frame, text="Create Shortcuts", 
                               command=self.create_shortcuts, style="Accent.TButton")
        create_btn.pack(pady=20)
        
    def create_shortcuts(self):
        try:
            # Create desktop shortcut
            desktop = os.path.expanduser("~/Desktop")
            shortcut_path = os.path.join(desktop, "YouDownload.bat")
            
            with open(shortcut_path, 'w') as f:
                f.write(f'@echo off\ncd /d "{os.path.dirname(os.path.abspath(__file__))}"\npython YouDownload/youtube_downloader_gui.py\npause')
                
            messagebox.showinfo("Success", "Desktop shortcut created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create shortcut: {e}")
            
    def show_finish(self):
        finish_text = """Installation Complete!

YouDownload has been successfully installed on your system.

To start using YouDownload:
1. Double-click the desktop shortcut, or
2. Run: python YouDownload/youtube_downloader_gui.py

Thank you for choosing YouDownload!"""
        
        text_widget = tk.Text(self.content_frame, wrap=tk.WORD, height=8, 
                             font=("Segoe UI", 10), bg="#f7fafd", relief=tk.FLAT)
        text_widget.pack(fill=tk.BOTH, expand=True)
        text_widget.insert(tk.END, finish_text)
        text_widget.config(state=tk.DISABLED)
        
    def next_step(self):
        if self.current_step < len(self.install_steps) - 1:
            self.show_step(self.current_step + 1)
        else:
            self.root.quit()
            
    def previous_step(self):
        if self.current_step > 0:
            self.show_step(self.current_step - 1)
            
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    installer = YouDownloadInstaller()
    installer.run() 