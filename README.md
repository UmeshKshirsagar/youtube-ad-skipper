# 📺 YouTube Ad Skipper Automation

This Python script automatically skips **YouTube ads** by detecting and clicking the **"Skip Ad"** button when videos are played in a Chrome browser running in **debugging mode**.

---

## ⚙️ Setup Instructions

### ✅ Step 1: Start Chrome in Debug Mode

Open **Command Prompt** and run the following command:

```bash
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium"

