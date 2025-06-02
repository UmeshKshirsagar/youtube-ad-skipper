# 📺 YouTube Ad Skipper Automation

This Python script automatically skips **YouTube ads** by detecting and clicking the **"Skip Ad"** button when videos are played in a Chrome browser running in **debugging mode**.

---

## ⚙️ Setup Instructions

### ✅ Step 1: Start Chrome in Debug Mode

Open **Command Prompt** and run the following command:

```bash
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium"
📝 Make sure the path to chrome.exe is correct for your system.
This command opens Chrome with remote debugging enabled (required for Selenium to attach).

✅ Step 2: Run the Python Script
In a new Command Prompt window, navigate to the project folder and run:

bash
Copy
python youtube_ad_skipper.py
💡 This script will attach to your running Chrome session and automatically skip ads whenever the "Skip Ad" button appears on YouTube.

🖥️ Automate on Windows
You can fully automate this so you never have to run commands manually.

🔁 Auto-Run When Chrome Is Open
Use the included batch file to detect when Chrome is open and launch the script:

batch
Copy
detect_chrome.bat
🧠 Optional: Automate with Task Scheduler
You can schedule the following batch files to run automatically at login:

start_chrome_debug.bat – launches Chrome in debug mode

detect_chrome.bat – waits for Chrome, then runs the Python script

Set them to run via Windows Task Scheduler using the "At log on" trigger.

📁 Project Files
File Name	Description
youtube_ad_skipper.py	Main Python script that skips YouTube ads
start_chrome_debug.bat	Starts Chrome in debugging mode
detect_chrome.bat	Detects when Chrome is running, then starts script

💡 Tip
To avoid keeping the Command Prompt window open, make sure your batch files use:

batch
Copy
start /B python "C:\path\to\youtube_ad_skipper.py"
This allows the script to run silently in the background.

