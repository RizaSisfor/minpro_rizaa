print("_______________________________")
print("_____DASAR DASAR PEMOGRAMAN____")
print("_______Mini Project Satu_______")
print("_________Ahmad Sepriza_________")
print("__________2409116025___________")
print("_______________________________")

# Proses Login
while True:
    print("\n====== LOGIN ====== \n")
    print("MASUKKAN NAMA DAN NIM") 
    NAMA = str(input("Masukkan Nama : "))
    NIM = str(input("Masukkan Akhiran NIM Anda : "))
    if NAMA =="Riza" and NIM == "025":
        print("Selamat Datang",NAMA,", " + NIM)
        break
    else:
        pilihan = input("Ulangi Login? (y/n): \n=>")
        if pilihan != "y":
            print("Login Gagal")
            exit("Coba Lagi \n")
            
# Proses Perhitungan Gaji
while True:    
    jam_kerja = int (input("\nMasukkan Jam Kerja : "))
    gaji_per_jam = int(input ("Masukkan Nominal Gaji Per Jam : Rp. "))

    # Hitung Gaji
    gaji_total = jam_kerja * gaji_per_jam
    if jam_kerja > 160:
        bonus = 0.1 * gaji_total
        total_dengan_bonus = gaji_total + bonus
        print(f"Total Gaji dengan Bonus : Rp. {total_dengan_bonus:}")
    else:
        print(f"Total Gaji tanpa Bonus : Rp. {gaji_total:}")

    ulang = input("Ingin Menghitung Ulang Total Gaji? (Yes/No): \n=> ")
    if ulang != "Yes":
        print("\nTerima Kasih Telah Menggunakan Program Ini \n")
        break