def cetak_pola(baris):
  """Mencetak pola segitiga bintang dengan jumlah baris yang ditentukan.

  Args:
    baris: Jumlah baris segitiga.
  """

  for i in range(baris):
    for j in range(i+1):
      print("*", end="")
    print()

# Meminta input pengguna
jumlah_baris = int(input("Masukkan jumlah baris segitiga: "))

# Memanggil fungsi untuk mencetak pola
cetak_pola(jumlah_baris)