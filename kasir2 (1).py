from audioop import reverse
from re import S
menuMakanan = ["Mie","Buah","Bumbu","Beras"]
menuMinuman=["Jus","Susu","Teh","Air"]
menuBarang=["Detergen","Sabun","Shampoo","Pasta gigi"]
hargaMakanan = ["25000", "50000", "15000", "50000"]
hargaMinuman = ["15000", "30000", "5000", "3000"]
hargaBarang = ["30000", "20000", "15000", "25000"]
semuaBarang = ["Mie", "Buah", "Bumbu", "Beras", "Jus", "Susu", "Teh", "Air", "Detergen", "Sabun", "Shampoo", "Pasta gigi"]
total=[]

#Searching
def pencarian():
    namaBarang = (input("Masukkan nama barang : "))
    find = False
    for i in range(0,len(semuaBarang)):
        if namaBarang == semuaBarang[i]:
            find = True
            break
    if find and namaBarang in menuMakanan:
        print("Barang tersedia di kategori makanan")
    elif find and namaBarang in menuMinuman:
        print("Barang tersedia di kategori minuman")
    elif find and namaBarang in menuBarang:
        print("Barang tersedia di kategori barang")
    else:
        print("%s tidak ada di daftar menu" %(namaBarang))
    menuutama()

#Menu_Utama
def menuutama():
    print("|==========================|")
    print("|      Selamat Datang      |")
    print("|==========================|")
    print("|      1. Pilih Menu       |")
    print("|      2. Melihat Pesanan  |")
    print("|      3. Pencarian        |")
    print("|      4. Urutkan Menu     |")
    print("|      5. Batal Pesanan    |")
    print("|      6. Ubah Pesanan     |")
    print("|      7. Checkout         |")
    print("|==========================|")
    kode = str(input(" Masukkan angka sesuai dengan menu yang tersedia [1-6]= "))
    if kode == "1":
        menuUtama()
    elif kode == "2":
        melihatpesanan()
    elif kode == "3":
        pencarian()
    elif kode == "4":
        urutkan()
    elif kode == "5":
        checkout()
    elif kode == "6":
        ubah()
    elif kode == "7":
        akhir()
    else:
        print("Kode yang anda masukkan salah")
        menuutama()

#Melihat_Pesanan
def melihatpesanan(): 
    pesanan()

def pesanan():
    pesan = (input("Apakah anda ingin menampilkan pesanan anda [ya/tidak]: "))
    if pesan == "ya" or "Ya":
        file = open("barang.txt", "r")
        content = file.read()
        print(content)
        file.close()
        menuutama()
    else:
        pesan == "tidak" or "Tidak"
        menuutama()

#Ubah pesanan
def ubah():
    file = open("barang.txt", "r")
    baca = file.read()
    baca = baca.replace(",", " ")
    print(baca)
    file.close()
    ubah1 = input("Apakah ingin mengubah pesanan ? [ya/tidak]: ")
    if ubah1 == "ya":
        nama = input("Nama Barang: ")
        jumlah = input("Jumlah Barang : ")
        total = input("Total : ")
        ubah2 = "Nama Barang: {}\n Jumlah Barang : {}\n Total : {}".format(nama, jumlah, total)
        file = open("barang.txt", "w")
        file.write(ubah2)
        file.close()
        menuutama()
        
#Sorting
def sorting(semuaBarang):
    return semuaBarang[1]

def urutkan():
    barang=(input("Masukkan angka yang tersedia [1. Dari barang ke makanan & minuman / 2. Dari makanan & minuman ke barang]: "))
    if barang == "1":
        semuaBarang.sort(key=sorting)
        print(semuaBarang)
    elif barang == "2":
        semuaBarang.sort(key=sorting, reverse=True)
        print(semuaBarang)
    menuutama()

