import webbrowser
import os
import subprocess

def open_facebook():
    webbrowser.open("https://web.facebook.com/")

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_musicplayer():
    subprocess.Popen('\\localhost\C$\@GMT-2022.01.13-09.04.00\Program Files\WindowsApps\Microsoft.ZuneMusic_10.21102.11411.0_x64__8wekyb3d8bbwe\Music.UI.Exe')

def close_browser():
    browserExe = "chrome"
    os.system("taskkill /f /im"+browserExe)