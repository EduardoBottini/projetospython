import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import ctypes
import os
import sys

SPI_GETDESKWALLPAPER = 0x0073
SPI_SETDESKWALLPAPER = 0x0014

BG     = "#1a1a2e"
ACCENT = "#e94560"
WHITE  = "#ffffff"
BLUE   = "#0f3460"
GREEN  = "#2ecc71"
GRAY   = "#aaaaaa"


def get_wallpaper():
    buf = ctypes.create_unicode_buffer(260)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, len(buf), buf, 0)
    return buf.value


def set_wallpaper(path):
    abs_path = os.path.abspath(path)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, abs_path, 3)


def overlay_image(bg_path, fg_path):
    bg = Image.open(bg_path).convert("RGBA")
    fg = Image.open(fg_path).convert("RGBA")

    bg_w, bg_h = bg.size
    fg_w, fg_h = fg.size

    # Scale down the overlay if it is larger than the wallpaper
    if fg_w > bg_w or fg_h > bg_h:
        scale = min(bg_w / fg_w, bg_h / fg_h)
        fg = fg.resize((int(fg_w * scale), int(fg_h * scale)), Image.LANCZOS)
        fg_w, fg_h = fg.size

    position = ((bg_w - fg_w) // 2, (bg_h - fg_h) // 2)

    bg.paste(fg, position, fg)

    result = bg.convert("RGB")

    if getattr(sys, "frozen", False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    temp_path = os.path.join(base_dir, "temp_wallpaper.bmp")

    # Remove stale temp file before writing a fresh one
    if os.path.isfile(temp_path):
        try:
            os.remove(temp_path)
        except OSError:
            pass

    result.save(temp_path, "BMP")
    return temp_path


def styled_btn(parent, text, color, command):
    return tk.Button(
        parent,
        text=text,
        font=("Segoe UI", 11, "bold"),
        bg=color,
        fg=WHITE,
        activebackground=color,
        activeforeground=WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        pady=12,
        padx=20,
        command=command,
    )


def label(parent, text, size=11, bold=False, color=WHITE, **kwargs):
    weight = "bold" if bold else "normal"
    return tk.Label(
        parent,
        text=text,
        font=("Segoe UI", size, weight),
        bg=BG,
        fg=color,
        **kwargs,
    )


def main():
    root = tk.Tk()
    root.title("🖼 Wallpaper Overlay")
    root.geometry("420x260")
    root.resizable(False, False)
    root.configure(bg=BG)

    label(root, "🖼 Wallpaper Overlay", 20, bold=True, color=ACCENT).pack(pady=(30, 6))
    label(root, "Selecione uma imagem para sobrepor ao wallpaper atual.", 10, color=GRAY).pack(pady=(0, 20))

    status_var = tk.StringVar(value="")
    status_lbl = label(root, "", 10, color=GREEN, textvariable=status_var)
    status_lbl.pack(pady=(0, 8))

    def select_and_overlay():
        file_path = filedialog.askopenfilename(
            title="Selecione a imagem",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp *.gif"), ("Todos os arquivos", "*.*")],
        )
        if not file_path:
            return

        current_wp = get_wallpaper()
        if not current_wp or not os.path.isfile(current_wp):
            messagebox.showerror(
                "Erro",
                "Não foi possível obter o wallpaper atual.\nDefinindo a imagem selecionada como wallpaper.",
            )
            set_wallpaper(file_path)
            status_var.set("✅ Wallpaper definido!")
            root.iconify()
            return

        try:
            new_wp = overlay_image(current_wp, file_path)
            set_wallpaper(new_wp)
            status_var.set("✅ Wallpaper atualizado!")
        except Exception as exc:
            messagebox.showerror("Erro", f"Falha ao processar a imagem:\n{exc}")
            return

        root.iconify()

    styled_btn(root, "📂 Selecionar imagem e sobrepor", ACCENT, select_and_overlay).pack()

    root.mainloop()


if __name__ == "__main__":
    main()
