import traceback
import tkinter as tk
import youtube_downloader_gui

def main():
    try:
        root = tk.Tk()
        app = youtube_downloader_gui.YouTubeDownloaderGUI(root)
        root.mainloop()
    except Exception:
        print("Error occurred:")
        print(traceback.format_exc())
        input("Press Enter to exit...")

if __name__ == "__main__":
    main()