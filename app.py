import os
import sys
from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image


def convert_images():
    files = filedialog.askopenfilenames(
        filetypes=[("Images", "*.jpg *.jpeg *.png")]
    )

    if not files:
        return

    use_same_folder = same_folder_var.get()

    if not use_same_folder:
        output_dir = filedialog.askdirectory()
        if not output_dir:
            return

    compression_mode = compression_var.get()

    if compression_mode == "Recomendada (alta calidad)":
        quality = 90
    else:
        quality = 80

    total_before = 0
    total_after = 0
    details = []

    progress["maximum"] = len(files)
    progress["value"] = 0

    for i, file in enumerate(files):
        img = Image.open(file)

        size_before = os.path.getsize(file)
        total_before += size_before

        filename = os.path.splitext(os.path.basename(file))[0] + ".webp"

        if use_same_folder:
            output_path = os.path.splitext(file)[0] + ".webp"
        else:
            output_path = os.path.join(output_dir, filename)

        img.save(output_path, "WEBP", quality=quality, method=6)

        size_after = os.path.getsize(output_path)
        total_after += size_after

        details.append(
            f"{filename}\n"
            f"  Antes: {size_before/1024:.2f} KB\n"
            f"  Después: {size_after/1024:.2f} KB\n"
        )

        progress["value"] = i + 1
        root.update_idletasks()

    ahorro = total_before - total_after

    # Mostrar primero totales
    result_text.delete("1.0", END)

    result_text.insert(END, "===== RESULTADO TOTAL =====\n")
    result_text.insert(END, f"Total antes: {total_before/1024:.2f} KB\n")
    result_text.insert(END, f"Total después: {total_after/1024:.2f} KB\n")
    result_text.insert(END, f"Ahorro total: {ahorro/1024:.2f} KB\n\n")

    result_text.insert(END, "===== DETALLE POR IMAGEN =====\n\n")

    for item in details:
        result_text.insert(END, item + "\n")

    status_label.config(text="Conversión finalizada ✅")


# ---------------- UI ----------------

root = Tk()
root.title("Convertidor a WebP")
root.geometry("600x600")

# Icono compatible Mac / Windows
if sys.platform.startswith("win"):
    root.iconbitmap("icon.ico")
else:
    if os.path.exists("icon.png"):
        icon = PhotoImage(file="icon.png")
        root.iconphoto(True, icon)

Label(root, text="Convertidor profesional a WebP").pack(pady=10)

same_folder_var = BooleanVar(value=True)
Checkbutton(root, text="Guardar en misma carpeta", variable=same_folder_var).pack()

Label(root, text="Tipo de compresión:").pack(pady=5)

compression_var = ttk.Combobox(
    root,
    values=["Recomendada (alta calidad)", "Máxima compresión"]
)
compression_var.current(0)
compression_var.pack()

Button(root, text="Elegir imágenes", command=convert_images).pack(pady=10)

progress = ttk.Progressbar(root, length=400)
progress.pack(pady=10)

status_label = Label(root, text="")
status_label.pack()

# Frame para scroll
frame = Frame(root)
frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

result_text = Text(frame, yscrollcommand=scrollbar.set)
result_text.pack(fill=BOTH, expand=True)

scrollbar.config(command=result_text.yview)

root.mainloop()