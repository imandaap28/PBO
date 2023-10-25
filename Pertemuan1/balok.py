''' Nama    : Imanda
    NIM     : 210511089
    Kelas   : TIF22B
'''

# Menghitung volume balok
panjang = float(input("Masukkan Panjang: "))  # Panjang balok
lebar = float(input("Masukkan Lebar: "))  # Lebar balok
tinggi = float(input("Masukkan Tinggi: "))  # Tinggi balok
volume = panjang * lebar * tinggi
print("Volume balok adalah:", volume)

# Menghitung luas permukaan balok
luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
print("Luas permukaan balok adalah:", luas_permukaan)