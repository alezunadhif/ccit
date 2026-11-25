# =========================================================
# LATIHAN 15A: Create Akun + Lihat Data + Edit Password
# =========================================================

import os

LOGIN_FILE = "login15a.txt"
current_user = None


def buat_file_login_default():
    if not os.path.exists(LOGIN_FILE):
        with open(LOGIN_FILE, "w") as f:
            f.write("admin:adminjuga\n")
            f.write("tri:333\n")
        print(">> File login.txt berhasil dibuat dengan 2 akun default.")
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
        print(f"Error: {e}")
    return akun


def simpan_akun(akun):
    with open(LOGIN_FILE, "w") as f:
        for username, password in akun.items():
            f.write(f"{username}:{password}\n")


def proses_login():
    global current_user
    akun = load_akun()
    print("\n----- FORM LOGIN -----")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

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
    username = input("Username baru: ").strip()
    password = input("Password baru: ").strip()

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


def menu_utama():
    data_mahasiswa = []
    while True:
        print("\n===== MENU FUNGSI =====")
        print(f"Jumlah data: {len(data_mahasiswa)}")
        print("1. Lihat semua data")
        print("2. Cari berdasarkan nama")
        print("3. Tambah data")
        print("4. Edit data")
        print("5. Hapus data")
        print("6. Informasi Fungsi")
        print("7. Edit Password Saya")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("\nKembali ke menu login...")
            break
        elif pilihan == "7":
            edit_password()
        elif pilihan in ["1", "2", "3", "4", "5", "6"]:
            print(
                "Terimakasih telah memilih menu ini, silahkan lihat latihan sebelumnya ini hany testing"
            )
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
    print("   LATIHAN 15A - CREATE AKUN + EDIT PASSWORD")
    print("=" * 55)
    buat_file_login_default()
    menu_login()