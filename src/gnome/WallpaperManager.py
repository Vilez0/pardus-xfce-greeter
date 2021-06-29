import os, subprocess

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

folders = ["/usr/share/backgrounds/", "/usr/share/desktop-base/active-theme/wallpaper/contents/images/"]
prefixs = ["jpg","png","bmp","jpeg","svg"]

def getWallpaperList():
    pictures = []
    for path in folders:
        paths = os.walk( path )
        for (dirpath, _, files) in paths:
            for file in files:
                for prefix in prefixs:
                    if file[-3:] == prefix:
                        pictures.append(f"{dirpath}/{file}")
                        break
    
    return pictures

def setWallpaper(wallpaper):
    subprocess.call([
        "gsettings",
        "set",
        "org.gnome.desktop.background",
        "picture-uri",
        f"file://{wallpaper}"
    ])