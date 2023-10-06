import tkinter as tk

import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog


def generate_qr_code():
    ssid = ssid_entry.get()
    password = password_entry.get()
    security = security_var.get()

    if not ssid:
        result_label.config(text="Introduceți numele rețelei Wi-Fi", fg="red")
        return

    wifi_config = f"WIFI:S:{ssid};T:{security};"
    if security != "nopass":
        wifi_config += f"P:{password};"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Generarea și salvarea imaginii codului QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("wifi_qr.png")

    # Afișarea imaginii codului QR
    qr_image = Image.open("wifi_qr.png")
    qr_photo = ImageTk.PhotoImage(qr_image)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

    result_label.config(text="Codul QR a fost generat cu succes!", fg="green")


def save_qr_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        qr_image = Image.open("wifi_qr.png")
        qr_image.save(file_path)
        result_label.config(text=f"Imaginea QR a fost salvată în {file_path}", fg="blue")


# Crearea ferestrei principale
root = tk.Tk()
root.title("Generator QR pentru rețea Wi-Fi")

# Setare dimensiuni fereastra
root.geometry("400x400")

# Eticheta pentru nume rețea Wi-Fi
ssid_label = tk.Label(root, text="Nume rețea Wi-Fi:")
ssid_label.pack()

# Câmp pentru introducerea numelui rețelei Wi-Fi
ssid_entry = tk.Entry(root)
ssid_entry.pack()

# Eticheta pentru parolă
password_label = tk.Label(root, text="Parolă rețea Wi-Fi:")
password_label.pack()

# Câmp pentru introducerea parolei
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Opțiuni pentru tipul de securitate
security_var = tk.StringVar()
security_var.set("WPA2")

security_label = tk.Label(root, text="Tipul de securitate:")
security_label.pack()

security_option_menu = tk.OptionMenu(root, security_var, "WEP", "WPA", "WPA2", "nopass")
security_option_menu.pack()

# Buton pentru generarea codului QR
generate_button = tk.Button(root, text="Generați codul QR", command=generate_qr_code)
generate_button.pack()

# Buton pentru salvarea imaginii QR
save_button = tk.Button(root, text="Salvați imaginea QR", command=save_qr_image)
save_button.pack()

# Eticheta pentru afișarea rezultatului
result_label = tk.Label(root, text="", fg="black")
result_label.pack()

# Imaginea codului QR
qr_label = tk.Label(root)
qr_label.pack()

root.mainloop()
