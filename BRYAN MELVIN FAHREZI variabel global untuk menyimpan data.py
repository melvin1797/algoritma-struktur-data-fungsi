buku = []

def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    print("Buku Sudah ditambakan")

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID Buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

def delete_data():
    show_data()
    indeks = int(input("Inputkan ID Buku: "))
    if indeks > len(buku):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

def show_menu():
    print("\n")
    print("---------Menu---------")
    print("[1] Show data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")

    menu = input("PILIH MENU> ")
    print("\n")

    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        delete_data()
    elif int(menu) == 5:
        exit()
    else:
        print("Salah Pilih")

if __name__ == "__main__":
    while True:
        show_menu()