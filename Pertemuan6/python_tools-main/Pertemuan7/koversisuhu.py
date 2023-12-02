import tkinter as tk
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

# Membuat jendela aplikasi
app = tk.Tk()
app.title("Konversi Suhu")

# Menambahkan label untuk input suhu
label_input = tk.Label(app, text="Masukkan Suhu (Celsius):")
label_input.pack()

# Menambahkan elemen input
entry_input = tk.Entry(app)
entry_input.pack()

# Menambahkan label untuk hasil konversi
label_result = tk.Label(app, text="Hasil Konversi:")
label_result.pack()

# Menambahkan elemen output
entry_result = tk.Entry(app, state='readonly')
entry_result.pack()

# Fungsi konversi suhu
def convert_temperature():
    celsius = float(entry_input.get())
    fahrenheit = (celsius * 9/5) + 32
    entry_result.config(state='normal')
    entry_result.delete(0, tk.END)
    entry_result.insert(0, f"{fahrenheit:.2f} Fahrenheit")
    entry_result.config(state='readonly')

# Tombol konversi
btn_convert = tk.Button(app, text="Konversi", command=convert_temperature)
btn_convert.pack()

# Menjalankan aplikasi
app.mainloop()