#Daftar_Kategori_Barang-barang
def menuUtama():
    print("|---------------------------|")
    print("|         Menu Utama        |")
    print("|---------------------------|")
    print("|    1. Kategori Makanan    |")
    print("|    2. Kategori Minuman    |")
    print("|    3. Kategori Barang     |")
    print("|---------------------------|")
    kategori = str(input(" Masukkan angka sesuai dengan menu yang tersedia [1-3] = "))
    if kategori == "1":
        kategoriMakanan()
    elif kategori == "2":
        kategoriMinuman()
    elif kategori == "3":
        kategoriBarang()
    return(menuUtama)

#Daftar_Makanan
def kategoriMakanan():
    print("|---------------------------|")
    print("|  No  |  Barang  |  Harga  |")
    print("|------|----------|---------|")
    print("|  1.  |  Mie     |  25000  |")
    print("|  2.  |  Buah    |  50000  |")
    print("|  3.  |  Bumbu   |  15000  |")
    print("|  4.  |  Beras   |  50000  |")
    print("|---------------------------|")
    kode1 = str(input(" Masukkan nama sesuai dengan menu yang tersedia = "))
    if kode1 == "mie" or "Mie":        
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 25000 * jumlah1
        total.append(total1)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode1.center(8),  jumlah1 ,"====")
        tampilan1 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode1, jumlah1, total1)
        file = open("barang.txt", "a")
        file.write(tampilan1)
        file.close()
        menuutama()
    elif kode1 == "buah" or "Buah":
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 50000 * jumlah2
        total.append(total2)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====",kode1.center(8),  jumlah2 ,"====")
        tampilan2 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode1, jumlah2, total2)
        file = open("barang.txt", "a")
        file.write(tampilan2)
        file.close()
        menuutama()
    elif kode1 == "bumbu" or "Bumbu":
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 15000 * jumlah3 
        total.append(total3)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode1.center(8),  jumlah3 ,"====")
        tampilan3 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode1, jumlah3, total3)
        file = open("barang.txt", "a")
        file.write(tampilan3)
        menuutama()
    elif kode1 == "beras" or "Beras" :
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 50000 * jumlah4
        total.append(total4)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode1.center(8),  jumlah4 ,"====")
        tampilan4 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode1, jumlah4, total4)
        file = open("barang.txt", "a")
        file.write(tampilan4)
        file.close()
        menuutama()
    return(kategoriMakanan)

#Daftar_Minuman
def kategoriMinuman():
    print("|---------------------------|")
    print("|  No  |  Barang  |  Harga  |")
    print("|------|----------|---------|")
    print("|  1.  |  Jus     |  15000  |")
    print("|  2.  |  Susu    |  30000  |")
    print("|  3.  |  Teh     |  10000  |")
    print("|  4.  |  Air     |  8000   |")
    print("|---------------------------|")
    kode2 = str(input(" Masukkan nama sesuai dengan menu yang tersedia = "))
    if kode2 == "jus" or "Jus":        
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 15000 * jumlah1
        total.append(total1)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode2.center(8),  jumlah1 ,"====")
        tampilan1 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode2, jumlah1, total1)
        file = open("barang.txt", "a")
        file.write(tampilan1)
        file.close()
        menuutama()
    elif kode2 == "susu" or "Susu":
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 30000 * jumlah2
        total.append(total2)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode2.center(8),  jumlah2 ,"====")
        tampilan2 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode2, jumlah2, total2)
        file = open("barang.txt", "a")
        file.write(tampilan2)
        file.close()
        menuutama()
    elif kode2 == "teh" or "Teh":
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 10000 * jumlah3 
        total.append(total3)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode2.center(8),  jumlah3 ,"====")
        tampilan1 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode2, jumlah3, total3)
        file = open("barang.txt", "a")
        file.write(tampilan1)
        file.close()
        menuutama()
    elif kode2 == "air" or "Air":
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 8000 * jumlah4
        total.append(total4)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode2.center(8),  jumlah4 ,"====")
        tampilan1 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode2, jumlah4, total4)
        file = open("barang.txt", "a")
        file.write(tampilan1)
        file.close()
        menuutama()
    return(kategoriMinuman)

