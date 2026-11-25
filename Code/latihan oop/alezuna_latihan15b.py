# =========================================================
# MODUL PRAKTIKUM PYTHON - LATIHAN 15B
# Login (L15A) + CRUD Mahasiswa dengan Menu Bertingkat
# =========================================================

import os

LOGIN_FILE = "login15b.txt"
MAHASISWA_FILE = "mahasiswa.txt"
current_user = None

# ==================== BAGIAN LOGIN ====================

def buat_file_login_default():
    if not os.path.exists(LOGIN_FILE):
        with open(LOGIN_FILE, "w") as f:
            f.write("admin:adminjuga\n")
            f.write("tri:333\n")
        print(">> File login.txt berhasil dibuat.")
        print("   1. admin / adminjuga")
        print("   2. tri / 333")


def load_akun():
    akun = {}
    try:
        with open(LOGIN_FILE, "r") as f:
            for baris in f:
                baris = baris.strip()
                if baris and ":" in baris:
                    username, password = baris.split(":", 1)
                    akun[username] = password
    except FileNotFoundError:
        buat_file_login_default()
        return load_akun()
    except Exception as e:
        print(f"Error baca login: {e}")
    return akun


def simpan_akun(akun):
    with open(LOGIN_FILE, "w") as f:
        for username, password in akun.items():
            f.write(f"{username}:{password}\n")


def proses_login():
    global current_user
    akun = load_akun()
    print("\n----- FORM LOGIN -----")
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    if username in akun and akun[username] == password:
        current_user = username
        print(f"\nLogin berhasil! Selamat datang, {username}")
        menu_utama()
    else:
        print("\nUsername atau password salah!")
        current_user = None


def menu_create_akun():
    while True:
        print("\n===== CREATE AKUN =====")
        print("1. Input Username dan Password")
        print("2. Lihat Daftar Akun")
        print("3. Kembali ke Menu Login")
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_akun()
        elif pilihan == "2":
            lihat_daftar_akun()
        elif pilihan == "3":
            print("Kembali ke Menu Login...")
            break
        else:
            print("Pilihan tidak valid!")


def tambah_akun():
    akun = load_akun()
    print("\n--- TAMBAH AKUN BARU ---")
    username = input("Username baru : ").strip()
    password = input("Password baru : ").strip()

    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return

    if username in akun:
        print(f"Username '{username}' sudah terdaftar!")
        return

    with open(LOGIN_FILE, "a") as f:
        f.write(f"{username}:{password}\n")
    print(f"Akun '{username}' berhasil ditambahkan!")


def lihat_daftar_akun():
    akun = load_akun()
    print("\n--- DAFTAR AKUN TERDAFTAR ---")
    if not akun:
        print("Belum ada akun terdaftar.")
    else:
        for i, username in enumerate(akun.keys(), 1):
            print(f"{i}. {username}")
        print("-" * 30)
        print(f"Total akun: {len(akun)}")


def edit_password():
    global current_user
    if current_user is None:
        print("Anda belum login!")
        return

    akun = load_akun()
    print("\n===== EDIT PASSWORD =====")
    print(f"Username Anda : {current_user}")

    password_lama = input("Masukkan password lama        : ").strip()
    password_baru = input("Masukkan password baru        : ").strip()
    konfirmasi = input("Konfirmasi password baru      : ").strip()

    if akun.get(current_user) != password_lama:
        print("Password lama salah!")
        return

    if not password_baru:
        print("Password baru tidak boleh kosong!")
        return

    if password_baru != konfirmasi:
        print("Konfirmasi password baru tidak cocok!")
        return

    akun[current_user] = password_baru
    simpan_akun(akun)
    print("Password berhasil diubah!")


# ==================== BAGIAN MAHASISWA ====================

