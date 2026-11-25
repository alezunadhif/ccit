# =====================================================
# LATIHAN 13A: Scope: Lokal & Global
# Tetap berhubungan: Login + Data Mahasiswa (dict)
# =====================================================

# ========== VARIABEL GLOBAL ==========
# Dibuat di LUAR semua fungsi, bisa dibaca di mana saja
INSTITUSI = "Kampus Python"
total_akses = 0


def login():
    """Login: semua variabel di sini BERSIFAT LOKAL."""
    username_benar = "nadhif"      # LOKAL
    password_benar = "nadhif123"   # LOKAL
    attempt = 3                    # LOKAL

    print("=== SISTEM LOGIN ===")
    print(f"Selamat datang di {INSTITUSI}")  # membaca GLOBAL (diizinkan)

    while attempt > 0:
        username = input("Username: ")
        password = input("Password: ")

        if username == username_benar and password == password_benar:
            print("\nLogin berhasil!\n")
            return True
        else:
            attempt -= 1
            if attempt > 0:
                print(f"Login gagal! Sisa: {attempt}\n")
            else:
                print("\nAkses ditolak.")
                return False


def catat_akses():
    """Mengubah variabel GLOBAL memakai keyword global."""
    global total_akses
    total_akses = total_akses + 1
    print(f"[Global] total_akses sekarang = {total_akses}")


def hitung_grade(uts, uas, tugas):
    # rata, grade, predikat, status bersifat LOKAL di fungsi ini
    rata = round((uts * 0.30) + (uas * 0.40) + (tugas * 0.30), 2)
    if rata >= 85:
        return rata, "A", "Sangat Baik", "LULUS"
    elif rata >= 70:
        return rata, "B", "Baik", "LULUS"
    elif rata >= 55:
        return rata, "C", "Cukup", "LULUS"
    elif rata >= 40:
        return rata, "D", "Kurang", "TIDAK LULUS"
    else:
        return rata, "E", "Sangat Kurang", "TIDAK LULUS"


def tampil_detail(mhs):
    rata, grade, predikat, status = hitung_grade(mhs["uts"], mhs["uas"], mhs["tugas"])
    print(f"\nNama      : {mhs['nama']}")
    print(f"Kelas     : {mhs['kelas']}")
    print(f"UTS       : {mhs['uts']}")
    print(f"UAS       : {mhs['uas']}")
    print(f"Tugas     : {mhs['tugas']}")
    print(f"Rata-rata : {rata}")
    print(f"Grade     : {grade} | {predikat} | {status}")


def demo_scope():
    print("\n" + "=" * 50)
    print("           DEMO SCOPE: LOKAL vs GLOBAL")
    print("=" * 50)

    # 1. Variabel LOKAL
    print("\n[1] Variabel LOKAL")
    pesan = "Saya hanya hidup di dalam demo_scope()"  # LOKAL
    print("  Di dalam fungsi:", pesan)
    print("  (Jika dipanggil dari luar fungsi -> NameError)")

    # 2. Membaca GLOBAL
    print("\n[2] Membaca variabel GLOBAL")
    print(f"  INSTITUSI (global)   = {INSTITUSI}")
    print(f"  total_akses (global) = {total_akses}")
    print("  -> Membaca global dari dalam fungsi: BOLEH")

    # 3. Mengubah GLOBAL tanpa keyword global
    print("\n[3] Mengubah global TANPA keyword global")
    print("  Jika menulis: total_akses = total_akses + 1")
    print("  Python menganggap total_akses sebagai LOKAL baru")
    print("  -> sering muncul UnboundLocalError atau tidak mengubah global")

    # 4. Mengubah GLOBAL dengan keyword global
    print("\n[4] Mengubah global DENGAN keyword global")
    catat_akses()
    print(f"  Setelah catat_akses(), total_akses = {total_akses}")

    # 5. Praktik baik: parameter + return
    print("\n[5] Praktik baik: parameter + return")

    def tambah_poin(nilai, bonus):
        hasil = nilai + bonus
        return hasil

    uts_lama = 80
    uts_baru = tambah_poin(uts_lama, 5)
    print(f"  uts_lama={uts_lama}, setelah bonus={uts_baru}")
    print("  -> Data dikirim lewat parameter, hasil lewat return")
    print("  -> Tidak perlu mengubah variabel global")
    print("\n" + "=" * 50)


def lihat_semua(data):
    if not data:
        print("Data kosong.")
        return
    for i, mhs in enumerate(data):
        print(f"\n--- [{i}] ---")
        tampil_detail(mhs)


def main():
    if not login():
        return

    data_mahasiswa = [
        {"nama": "Budi", "kelas": "3CS1", "uts": 80, "uas": 85, "tugas": 90},
        {"nama": "Andi", "kelas": "3CS1", "uts": 70, "uas": 75, "tugas": 80},
    ]

    catat_akses()  # akses tercatat pertama kali setelah login sukses

    while True:
        print("\n===== MENU L13A (SCOPE) =====")
        print(f"Institusi: {INSTITUSI}")
        print(f"Total akses dicatat: {total_akses}")
        print(f"Jumlah data: {len(data_mahasiswa)}")
        print("1. Lihat semua data mahasiswa")
        print("2. Demo scope lokal & global")
        print("3. Catat akses lagi (ubah global)")
        print("0. Keluar")

        pilih = input("Pilihan: ")
        if pilih == "1":
            lihat_semua(data_mahasiswa)
        elif pilih == "2":
            demo_scope()
        elif pilih == "3":
            catat_akses()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()