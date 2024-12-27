def main():
    print("=== Program Biodata ===")

    # Meminta input dari pengguna
    nama = input("Masukkan nama Anda: ")
    usia = input("Masukkan usia Anda: ")
    alamat = input("Masukkan alamat Anda: ")
    hobi = input("Masukkan hobi Anda: ")

    # Menampilkan informasi biodata
    print("\n=== Biodata Anda ===")
    print(f"Nama    : {nama}")
    print(f"Usia    : {usia} tahun")
    print(f"Alamat  : {alamat}")
    print(f"Hobi    : {hobi}")

if __name__ == "__main__":
    main()