# =========================================================
# MODUL PRAKTIKUM PYTHON - LATIHAN 15
# Tema: File I/O + Sistem Login Sederhana
# =========================================================

import os

LOGIN_FILE = "login.txt"

# 1. Membuat file login.txt default (jika belum ada)
def buat_file_login_default():
    if not os.path.exists(LOGIN_FILE):
        with open(LOGIN_FILE, "w") as f:
            f.write("admin:admin123\n")
            f.write("mahasiswa:python15\n")
        print(">> File login.txt berhasil dibuat dengan 2 akun default.")
        print("   1. admin / admin123")
        print("   2. mahasiswa / python15")


# 2. Membaca data akun dari login.txt
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
        print("File login.txt tidak ditemukan. Membuat file default...")
        buat_file_login_default()
        return load_akun()
    except Exception as e:
        print(f"Terjadi error saat membaca file: {e}")
    return akun


# 3. Proses Login
def proses_login():
    akun = load_akun()

    print("\n----- FORM LOGIN -----")
    username = input("Username : ").strip()
    password = input("Password : ").strip()

    if username in akun and akun[username] == password:
        print(f"\nLogin berhasil! Selamat datang, {username}")
        menu_utama()
    else:
        print("\nUsername atau password salah!")


# 4. Menu Create Akun (sementara - belum aktif penuh)
def menu_create_akun():
    print("\n===== CREATE AKUN =====")
    print("Fitur ini masih dalam tahap pengembangan.")
    print("Nanti akan diaktifkan sepenuhnya di Latihan 15A.")
    print("Sementara hanya menampilkan pesan ini.")
    input("\nTekan Enter untuk kembali ke menu login...")


# 5. Menu Utama (setelah login berhasil)
def menu_utama():
    data_mahasiswa = []  # dummy hanya untuk menampilkan jumlah
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

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("\nKembali ke menu login...")
            break
        elif pilihan in ["1", "2", "3", "4", "5", "6"]:
            print(
                "Terimakasih telah memilih menu ini, "
                "silahkan lihat latihan sebelumnya ini hanya testing"
            )
        else:
            print("Pilihan tidak valid!")


# 6. Menu Login Utama
def menu_login():
    while True:
        print("\n===== MENU LOGIN =====")
        print("1. Login")
        print("2. Exit")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "1":
            proses_login()
        elif pilihan == "2":
            print("\nTerima kasih telah menggunakan program ini.")
            print("Program selesai.")
            break
        elif pilihan == "333":
            # Fitur tersembunyi
            menu_create_akun()
        else:
            print("Pilihan tidak valid!")


# PROGRAM UTAMA
if __name__ == "__main__":
    print("=" * 55)
    print("       LATIHAN 15 - FILE I/O SISTEM LOGIN")
    print("=" * 55)
    buat_file_login_default()
    menu_login()