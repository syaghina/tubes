# Program cari tahun
# Program mencari gadget berdasarkan tahun

# Fungsi/Prosedur
def cari_tahun():
# I.S. belum ada input tahun untuk mencari gadget
# F.S. hasil pencarian telah ditemukan
    
# ALGORITMA
    # Membuka file dan memisahkan file menjadi baris
    f =  open("gadget.csv", "r")
    gadget = f.readlines()
    f.close()

    print(">>> CARI TAHUN <<<")
    print()
    tahun = int(input("Masukkan tahun: "))
    kategori = input("Masukkan kategori: ")
    print()
    print("Hasil pencarian:")
    print()

    # Menghilangkan tanda petik dan enter pada file
    old_lines = [raw_line.replace('"', "") for raw_line in gadget]
    lines = [raw_line.replace("\n", "") for raw_line in old_lines]

    # Mengkonversi baris pada list menjadi array
    data = []
    data_tahun = []
    data_kategori = ['<', '>', '>=', '<=', '=']
    for i in range(1, len(lines)):
        new_file = []
        kata = ''
        for j in (lines[i]):
            if (j == ";"):
                new_file.append(kata)
                kata = ''
            else:
                kata += j
        if kata:
            new_file.append(kata)
        array = [data.strip() for data in new_file]
        hasil = convertArray(array)
        data.append(hasil)
        # Membuat list berisi data tahun ditemukan
        data_tahun.append(hasil[5])

    # Memvalidasi input
    if (tahun > 999) & (kategori in data_kategori):
        if (kategori == '='):
            ind = data_tahun.index(tahun)
            print("Nama: ",data[ind][1])
            print("Deskripsi: ",data[ind][2])
            print("Jumlah: ",data[ind][3])
            print("Rarity: ",data[ind][4])
            print("Tahun Ditemukan: ",data[ind][5])
        elif (kategori == '<'):
            for item in data_tahun:
                if item < tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '>'):
            for item in data_tahun:
                if item > tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '<='):
            for item in data_tahun:
                if item <= tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
        elif (kategori == '>='):
            for item in data_tahun:
                if item >= tahun:
                    ind = data_tahun.index(item)
                    print("Nama: ",data[ind][1])
                    print("Deskripsi: ",data[ind][2])
                    print("Jumlah: ",data[ind][3])
                    print("Rarity: ",data[ind][4])
                    print("Tahun Ditemukan: ",data[ind][5])
                    print()
    else:
        print("Tidak ada gadget yang ditemukan")

# Fungsi/Prosedur
def convertArray(array):
# Fungsi untuk mengkonversi array menjadi value sebenarnya
    
# ALGORITMA FUNGSI
    arr = array[:]
    for i in range(6):
        # Untuk kolom tahun ditemukan (indeks ke-5) value sebenarnya adalah integer, bukan string
        if(i == 5):
            arr[i] = int(arr[i])
    return(arr)
