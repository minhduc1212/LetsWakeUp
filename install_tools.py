import subprocess
import sys
import ctypes
import os

# Mapping of your tools from idea.txt to their Chocolatey package names
CHOCO_PACKAGES = {
    # Core Apps & Tools
    "Visual Studio Code": "vscode",
    "Git": "git",
    "Docker": "docker-desktop",
    "Visual Studio 2022": "visualstudio2022community",
    "Mitm Proxy": "mitmproxy",
    "Postman": "postman",
    "DBeaver": "dbeaver",

    # Programming Languages
    "Python": "python",
    "Java": "openjdk",
    "NodeJS": "nodejs",
    "Rust": "rust",
    "Go": "golang",
    "Dart": "dart-sdk",
    
    # Gaming
    "Steam": "steam",
    "Epic Games": "epicgameslauncher",
    "Discord": "discord",

    # Decorate / Terminals
    "Oh My Posh": "oh-my-posh",
    "Windows Terminal": "microsoft-windows-terminal",
    "Everything": "everything",

    # Web Browsers
    "Google Chrome": "googlechrome",
    "Mozilla Firefox": "firefox",
    "Brave": "brave",

    # Utilities & Productivity
    "7-Zip": "7zip",
    "Microsoft PowerToys": "powertoys",
    "VLC Media Player": "vlc",
    "Notion": "notion",
    "Slack": "slack",
    "Zoom": "zoom",
    "WinRAR": "winrar",
    "Obsidian": "obsidian"
}

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def install_choco():
    """Install Chocolatey if it is not already installed."""
    try:
        subprocess.run(["choco", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Chocolatey is already installed.")
    except FileNotFoundError:
        print("Installing Chocolatey...")
        ps_command = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        subprocess.run(["powershell", "-Command", ps_command], check=True)

def install_packages():
    """Iterate through the dictionary and install each package silently."""
    print(f"\nStarting installation of {len(CHOCO_PACKAGES)} packages...\n")
    for name, pkg in CHOCO_PACKAGES.items():
        print(f"Installing {name}...")
        subprocess.run(["choco", "install", pkg, "-y"], shell=True)
        print(f"Finished processing {name}.\n")

if __name__ == "__main__":
    if not is_admin():
        print("Requesting administrative privileges...")
        # Re-run the script with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()
        
    install_choco()
    install_packages()
    
    print("All tool installations completed!")
    input("Press Enter to exit...")