#Daftar_Barang
def kategoriBarang():
    print("|----------------------------|")    
    print("| No |    Barang     | Harga |")
    print("|----|---------------|-------|")
    print("| 1. | Detergen      | 30000 |")
    print("| 2. | Sabun         | 20000 |")
    print("| 3. | Shamppo       | 15000 |")
    print("| 4. | Pasta Gigi    | 25000 |")
    print("|----------------------------|")
    kode3 = str(input(" Masukkan nama sesuai dengan menu yang tersedia = "))
    if kode3 == "detergen" or "Detergen":        
        jumlah1 = int(input("Masukkan jumlah barang : "))
        total1 = 30000 * jumlah1
        total.append(total1)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode3.center(8),  jumlah1 ,"====")
        tampilan1 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode3, jumlah1, total1)
        file = open("barang.txt", "a")
        file.write(tampilan1)
        file.close()
        menuutama()
    elif kode3 == "sabun" or "Sabun":
        jumlah2 = int(input("Masukkan jumlah barang : "))
        total2 = 20000 * jumlah2
        total.append(total2)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode3.center(8),  jumlah2 ,"====")
        tampilan2 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode3, jumlah2, total2)
        file = open("barang.txt", "a")
        file.write(tampilan2)
        file.close()
        menuutama()
    elif kode3 == "shamppo" or "Shamppo":
        jumlah3 = int(input("Masukkan jumlah barang : "))
        total3 = 15000 * jumlah3 
        total.append(total3)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode3.center(8),  jumlah3 ,"====")
        tampilan3 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode3, jumlah3, total3)
        file = open("barang.txt", "a")
        file.write(tampilan3)
        file.close()
        menuutama()
    elif kode3 == "pasta gigi" or "Pasta gigi":
        jumlah4 = int(input("Masukkan jumlah barang : "))
        total4 = 25000 * jumlah4
        total.append(total4)
        print("====================")
        print("   Barang | Jumlah  ")
        print("====================")
        print( "====", kode3.center(8),  jumlah4 ,"====")
        tampilan4 = "\nNama Barang : {}, \nJumlah Barang : {}, \nTotal : {} \n".format(kode3, jumlah4, total4)
        file = open("barang.txt", "a")
        file.write(tampilan4)
        file.close()
        menuutama()
    return(kategoriBarang)

#Hapus pesanan
def checkout():
    checkout1 =(input("Apakah anda ingin membatalkan pesanan ? [ya/tidak] : "))
    if checkout1 == "ya" or "Ya":
        import os
        os.remove("barang.txt")
        total.clear()
        menuutama()
    elif checkout1 == "tidak" or "Tidak":
        menuutama()

#Struk
def akhir():  
    for harga in total:
        print("=====================================")
        print("===== J U M L A H     A K H I R =====")
        print("=====================================")   
        print("SubTotal         : ", sum(total))
        diskon = 0
        a = sum(total)
        if a > 500000:
            diskon = a * 8/100
        elif a > 300000:
            diskon = a * 5/100
        elif a > 200000:
            diskon = a * 3/100
        elif a > 100000:
            diskon = a * 1/100
        else:
            diskon = 0
        print("Potongan Harga   : ", diskon)
        totalakhir = a - diskon
        print("Total            : ", totalakhir)     
        print("-------------------------------------")
        print("-------------------------------------")
        bayar = int(input("Bayar            :  "))
        print("=====================================")
        print("=== S T R U K   P E M B E L I A N ===")
        print("=====================================")    
        kembalian = bayar - totalakhir
        file = open("barang.txt", "r")
        baca = file.read()
        baca = baca.replace(",", " ")
        print(baca)
        import datetime
        x = datetime.datetime.now()
        print(x.strftime("--- %A, %d %B %Y %X ---"))        
        print("Kembalian        : ", kembalian)
        print("-------------------------------------")
        print("============ Terima Kasih ===========")
        print("-------------------------------------")
        print("=====================================")
        break

menuutama()
