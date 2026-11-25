# LATIHAN 10C - List CRUD (Tambah, Lihat, Cari, Edit, Hapus)
# =====================================================

# LOGIN
username_benar = "nadhif"  # ganti
password_benar = "nadhif123"  # ganti

attempt = 3
login_berhasil = False

print("=== SISTEM LOGIN ===")

while attempt > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == username_benar and password == password_benar:
        print("\nLogin berhasil!\n")
        login_berhasil = True
        break
    else:
        attempt -= 1
        if attempt > 0:
            print(f"Login gagal! Sisa: {attempt}\n")
        else:
            print("\nAkses ditolak. Gagal 3 kali.")

if login_berhasil:
    list_nama = ["Budi", "Andi"]
    list_kelas = ["3CS1", "3CS1"]
    list_uts = [80.0, 70.0]
    list_uas = [85.0, 75.0]
    list_tugas = [90.0, 80.0]

    def tampil_detail(i):
        rata = round(
            (list_uts[i] * 0.30)
            + (list_uas[i] * 0.40)
            + (list_tugas[i] * 0.30),
            2,
        )

        if rata >= 85:
            grade, predikat, status = "A", "Sangat Baik", "LULUS"
        elif rata >= 70:
            grade, predikat, status = "B", "Baik", "LULUS"
        elif rata >= 55:
            grade, predikat, status = "C", "Cukup", "LULUS"
        elif rata >= 40:
            grade, predikat, status = "D", "Kurang", "TIDAK LULUS"
        else:
            grade, predikat, status = "E", "Sangat Kurang", "TIDAK LULUS"

        print(f"\nNama      : {list_nama[i]}")
        print(f"Kelas     : {list_kelas[i]}")
        print(f"UTS       : {list_uts[i]}")
        print(f"UAS       : {list_uas[i]}")
        print(f"Tugas     : {list_tugas[i]}")
        print(f"Rata-rata : {rata}")
        print(f"Grade     : {grade}")
        print(f"Predikat  : {predikat}")
        print(f"Status    : {status}")

    def input_data_baru():
        while True:
            print("\n--- INPUT DATA MAHASISWA BARU ---")
            nama = input("Nama: ")
            kelas = input("Kelas: ")

            uts = float(input("UTS (0-100): "))
            while uts < 0 or uts > 100:
                print(" [!] 0-100 saja.")
                uts = float(input("UTS (0-100): "))

            uas = float(input("UAS (0-100): "))
            while uas < 0 or uas > 100:
                print(" [!] 0-100 saja.")
                uas = float(input("UAS (0-100): "))

            tugas = float(input("Tugas (0-100): "))
            while tugas < 0 or tugas > 100:
                print(" [!] 0-100 saja.")
                tugas = float(input("Tugas (0-100): "))

            list_nama.append(nama)
            list_kelas.append(kelas)
            list_uts.append(uts)
            list_uas.append(uas)
            list_tugas.append(tugas)

            idx = len(list_nama) - 1
            print(f"\n[v] Data masuk di indeks ke-{idx}")
            print(f"Total data: {len(list_nama)}")

            if input("\nLanjut input? (y/n): ").lower() != "y":
                print("Kembali ke menu utama...")
                break

    def edit_data():
        if len(list_nama) == 0:
            print("List masih kosong.")
            return

        print("\n--- EDIT DATA ---")
        print("1. Berdasarkan indeks")
        print("2. Berdasarkan nama")
        cara = input("Pilih cara: ")
        i = None

        if cara == "1":
            print(f"Indeks: 0 s/d {len(list_nama) - 1}")
            idx = int(input("Indeks: "))
            if 0 <= idx < len(list_nama):
                i = idx
            else:
                print("Indeks tidak valid!")
                return
        elif cara == "2":
            cari = input("Nama: ")
            if cari in list_nama:
                i = list_nama.index(cari)
            else:
                print(f"'{cari}' tidak ditemukan.")
                return
        else:
            print("Pilihan tidak valid.")
            return

        print("\nData saat ini:")
        tampil_detail(i)

        print("\nMasukkan data baru:")
        nama = input("Nama: ")
        kelas = input("Kelas: ")

        uts = float(input("UTS (0-100): "))
        while uts < 0 or uts > 100:
            print(" [!] 0-100 saja.")
            uts = float(input("UTS (0-100): "))

        uas = float(input("UAS (0-100): "))
        while uas < 0 or uas > 100:
            print(" [!] 0-100 saja.")
            uas = float(input("UAS (0-100): "))

        tugas = float(input("Tugas (0-100): "))
        while tugas < 0 or tugas > 100:
            print(" [!] 0-100 saja.")
            tugas = float(input("Tugas (0-100): "))

        list_nama[i] = nama
        list_kelas[i] = kelas
        list_uts[i] = uts
        list_uas[i] = uas
        list_tugas[i] = tugas

        print(f"\n[v] Data Indeks ke-{i} berhasil diubah.")
        tampil_detail(i)

    def hapus_data():
        if len(list_nama) == 0:
            print("List masih kosong.")
            return

        print("\n--- HAPUS DATA ---")
        print("1. Berdasarkan indeks")
        print("2. Berdasarkan nama")
        cara = input("Pilih cara: ")
        i = None

        if cara == "1":
            print(f"Indeks: 0 s/d {len(list_nama) - 1}")
            idx = int(input("Indeks: "))
            if 0 <= idx < len(list_nama):
                i = idx
            else:
                print("Indeks tidak valid!")
                return
        elif cara == "2":
            cari = input("Nama: ")
            if cari in list_nama:
                i = list_nama.index(cari)
            else:
                print(f"'{cari}' tidak ditemukan.")
                return
        else:
            print("Pilihan tidak valid.")
            return

        print("\nData yang akan dihapus:")
        tampil_detail(i)

        if input("\nYakin hapus? (y/n): ").lower() == "y":
            list_nama.pop(i)
            list_kelas.pop(i)
            list_uts.pop(i)
            list_uas.pop(i)
            list_tugas.pop(i)
            print("\n[v] Data berhasil dihapus.")
            print(f"Sisa data: {len(list_nama)}")
        else:
            print("Penghapusan dibatalkan.")

    # MENU UTAMA
    while True:
        print("\n==== MENU UTAMA ====")
        print(f"Jumlah data: {len(list_nama)}")
        print("1. Lihat data berdasarkan indeks")
        print("2. Cari data berdasarkan nama")
        print("3. Lihat data pertama & terakhir")
        print("4. Masukkan data baru")
        print("5. Edit data")
        print("6. Hapus data")
        print("0. Keluar")

        pilih = input("Pilihan: ")

        if pilih == "1":
            if len(list_nama) == 0:
                print("List masih kosong.")
            else:
                print(f"Indeks: 0 s/d {len(list_nama) - 1}")
                idx = int(input("Indeks: "))
                if 0 <= idx < len(list_nama):
                    tampil_detail(idx)
                else:
                    print("Indeks tidak valid!")

        elif pilih == "2":
            if len(list_nama) == 0:
                print("List masih kosong.")
            else:
                cari = input("Nama: ")
                if cari in list_nama:
                    i = list_nama.index(cari)
                    print(f"Ditemukan di indeks ke-{i}")
                    tampil_detail(i)
                else:
                    print(f"'{cari}' tidak ditemukan.")

        elif pilih == "3":
            if len(list_nama) == 0:
                print("List masih kosong.")
            else:
                print("\n--- Data Pertama ---")
                tampil_detail(0)
                print("\n--- Data Terakhir ---")
                tampil_detail(-1)

        elif pilih == "4":
            input_data_baru()

        elif pilih == "5":
            edit_data()

        elif pilih == "6":
            hapus_data()

        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")