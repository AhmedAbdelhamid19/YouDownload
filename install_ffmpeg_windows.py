import os
import sys
import zipfile
import shutil
import urllib.request
import subprocess
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_ffmpeg(dest_folder):
    print("Downloading FFmpeg...")
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    zip_path = os.path.join(dest_folder, "ffmpeg.zip")
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete.")
    return zip_path

def extract_ffmpeg(zip_path, dest_folder):
    print("Extracting FFmpeg...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    # Find the extracted folder
    for name in os.listdir(dest_folder):
        if name.lower().startswith("ffmpeg") and os.path.isdir(os.path.join(dest_folder, name)):
            bin_path = os.path.join(dest_folder, name, "bin")
            return bin_path
    raise Exception("FFmpeg bin folder not found after extraction.")

def add_to_path(bin_path):
    print(f"Adding {bin_path} to system PATH...")
    # Read current PATH
    import winreg
    reg_path = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
    with winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE) as reg:
        with winreg.OpenKey(reg, reg_path, 0, winreg.KEY_READ | winreg.KEY_WRITE) as key:
            value, _ = winreg.QueryValueEx(key, "Path")
            if bin_path.lower() not in value.lower():
                new_value = value + ";" + bin_path
                winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_value)
                print("PATH updated. You may need to restart your computer.")
            else:
                print("FFmpeg bin path already in PATH.")

def verify_ffmpeg():
    print("Verifying FFmpeg installation...")
    try:
        result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("FFmpeg installed successfully!")
            print(result.stdout.splitlines()[0])
            return True
        else:
            print("FFmpeg not found in PATH.")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"Error running ffmpeg: {e}")
        return False

def main():
    if not is_admin():
        print("This script must be run as administrator to update the system PATH.")
        print("Right-click on Command Prompt and choose 'Run as administrator', then run this script again.")
        sys.exit(1)
    dest_folder = os.path.abspath("C:/ffmpeg")
    os.makedirs(dest_folder, exist_ok=True)
    zip_path = download_ffmpeg(dest_folder)
    bin_path = extract_ffmpeg(zip_path, dest_folder)
    add_to_path(bin_path)
    os.remove(zip_path)
    print("FFmpeg setup complete.")
    print("Please restart your computer for PATH changes to take effect.")
    verify_ffmpeg()

if __name__ == "__main__":
    main() 