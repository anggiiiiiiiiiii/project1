#harus ada list
#harus ada looping
#harus ada function
#harus bisa dibaca, diupdate(hapus dan tambah)

daftar_kontak = [{"nama" : "Angga", "hubungan" : "pasangan", "nomor" : "0813-1322-4752"},
                 {"nama" : "Anggi", "hubungan" : "sahabat", "nomor" : "0488-9991-0808"},
                 {"nama" : "Anggira","hubungan": "saudara", "nomor" : "0902-2345-2222"}]

def menampilkan_kontak():
    print("\t------DAFTAR KONTAK------")
    print("No\t | Nama\t\t | Hubungan\t | Nomor Telepon")
    for i in range(len(daftar_kontak)):
        print(f"{(i)}\t | {daftar_kontak[i]["nama"]}\t | {daftar_kontak[i]["hubungan"]}\t | {daftar_kontak[i]["nomor"]}")
    print("\n")

def menambahkan_kontak():
    print("\t------MENAMBAH KONTAK------")
    nama = str(input("Masukan nama kontak: "))
    hubungan = str(input("Masukan hubungan dengan kontak: "))
    nomor = str(input("Masukan nomor kontak: "))
    daftar_kontak.append({"nama" : nama, "hubungan" : hubungan ,"nomor" : nomor})
    print("\n")

def mencari_kontak():
    print("\t------MENCARI KONTAK------")
    indeks = int(input("Masukan (nomor urutan) kontak yang ingin dicari: "))
    print(f"{daftar_kontak[indeks]["nama"]}\t |{daftar_kontak[indeks]["hubungan"]}\t| {daftar_kontak[indeks]["nomor"]} |")
    print("\n")

def menghapus_kontak():
    print("\t------MENGHAPUS KONTAK------")
    indeks1 = int(input("Masukan (nomor urutan) kontak yang ingin dihapus: "))
    del daftar_kontak[indeks1]
    print("\n")

while True:
    inputan = int(input("""-----Selamat Datang di Daftar Kontak-----\n1.Daftar Kontak\n2.Menambah Kontak\n3.Mencari Kontak\n4.Menghapus Kontak\n5.Selesai\n\nmasukan input(berupa angka): """))
    if (inputan == 5):
        break
    else:
        if (inputan == 1):
            menampilkan_kontak()
        elif (inputan == 2):
            menambahkan_kontak()
        elif (inputan == 3):
            mencari_kontak()
        elif (inputan == 4):
            menghapus_kontak()
        else:
            print("Masukan angka yang benar")