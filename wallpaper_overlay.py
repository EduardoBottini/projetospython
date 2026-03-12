import tkinter as tk
from tkinter import filedialog
from PIL import Image
import ctypes
import os

# Constants for Windows API
SPI_GETDESKWALLPAPER = 0x0073
SPI_SETDESKWALLPAPER = 0x0014

def get_wallpaper():
    buffer = ctypes.create_unicode_buffer(260)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, len(buffer), buffer, 0)
    return buffer.value

def set_wallpaper(path):
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

def overlay_image(bg_path, fg_path):
    bg = Image.open(bg_path).convert("RGBA")
    fg = Image.open(fg_path).convert("RGBA")
    
    # Resize fg to fit bg if needed, but for simplicity, assume fg is overlay size
    # Place fg at center
    bg_width, bg_height = bg.size
    fg_width, fg_height = fg.size
    position = ((bg_width - fg_width) // 2, (bg_height - fg_height) // 2)
    
    bg.paste(fg, position, fg)
    
    temp_path = os.path.join(os.getcwd(), "temp_wallpaper.png")
    bg.save(temp_path)
    return temp_path

def main():
    root = tk.Tk()
    root.title("Wallpaper Overlay")
    
    def select_and_overlay():
        file_path = filedialog.askopenfilename(title="Select image to overlay", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            current_wp = get_wallpaper()
            new_wp = overlay_image(current_wp, file_path)
            set_wallpaper(new_wp)
            root.iconify()  # Minimize the window
    
    button = tk.Button(root, text="Select Image and Overlay", command=select_and_overlay)
    button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()