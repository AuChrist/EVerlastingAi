import ctypes
import os
from os.path import isfile, join
import random
import time

def change_wallpaper():
    wallpapers = ("C:/Users/Yukino Arata/Pictures/Anime/Ganyu Wangy")

    wallpaper = [f for f in os.listdir(wallpapers) if isfile(join(wallpapers, f))]

    wallpaper_on = random.choices(wallpaper)
   
    for image in wallpaper:
        print(image)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpapers+ "\\" + wallpaper_on, 0)
        