def buat_file_mahasiswa_default():
    if not os.path.exists(MAHASISWA_FILE):
        with open(MAHASISWA_FILE, "w") as f:
            f.write("1234567890:Budi Santoso:Informatika:85\n")
            f.write("1234567891:Ani Wijaya:Sistem Informasi:90\n")
        print(">> File mahasiswa.txt berhasil dibuat dengan 2 data contoh.")


def load_mahasiswa():
    data = []
    try:
        with open(MAHASISWA_FILE, "r") as f:
            for baris in f:
                baris = baris.strip()
                if baris and baris.count(":") >= 3:
                    bagian = baris.split(":")
                    nim = bagian[0]
                    nilai = bagian[-1]
                    jurusan = bagian[-2]
                    nama = ":".join(bagian[1:-2])
                    data.append({
                        "nim": nim,
                        "nama": nama,
                        "jurusan": jurusan,
                        "nilai": nilai
                    })
    except FileNotFoundError:
        buat_file_mahasiswa_default()
        return load_mahasiswa()
    except Exception as e:
        print(f"Error baca mahasiswa: {e}")
    return data


def simpan_mahasiswa(data):
    with open(MAHASISWA_FILE, "w") as f:
        for m in data:
            f.write(f"{m['nim']}:{m['nama']}:{m['jurusan']}:{m['nilai']}\n")


def lihat_semua_mahasiswa():
    data = load_mahasiswa()
    print("\n===== DAFTAR SEMUA MAHASISWA =====")
    if not data:
        print("Belum ada data mahasiswa.")
        return

    print(f"{'No':<4} {'NIM':<14} {'Nama':<22} {'Jurusan':<20} {'Nilai':<6}")
    print("-" * 70)
    for i, m in enumerate(data, 1):
        print(f"{i:<4} {m['nim']:<14} {m['nama']:<22} {m['jurusan']:<20} {m['nilai']:<6}")
    print("-" * 70)
    print(f"Total data: {len(data)}")


def cari_mahasiswa():
    data = load_mahasiswa()
    print("\n--- CARI MAHASISWA ---")
    keyword = input("Masukkan nama (atau sebagian nama): ").strip().lower()
    if not keyword:
        print("Keyword tidak boleh kosong!")
        return

    hasil = [m for m in data if keyword in m["nama"].lower()]
    if not hasil:
        print("Data tidak ditemukan.")
        return

    print(f"\nDitemukan {len(hasil)} data:")
    print(f"{'No':<4} {'NIM':<14} {'Nama':<22} {'Jurusan':<20} {'Nilai':<6}")
    print("-" * 70)
    for i, m in enumerate(hasil, 1):
        print(f"{i:<4} {m['nim']:<14} {m['nama']:<22} {m['jurusan']:<20} {m['nilai']:<6}")


def validasi_nilai(nilai_str):
    nilai_str = nilai_str.strip()
    if not nilai_str:
        return False, "Nilai tidak boleh kosong!"
    try:
        nilai = float(nilai_str)
    except ValueError:
        return False, "Nilai harus berupa angka!"

    if nilai < 0:
        return False, "Nilai tidak boleh minus!"
    if nilai > 100:
        return False, "Nilai tidak boleh lebih dari 100!"

    # Format rapi: buang .0 jika bilangan bulat
    if nilai.is_integer():
        return True, str(int(nilai))
    return True, str(round(nilai, 2))


def tambah_mahasiswa():
    data = load_mahasiswa()
    print("\n===== TAMBAH DATA MAHASISWA =====")
    nim = input("NIM     : ").strip()
    nama = input("Nama    : ").strip()
    jurusan = input("Jurusan : ").strip()
    nilai_input = input("Nilai   : ").strip()

    if not nim or not nama:
        print("NIM dan Nama wajib diisi!")
        return

    if any(m["nim"] == nim for m in data):
        print(f"NIM {nim} sudah terdaftar!")
        return

    ok, hasil = validasi_nilai(nilai_input)
    if not ok:
        print(hasil)
        return

    data.append({
        "nim": nim,
        "nama": nama,
        "jurusan": jurusan,
        "nilai": str(hasil)
    })
    simpan_mahasiswa(data)
    print(f"Data mahasiswa {nama} berhasil ditambahkan!")


