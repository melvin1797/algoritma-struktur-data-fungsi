usia = int(input("Masukkan usia Anda: "))

if usia >= 0 and usia <= 5:
    kategori = "Balita"
elif usia >= 6 and usia <= 12:
    kategori = "Anak-anak"
elif usia >= 13 and usia <= 17:
    kategori = "Remaja"
elif usia >= 18 and usia <= 59:
    kategori = "Dewasa"
else:
    kategori = "Lansia"

print("Kategori usia Anda adalah:", kategori)