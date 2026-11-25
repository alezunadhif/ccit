# =====================================================
# LATIHAN 13 - Fungsi (Function) di Python
# Login + Function untuk setiap operasi data
# =====================================================

# --- LOGIN (fungsi) ---
def login():
    username_benar = "nadhif"  # Ganti
    password_benar = "nadhif123"  # Ganti
    attempt = 3

    print("=== SISTEM LOGIN ===")
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
                print("\nAkses ditolak. Gagal 3 kali.")
                return False


# --- HITUNG GRADE (return banyak nilai / tuple)
def hitung_grade(uts, uas, tugas):
    """Hitung rata-rata tertimbang dan tentukan grade."""
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


# --- TAMPIL DETAIL (parameter: dict)
def tampil_detail(mhs):
    rata, grade, predikat, status = hitung_grade(mhs["uts"], mhs["uas"], mhs["tugas"])
    print(f"\nNama      : {mhs['nama']}")
    print(f"Kelas     : {mhs['kelas']}")
    print(f"UTS       : {mhs['uts']}")
    print(f"UAS       : {mhs['uas']}")
    print(f"Tugas     : {mhs['tugas']}")
    print(f"Rata-rata : {rata}")
    print(f"Grade     : {grade}")
    print(f"Predikat  : {predikat}")
    print(f"Status    : {status}")


# --- VALIDASI NILAI (default argument)
def input_nilai(label, min_val=0, max_val=100):
    """Minta input angka dengan validasi rentang. Default 0-100."""
    nilai = float(input(f"{label} ({min_val}-{max_val}): "))
    while nilai < min_val or nilai > max_val:
        print(f" [!] Nilai harus {min_val}-{max_val}.")
        nilai = float(input(f"{label} ({min_val}-{max_val}): "))
    return nilai


# --- CARI INDEKS BY NAMA
def cari_indeks(data, nama):
    for i, mhs in enumerate(data):
        if mhs["nama"].lower() == nama.lower():
            return i
    return -1


# --- INFO FUNGSI (tanpa parameter & tanpa return)
def info_fungsi():
    print("\n" + "=" * 50)
    print("               INFORMASI FUNGSI")
    print("=" * 50)
    print("""
Fungsi: blok kode yang punya nama, bisa dipanggil berulang.
Sintaks dasar:
def nama_fungsi(parameter):
    # isi fungsi
    return nilai  # opsional

Manfaat:
1. Menghindari kode berulang (DRY - Don't Repeat Yourself)
2. Memecah program jadi bagian kecil (modular)
3. Mudah diuji dan diperbaiki

Jenis di latihan ini:
- Tanpa parameter / tanpa return -> info_fungsi()
- Dengan parameter               -> tampil_detail(mhs)
- Dengan return                  -> login(), cari_indeks(...)
- Default argument               -> input_nilai(label, min_val=0, max_val=100)
- Return banyak nilai            -> hitung_grade(...)
""")
    print("=" * 50)


# --- OPERASI CRUD
def lihat_semua(data):
    if not data:
        print("Data masih kosong.")
        return
    for i, mhs in enumerate(data):
        print(f"\n--- [{i}] ---")
        tampil_detail(mhs)


def cari_data(data):
    nama = input("Nama: ")
    i = cari_indeks(data, nama)
    if i != -1:
        print(f"Ditemukan di indeks ke-{i}")
        tampil_detail(data[i])
    else:
        print("Tidak ditemukan.")


def tambah_data(data):
    while True:
        print("\n--- INPUT DATA BARU ---")
        nama = input("Nama  : ")
        kelas = input("Kelas : ")
        uts = input_nilai("UTS")
        uas = input_nilai("UAS")
        tugas = input_nilai("Tugas")

        data.append({
            "nama": nama, "kelas": kelas,
            "uts": uts, "uas": uas, "tugas": tugas
        })
        print(f"\n[v] Ditambahkan. Total: {len(data)}")

        if input("\nLanjut input? (y/n): ").lower() != "y":
            break


def edit_data(data):
    if not data:
        print("Data masih kosong.")
        return
    nama = input("Nama yang akan diedit: ")
    i = cari_indeks(data, nama)
    if i == -1:
        print("Tidak ditemukan.")
        return

    print("\nData saat ini:")
    tampil_detail(data[i])

    print("\nMasukkan data baru:")
    data[i]["nama"] = input("Nama  : ")
    data[i]["kelas"] = input("Kelas : ")
    data[i]["uts"] = input_nilai("UTS")
    data[i]["uas"] = input_nilai("UAS")
    data[i]["tugas"] = input_nilai("Tugas")

    print("\n[v] Berhasil diubah.")
    tampil_detail(data[i])


def hapus_data(data):
    if not data:
        print("Data masih kosong.")
        return
    nama = input("Nama yang akan dihapus: ")
    i = cari_indeks(data, nama)
    if i == -1:
        print("Tidak ditemukan.")
        return

    print("\nData yang akan dihapus:")
    tampil_detail(data[i])

    if input("\nYakin hapus? (y/n): ").lower() == "y":
        data.pop(i)
        print(f"\n[v] Dihapus. Sisa: {len(data)}")
    else:
        print("Dibatalkan.")


# --- PROGRAM UTAMA
def main():
    if not login():
        return

    data_mahasiswa = [
        {"nama": "Budi", "kelas": "3CS1", "uts": 80.0, "uas": 85.0, "tugas": 90.0},
        {"nama": "Andi", "kelas": "3CS1", "uts": 70.0, "uas": 75.0, "tugas": 80.0},
        {"nama": "Siti", "kelas": "3CS2", "uts": 90.0, "uas": 95.0, "tugas": 85.0},
    ]

    while True:
        print("\n===== MENU FUNGSI =====")
        print(f"Jumlah data: {len(data_mahasiswa)}")
        print("1. Lihat semua data")
        print("2. Cari berdasarkan nama")
        print("3. Tambah data")
        print("4. Edit data")
        print("5. Hapus data")
        print("6. Informasi Fungsi")
        print("0. Keluar")

        pilih = input("Pilihan: ")
        if pilih == "1":
            lihat_semua(data_mahasiswa)
        elif pilih == "2":
            cari_data(data_mahasiswa)
        elif pilih == "3":
            tambah_data(data_mahasiswa)
        elif pilih == "4":
            edit_data(data_mahasiswa)
        elif pilih == "5":
            hapus_data(data_mahasiswa)
        elif pilih == "6":
            info_fungsi()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


# Panggil fungsi utama sebagai entry point
main()