def edit_mahasiswa():
    data = load_mahasiswa()
    print("\n===== EDIT DATA MAHASISWA =====")
    nim = input("Masukkan NIM yang akan diedit: ").strip()

    ditemukan = None
    for m in data:
        if m["nim"] == nim:
            ditemukan = m
            break

    if ditemukan is None:
        print("NIM tidak ditemukan!")
        return

    print(f"Data saat ini -> Nama: {ditemukan['nama']} | Jurusan: {ditemukan['jurusan']} | Nilai: {ditemukan['nilai']}")
    print("(Kosongkan jika tidak ingin diubah)")

    nama_baru = input("Nama baru    : ").strip()
    jurusan_baru = input("Jurusan baru : ").strip()
    nilai_baru = input("Nilai baru   : ").strip()

    if nama_baru:
        ditemukan["nama"] = nama_baru
    if jurusan_baru:
        ditemukan["jurusan"] = jurusan_baru
    if nilai_baru:
        ok, hasil = validasi_nilai(nilai_baru)
        if not ok:
            print(hasil)
            return
        ditemukan["nilai"] = str(hasil)

    simpan_mahasiswa(data)
    print("Data berhasil diubah!")


def hapus_mahasiswa():
    data = load_mahasiswa()
    print("\n===== HAPUS DATA MAHASISWA =====")
    nim = input("Masukkan NIM yang akan dihapus: ").strip()

    baru = [m for m in data if m["nim"] != nim]
    if len(baru) == len(data):
        print("NIM tidak ditemukan!")
        return

    konfirmasi = input(f"Yakin hapus NIM {nim}? (y/n): ").strip().lower()
    if konfirmasi == "y":
        simpan_mahasiswa(baru)
        print("Data berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


# ==================== MENU SISTEM ====================

def menu_kelola_mahasiswa():
    while True:
        data = load_mahasiswa()
        print("\n===== KELOLA DATA MAHASISWA =====")
        print(f"Jumlah data: {len(data)}")
        print("1. Lihat semua data")
        print("2. Cari berdasarkan nama")
        print("3. Tambah data")
        print("4. Edit data")
        print("5. Hapus data")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            break
        elif pilihan == "1":
            lihat_semua_mahasiswa()
        elif pilihan == "2":
            cari_mahasiswa()
        elif pilihan == "3":
            tambah_mahasiswa()
        elif pilihan == "4":
            edit_mahasiswa()
        elif pilihan == "5":
            hapus_mahasiswa()
        else:
            print("Pilihan tidak valid!")


def menu_data_profile():
    while True:
        print("\n===== DATA PROFILE =====")
        print(f"User login : {current_user}")
        print("1. Edit Password Saya")
        print("0. Kembali")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            break
        elif pilihan == "1":
            edit_password()
        else:
            print("Pilihan tidak valid!")


def menu_utama():
    while True:
        print("\n===== MENU FUNGSI =====")
        print("1. Kelola Data Mahasiswa")
        print("2. Data Profile")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("\nKembali ke menu login...")
            break
        elif pilihan == "1":
            menu_kelola_mahasiswa()
        elif pilihan == "2":
            menu_data_profile()
        else:
            print("Pilihan tidak valid!")


def menu_login():
    while True:
        print("\n===== MENU LOGIN =====")
        print("1. Login")
        print("2. Exit")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            proses_login()
        elif pilihan == "2":
            print("\nTerima kasih. Program selesai.")
            break
        elif pilihan == "333":
            menu_create_akun()
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    print("=" * 55)
    print("     LATIHAN 15B - LOGIN + CRUD DATA MAHASISWA")
    print("=" * 55)
    buat_file_login_default()
    buat_file_mahasiswa_default()
    menu_login()