#fungsi garis
def garis1():
    print ("=======================================")

def garis2():
    print ("=======================================")

# perpus Kosong untuk menyimpan Buku
buku = []

#fungsi show buku ( perlihatkan buku)
def show_buku():
    garis1()
    if len(buku) <= 0:
        print("Buku Kosong maz!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print("[{}] {}".format (indeks,buku [indeks]))
            garis1()

#fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("Inputan ID buku : "))
    if indeks > len(buku):
        print("ID salah")
        garis2()
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru 
        garis2()
        print("Buku berhasil di rubah!")
        show_buku()
        garis1()

#fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)
    garis2()
    print ("Buku Berhasil Di tambah!")
    garis1()
#fungsi delete buku
def delete_buku():
    show_buku()
    indeks = int(input("Inputkan ID buku :"))
    if indeks > len(buku):
        print ("ID Salah")
    else:
        buku.remove(buku[indeks])
        garis1()
        print ("Buku berhasil Di hapus! ")
        garis2()


#menu untuk tampilan perpustakaan
def show_menu():
    print("\n")
    print("--Selamat Datang Di Perpus--")
    print("1.show buku")
    print("2.insert Buku")
    print("3.edit Buku")
    print("4.delete Buku")
    print("5.Keluar")

    menu = int(input("Pilih Menu : >"))
    
       
    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print("Upsss Salah")

#tampilkan menu
if __name__ == "__main__":
    while True:
        show_menu()


