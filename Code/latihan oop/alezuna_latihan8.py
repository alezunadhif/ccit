# =====================================================
# LATIHAN 8 - Login + Multi Mahasiswa + Validasi + Grade
# =====================================================

username_benar = "nadhif"
password_benar = "0666"

attempt = 3
login_berhasil = False

print("=== SISTEM LOGIN ===")

while attempt > 0:
    username = input("Username: ")
    password = input("Password: ")

    if username == username_benar and password == password_benar:
        print("\nLogin berhasil! Selamat datang.\n")
        login_berhasil = True
        break
    else:
        attempt -= 1
        if attempt > 0:
            print(f"Login gagal! Sisa percobaan: {attempt}\n")
        else:
            print("\nAnda telah gagal login 3 kali. Akses ditolak.")

if login_berhasil:
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    print()

    for i in range(1, jumlah + 1):
        print(f"--- Data Mahasiswa ke-{i} ---")
        nama = input("Nama mahasiswa: ")

        # Validasi UTS
        uts = float(input("Nilai UTS (0-100): "))
        while uts < 0 or uts > 100:
            print(" [!] Nilai harus antara 0-100. Coba lagi.")
            uts = float(input("Nilai UTS (0-100): "))

        # Validasi UAS
        uas = float(input("Nilai UAS (0-100): "))
        while uas < 0 or uas > 100:
            print(" [!] Nilai harus antara 0-100. Coba lagi.")
            uas = float(input("Nilai UAS (0-100): "))

        # Validasi Tugas
        tugas = float(input("Nilai Tugas (0-100): "))
        while tugas < 0 or tugas > 100:
            print(" [!] Nilai harus antara 0-100. Coba lagi.")
            tugas = float(input("Nilai Tugas (0-100): "))

        # Hitung rata-rata tertimbang
        rata_rata = (uts * 0.30) + (uas * 0.40) + (tugas * 0.30)
        rata_rata = round(rata_rata, 2)

        # Tentukan grade, predikat, status
        if rata_rata >= 85:
            grade, predikat, status = "A", "Sangat Baik", "LULUS"
        elif rata_rata >= 70:
            grade, predikat, status = "B", "Baik", "LULUS"
        elif rata_rata >= 55:
            grade, predikat, status = "C", "Cukup", "LULUS"
        elif rata_rata >= 40:
            grade, predikat, status = "D", "Kurang", "TIDAK LULUS"
        else:
            grade, predikat, status = "E", "Sangat Kurang", "TIDAK LULUS"

        # Tampilkan hasil
        print("\n=== HASIL PENILAIAN ===")
        print(f"Nama      : {nama}")
        print(f"UTS       : {uts}")
        print(f"UAS       : {uas}")
        print(f"Tugas     : {tugas}")
        print(f"Rata-rata : {rata_rata}")
        print(f"Grade     : {grade}")
        print(f"Predikat  : {predikat}")
        print(f"Status    : {status}")
        print("-" * 28 + "\n")