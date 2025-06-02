from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.debugger_address = "localhost:9222"

driver = webdriver.Chrome(options=options)

# Switch to the YouTube tab
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "YouTube" in driver.title:
        print("Switched to YouTube tab!")
        break

while True:
    try:
        # Find and click the new Skip Ad button
        skip_buttons = driver.find_elements(By.CLASS_NAME, "ytp-skip-ad-button")

        if skip_buttons:
            for button in skip_buttons:
                button.click()
                print("✅ Ad skipped successfully!")
        else:
            print("⏳ No skip button detected...")

    except Exception as e:
        print("Error:", e)

    time.sleep(2)  # Check every 2 seconds
