def tambah(a, b):
  """Fungsi untuk menjumlahkan dua bilangan."""
  return a + b

def kurang(a, b):
  """Fungsi untuk mengurangkan dua bilangan."""
  return a - b

def kali(a, b):
  """Fungsi untuk mengalikan dua bilangan."""
  return a * b

def bagi(a, b):
  """Fungsi untuk membagi dua bilangan.

  Args:
    a: Pembilang.
    b: Penyebut.

  Returns:
    Hasil pembagian jika b tidak nol. Jika b adalah nol, maka akan mengembalikan pesan kesalahan.
  """
  if b == 0:
    return "Tidak dapat membagi dengan nol"
  else:
    return a / b

# Meminta pengguna memilih operasi
print("Pilih operasi:")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = int(input("Masukkan pilihan Anda (1/2/3/4): "))

# Meminta input angka dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Memanggil fungsi berdasarkan pilihan pengguna
if pilihan == 1:
  hasil = tambah(angka1, angka2)
elif pilihan == 2:
  hasil = kurang(angka1, angka2)
elif pilihan == 3:
  hasil = kali(angka1, angka2)
elif pilihan == 4:
  hasil = bagi(angka1, angka2)
else:
  print("Pilihan tidak valid")

# Menampilkan hasil
if isinstance(hasil, str):
  print(hasil)  # Jika hasil adalah string (pesan kesalahan), cetak langsung
else:
  print("Hasil:", hasil)