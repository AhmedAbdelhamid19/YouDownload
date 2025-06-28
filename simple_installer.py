import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import shutil
import sys
import subprocess
from pathlib import Path

class YouDownloadInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YouDownload - Installation Wizard")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Center the window
        self.root.eval('tk::PlaceWindow . center')
        
        # Variables
        self.install_path = tk.StringVar()
        self.create_desktop_shortcut = tk.BooleanVar(value=True)
        self.create_start_menu = tk.BooleanVar(value=True)
        self.auto_launch = tk.BooleanVar(value=True)
        
        # Default installation path
        default_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "YouDownload")
        self.install_path.set(default_path)
        
        self.current_step = 0
        self.steps = [
            self.welcome_step,
            self.license_step,
            self.install_location_step,
            self.options_step,
            self.install_step,
            self.finish_step
        ]
        
        self.setup_ui()
        self.show_current_step()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Title
        self.title_label = ttk.Label(main_frame, text="YouDownload Installation Wizard", 
                                    font=("Arial", 16, "bold"))
        self.title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, maximum=len(self.steps), length=400)
        self.progress.grid(row=1, column=0, pady=(0, 20))
        
        # Content frame
        self.content_frame = ttk.Frame(main_frame)
        self.content_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        self.content_frame.columnconfigure(0, weight=1)
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, sticky=(tk.W, tk.E))
        button_frame.columnconfigure(1, weight=1)
        
        self.back_btn = ttk.Button(button_frame, text="< Back", command=self.previous_step)
        self.back_btn.grid(row=0, column=0, padx=(0, 10))
        
        self.next_btn = ttk.Button(button_frame, text="Next >", command=self.next_step)
        self.next_btn.grid(row=0, column=1, padx=(10, 0))
        
        self.cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.cancel_installation)
        self.cancel_btn.grid(row=0, column=2, padx=(10, 0))
        
    def show_current_step(self):
        # Clear content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        
        # Show current step
        self.steps[self.current_step]()
        
        # Update progress
        self.progress['value'] = self.current_step + 1
        
        # Update buttons
        if self.current_step == 0:
            self.back_btn.config(state="disabled")
        else:
            self.back_btn.config(state="normal")
            
        if self.current_step == len(self.steps) - 1:
            self.next_btn.config(text="Finish")
        else:
            self.next_btn.config(text="Next >")
    
    def welcome_step(self):
        # Welcome message
        welcome_text = """Welcome to the YouDownload Installation Wizard!

This wizard will guide you through the installation of YouDownload, 
a modern YouTube video downloader with a beautiful GUI interface.

Features:
• Download YouTube videos in multiple qualities (1080p, 720p, 480p, 360p)
• Extract audio as MP3 files
• Modern, user-friendly interface
• Progress tracking and video information

Click Next to continue with the installation."""
        
        text_widget = tk.Text(self.content_frame, height=12, width=60, wrap=tk.WORD, 
                             font=("Arial", 10), state=tk.DISABLED)
        text_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Enable text widget to insert content
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, welcome_text)
        text_widget.config(state=tk.DISABLED)
    
    def license_step(self):
        # License agreement
        license_text = """MIT License

Copyright (c) 2024 YouDownload Team
Team: 
    - Ahmed Abdlehamid Ahmed

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
        
        # License frame
        license_frame = ttk.LabelFrame(self.content_frame, text="License Agreement", padding="10")
        license_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        license_frame.columnconfigure(0, weight=1)
        license_frame.rowconfigure(0, weight=1)
        
        text_widget = tk.Text(license_frame, height=15, width=60, wrap=tk.WORD, 
                             font=("Arial", 9), state=tk.DISABLED)
        text_widget.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(license_frame, orient=tk.VERTICAL, command=text_widget.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        text_widget.config(yscrollcommand=scrollbar.set)
        
        # Enable text widget to insert content
        text_widget.config(state=tk.NORMAL)
        text_widget.insert(tk.END, license_text)
        text_widget.config(state=tk.DISABLED)
        
        # Agreement checkbox
        self.agree_var = tk.BooleanVar()
        agree_check = ttk.Checkbutton(self.content_frame, text="I accept the terms of the License Agreement", 
                                     variable=self.agree_var)
        agree_check.grid(row=1, column=0, pady=(10, 0))
    
    def install_location_step(self):
        # Installation location
        location_frame = ttk.LabelFrame(self.content_frame, text="Installation Location", padding="10")
        location_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        location_frame.columnconfigure(0, weight=1)
        
        ttk.Label(location_frame, text="Choose the installation folder:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        path_frame = ttk.Frame(location_frame)
        path_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        path_frame.columnconfigure(0, weight=1)
        
        path_entry = ttk.Entry(path_frame, textvariable=self.install_path, width=50)
        path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        browse_btn = ttk.Button(path_frame, text="Browse", command=self.browse_location)
        browse_btn.grid(row=0, column=1)
        
        # Space required
        space_frame = ttk.Frame(location_frame)
        space_frame.grid(row=2, column=0, sticky=(tk.W, tk.E))
        
        ttk.Label(space_frame, text="Space required: ~20 MB").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(space_frame, text="Space available: " + self.get_free_space()).grid(row=1, column=0, sticky=tk.W)
    
    def options_step(self):
        # Installation options
        options_frame = ttk.LabelFrame(self.content_frame, text="Installation Options", padding="10")
        options_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Desktop shortcut
        desktop_check = ttk.Checkbutton(options_frame, text="Create a desktop shortcut", 
                                       variable=self.create_desktop_shortcut)
        desktop_check.grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        # Start menu
        start_check = ttk.Checkbutton(options_frame, text="Create Start Menu shortcuts", 
                                     variable=self.create_start_menu)
        start_check.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        # Auto launch
        launch_check = ttk.Checkbutton(options_frame, text="Launch YouDownload after installation", 
                                      variable=self.auto_launch)
        launch_check.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        
        # FFmpeg notice
        notice_frame = ttk.Frame(options_frame)
        notice_frame.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(20, 0))
        
        ttk.Label(notice_frame, text="Note: You may need to install FFmpeg for full functionality.", 
                 font=("Arial", 9, "italic")).grid(row=0, column=0, sticky=tk.W)
        ttk.Label(notice_frame, text="See README.md for installation instructions.", 
                 font=("Arial", 9, "italic")).grid(row=1, column=0, sticky=tk.W)
    
    def install_step(self):
        # Installation progress
        progress_frame = ttk.LabelFrame(self.content_frame, text="Installing YouDownload", padding="10")
        progress_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))
        progress_frame.columnconfigure(0, weight=1)
        
        self.install_progress = ttk.Progressbar(progress_frame, mode='indeterminate')
        self.install_progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.status_label = ttk.Label(progress_frame, text="Preparing installation...")
        self.status_label.grid(row=1, column=0, sticky=tk.W)
        
        # Start installation
        self.install_progress.start()
        self.root.after(100, self.perform_installation)
    
    def finish_step(self):
        # Finish screen
        self.clear_window()
        self.show_header("Installation Complete!")
        
        print("🎉 YouDownload has been successfully installed!")
        print()
        print("📁 Installation location:")
        print(f"   {self.install_path}")
        print()
        print("🚀 How to launch YouDownload:")
        print("   • Desktop shortcut: Double-click 'YouDownload' on your desktop")
        print("   • Start Menu: Search for 'YouDownload' in the Start Menu")
        print("   • Direct launch: Double-click 'YouDownload.bat' in this folder")
        print()
        print("📋 What's included:")
        print("   ✅ YouTube video downloader with GUI")
        print("   ✅ Playlist support with video selection")
        print("   ✅ Audio extraction with thumbnail embedding")
        print("   ✅ Progress tracking and error handling")
        print("   ✅ FFmpeg for video processing")
        print()
        print("💡 Tips:")
        print("   • Paste YouTube URLs (videos or playlists) to get started")
        print("   • Use the 'Download Audio' option for music files")
        print("   • Check 'Load thumbnails' to see video previews")
        print()
        print("🔧 Need help? Check the README.md file for detailed instructions.")
        print()
        
        if self.create_desktop_shortcut:
            print("🖥️  A desktop shortcut has been created for easy access!")
        if self.create_start_menu.get():
            print("📋 A Start Menu shortcut has been created!")
        print()
        
        input("Press Enter to exit...")
    
    def browse_location(self):
        folder = filedialog.askdirectory(title="Choose Installation Folder")
        if folder:
            self.install_path.set(folder)
    
    def get_free_space(self):
        try:
            path = self.install_path.get()
            if os.path.exists(path):
                stat = os.statvfs(path)
                free_space = stat.f_frsize * stat.f_bavail
                return f"{free_space // (1024*1024)} MB"
            else:
                return "Unknown"
        except:
            return "Unknown"
    
    def perform_installation(self):
        try:
            install_dir = self.install_path.get()
            
            # Create installation directory
            self.status_label.config(text="Creating installation directory...")
            os.makedirs(install_dir, exist_ok=True)
            
            # Copy executable
            self.status_label.config(text="Copying files...")
            exe_source = "dist/YouDownload.exe"
            exe_dest = os.path.join(install_dir, "YouDownload.exe")
            shutil.copy2(exe_source, exe_dest)
            
            # Copy logo
            logo_source = "youtube_downloader_logo.ico"
            logo_dest = os.path.join(install_dir, "youtube_downloader_logo.ico")
            shutil.copy2(logo_source, logo_dest)
            
            # Copy source files
            source_dir = os.path.join(install_dir, "YouDownload")
            shutil.copytree("YouDownload", source_dir, dirs_exist_ok=True)
            
            # Create desktop shortcut
            if self.create_desktop_shortcut.get():
                self.status_label.config(text="Creating desktop shortcut...")
                self.create_shortcut(exe_dest, "Desktop")
            
            # Create start menu shortcut
            if self.create_start_menu.get():
                self.status_label.config(text="Creating Start Menu shortcuts...")
                self.create_shortcut(exe_dest, "StartMenu")
            
            # Installation complete
            self.install_progress.stop()
            self.status_label.config(text="Installation completed successfully!")
            
            # Auto launch if selected
            if self.auto_launch.get():
                self.root.after(1000, lambda: subprocess.Popen([exe_dest]))
            
        except Exception as e:
            self.install_progress.stop()
            self.status_label.config(text=f"Installation failed: {str(e)}")
            messagebox.showerror("Installation Error", f"Failed to install YouDownload:\n{str(e)}")
    
    def create_shortcut(self, target_path, location):
        try:
            if location == "Desktop":
                shortcut_path = os.path.join(os.path.expanduser("~"), "Desktop", "YouDownload.lnk")
            elif location == "StartMenu":
                start_menu = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs")
                os.makedirs(start_menu, exist_ok=True)
                shortcut_path = os.path.join(start_menu, "YouDownload.lnk")
            
            # Get the icon path (copy icon to installation directory)
            icon_source = "youtube_downloader_logo.ico"
            icon_dest = os.path.join(os.path.dirname(target_path), "youtube_downloader_logo.ico")
            
            # Copy icon if it exists
            if os.path.exists(icon_source):
                shutil.copy2(icon_source, icon_dest)
            
            # Create shortcut using PowerShell with custom icon
            ps_script = f'''
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
$Shortcut.TargetPath = "{target_path}"
$Shortcut.WorkingDirectory = "{os.path.dirname(target_path)}"
$Shortcut.IconLocation = "{icon_dest}"
$Shortcut.Description = "YouTube Video Downloader - Download videos and playlists from YouTube"
$Shortcut.Save()
'''
            
            # Write and run PowerShell script
            with open("create_shortcut_temp.ps1", "w") as f:
                f.write(ps_script)
            
            subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", "create_shortcut_temp.ps1"], 
                         capture_output=True)
            
            # Clean up
            os.remove("create_shortcut_temp.ps1")
            
        except Exception as e:
            print(f"Failed to create shortcut: {e}")
    
    def next_step(self):
        # Validate current step
        if self.current_step == 1 and not self.agree_var.get():
            messagebox.showwarning("License Agreement", "You must accept the license agreement to continue.")
            return
        
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.show_current_step()
        else:
            self.root.quit()
    
    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
            self.show_current_step()
    
    def cancel_installation(self):
        if messagebox.askyesno("Cancel Installation", "Are you sure you want to cancel the installation?"):
            self.root.quit()
    
    def run(self):
        self.root.mainloop()

def main():
    # Check if executable exists
    if not os.path.exists("dist/YouDownload.exe"):
        messagebox.showerror("Error", "YouDownload.exe not found in dist/ folder.\nPlease build the executable first.")
        return
    
    # Run installer
    installer = YouDownloadInstaller()
    installer.run()

if __name__ == "__main__":
    main() 