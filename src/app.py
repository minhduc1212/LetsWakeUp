import customtkinter as ctk
import subprocess
import threading

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

def install_choco(log_callback):
    """Install Chocolatey if it is not already installed."""
    try:
        subprocess.run(["choco", "-v"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        log_callback("Chocolatey is already installed.\n")
    except FileNotFoundError:
        log_callback("Installing Chocolatey...\n")
        ps_command = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        try:
            subprocess.run(["powershell", "-Command", ps_command], check=True, capture_output=True, text=True)
            log_callback("Chocolatey installation completed.\n")
        except subprocess.CalledProcessError as e:
            log_callback(f"Failed to install Chocolatey.\n{e.stderr}\n")

class InstallerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Let's Wake Up - App Installer")
        self.geometry("600x700")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="Select Applications to Install")
        self.scrollable_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.checkboxes = {}
        for name, pkg in CHOCO_PACKAGES.items():
            var = ctk.StringVar(value=pkg)  # Default all to checked state
            checkbox = ctk.CTkCheckBox(self.scrollable_frame, text=name, variable=var, onvalue=pkg, offvalue="")
            checkbox.pack(anchor="w", pady=5, padx=10)
            self.checkboxes[name] = var

        self.install_button = ctk.CTkButton(self, text="Install Selected", command=self.start_installation)
        self.install_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        self.log_textbox = ctk.CTkTextbox(self, height=150)
        self.log_textbox.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="nsew")
        self.log_textbox.configure(state="disabled")

    def log_message(self, message):
        self.log_textbox.configure(state="normal")
        self.log_textbox.insert("end", message)
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def start_installation(self):
        selected_packages = {name: var.get() for name, var in self.checkboxes.items() if var.get() != ""}
        
        if not selected_packages:
            self.log_message("No applications selected.\n")
            return

        self.install_button.configure(state="disabled")
        
        # Run in a separate thread to prevent UI freezing
        threading.Thread(target=self.install_packages, args=(selected_packages,), daemon=True).start()

    def install_packages(self, packages):
        self.log_message("Checking Chocolatey installation...\n")
        install_choco(self.log_message)

        self.log_message(f"\nStarting installation of {len(packages)} packages...\n")
        for name, pkg in packages.items():
            self.log_message(f"Installing {name}...\n")
            process = subprocess.run(["choco", "install", pkg, "-y"], shell=True, capture_output=True, text=True)
            if process.returncode == 0:
                self.log_message(f"Finished installing {name}.\n\n")
            else:
                self.log_message(f"Error installing {name}.\n{process.stderr}\n\n")

        self.log_message("All tool installations completed!\n")
        self.install_button.configure(state="normal")