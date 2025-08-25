import subprocess
import sys

def build_exe():
	print("Building YouDownload.exe...")
	try:
		import PyInstaller  # noqa: F401
	except ImportError:
		print("PyInstaller not found. Installing...")
		subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

	cmd = [
		sys.executable, "-m", "PyInstaller",
		"--onefile",
		"--windowed",
		"--name=YouDownload",
		"--icon=youtube_downloader_logo.ico",
		"--add-data=youtube_downloader_logo.png;.",
		"--add-data=icons;icons",
		"--hidden-import=PIL.Image",
		"--hidden-import=PIL.ImageTk",
		"--hidden-import=sv_ttk",
		"--hidden-import=yt_dlp",
		"YouDownload/youtube_downloader_gui.py",
	]
	res = subprocess.run(cmd, text=True, capture_output=True)
	if res.returncode != 0:
		print(res.stdout)
		print(res.stderr)
		raise SystemExit(res.returncode)
	print("Done. Check dist/YouDownload.exe")

if __name__ == "__main__":
	build_exe()
