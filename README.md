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
