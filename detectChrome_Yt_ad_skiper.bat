@echo off
:loop
tasklist | find /i "chrome.exe" >nul
if errorlevel 1 (
    echo Chrome is not running, waiting...
    timeout /t 10
    goto loop
) else (
    echo Chrome detected! Running the script...
    start /B python "C:\Umesh\skip_youtube_ads.py"
    exit
)
