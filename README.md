# Start Again - Windows App Installer

## Introduction
After reinstalling Windows, getting your development environment and daily-use applications set up can be a tedious and time-consuming process. **Let's Wake Up** is a Python-based desktop application created to help you automatically install all the tools, programming languages, and utilities you need with just one click.

Built with a clean UI using `customtkinter`, this tool allows you to visually select the applications you want and handles the installation process in the background.

## Features
- 🖱️ **User-Friendly GUI**: Simple checklist interface to select exactly what you want to install.
- 🛡️ **Auto-Admin Privileges**: Automatically requests Windows Administrator rights needed for installations.
- 📦 **Chocolatey Integration**: Seamlessly checks for and installs the Chocolatey package manager if it's missing from your system.
- ⚡ **Non-Blocking UI**: Installations run in a background thread, keeping the application responsive while providing real-time log updates.
- 🛠️ **Extensive Software Support**: Includes configurations for web browsers, IDEs, programming languages, gaming platforms, and productivity utilities.

## How It Works
1. **Privilege Escalation**: When you run the script, it checks if it has administrative privileges. If not, it will prompt you for standard Windows UAC permission and relaunch itself as an administrator.
2. **Package Manager Check**: The application verifies if Chocolatey is installed on your machine. If not, it uses PowerShell to download and install Chocolatey automatically.
3. **Batch Installation**: Once you select your desired apps and hit "Install Selected", the app iterates through your choices and silently installs them using Chocolatey commands (`choco install <package_name> -y`).
4. **Live Logging**: A built-in terminal log shows you exactly what is happening, which package is being installed, and if any errors occur.

## Supported Software Categories
- **Core Apps & Tools:** VS Code, Git, Docker, Visual Studio 2022, Postman, DBeaver, etc.
- **Programming Languages:** Python, Java, NodeJS, Rust, Go, Dart, etc.
- **Gaming:** Steam, Epic Games, Discord.
- **Customization & Terminals:** Oh My Posh, Windows Terminal, Everything.
- **Web Browsers:** Google Chrome, Mozilla Firefox, Brave.
- **Utilities & Productivity:** 7-Zip, PowerToys, VLC, Notion, Slack, Zoom, WinRAR, Obsidian.

## How to Use

### Prerequisites
- Windows Operating System.
- Python 3.x installed on your system.

### Installation
1. Clone or download this repository to your local machine.
2. Open your terminal or command prompt in the project directory.
3. Install the required UI library (`customtkinter`) using pip:
   ```bash
   pip install customtkinter
   ```

### Running the Application
1. Execute the main script from your terminal:
   ```bash
   python main.py
   ```
   *(Note: You can also run `install_tools.py` if that is your configured entry point).*
2. If prompted by Windows User Account Control (UAC), click **Yes** to grant administrator privileges.
3. The **Let's Wake Up** interface will appear.
4. Scroll through the list and **check the boxes** next to the applications you wish to install.
5. Click **Install Selected**.
6. Sit back and watch the log window as your computer wakes up and sets itself up!

## Customizing the App List
If you want to add or remove applications from the checklist, simply open `src/app.py` and modify the `CHOCO_PACKAGES` dictionary. The key is the display name, and the value is the official Chocolatey package name.

```python
CHOCO_PACKAGES = {
    "My Custom App": "my-custom-app-choco-name",
    ...
}
```

---
*Created to make Windows reinstalls painless.*