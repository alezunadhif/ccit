# =========================================================
# MODUL PRAKTIKUM PYTHON - LATIHAN 16A
# Tema: Migrasi Login ke MySQL & Hak Akses (Role-Based)
# =========================================================

import mysql.connector

# Variabel Global untuk menyimpan sesi user aktif
current_user = None
current_role = None


# BAGIAN 1: KONFIGURASI & KONEKSI DATABASE
def get_connection():
    try:
        # Menghubungkan ke service MySQL localhost XAMPP
        conn = mysql.connector.connect(host="localhost", user="root", password="")
        cursor = conn.cursor()

        # Inisialisasi Database & Tabel jika belum tersedia
        cursor.execute("CREATE DATABASE IF NOT EXISTS db_praktikum")
        cursor.execute("USE db_praktikum")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS login (
                username VARCHAR(50) PRIMARY KEY,
                password VARCHAR(100) NOT NULL,
                role ENUM('admin', 'user') DEFAULT 'user'
            )
        """)

        # Cek dan isi data default jika tabel masih kosong
        cursor.execute("SELECT COUNT(*) FROM login")
        if cursor.fetchone()[0] == 0:
            sql_insert = "INSERT INTO login (username, password, role) VALUES (%s, %s, %s)"
            data_default = [
                ("admin", "adminjuga", "admin"),
                ("budi", "budi123", "user"),
            ]
            cursor.executemany(sql_insert, data_default)
            conn.commit()
            print(">> [Sistem] Tabel login dibuat & diisi default akun.")

        return conn
    except mysql.connector.Error as err:
        print(f"Error Koneksi MySQL: {err}")
        return None


# BAGIAN 2: LOGIKA AUTENTIKASI (LOGIN)
def proses_login():
    global current_user, current_role
    print("\n=== FORM LOGIN MYSQL ===")
    user_input = input("Username: ").strip()
    pass_input = input("Password: ").strip()

    conn = get_connection()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)
    sql = "SELECT * FROM login WHERE username=%s AND password=%s"
    cursor.execute(sql, (user_input, pass_input))
    akun = cursor.fetchone()

    if akun:
        current_user = akun["username"]
        current_role = akun["role"]
        print(
            f"\nBerhasil! Selamat datang, {current_user} (Akses: {current_role.upper()})"
        )
        menu_utama()
    else:
        print("\nGAGAL: Username atau password salah!")

    cursor.close()
    conn.close()


# BAGIAN 3: SUBMENU KELOLA AKUN (CRUD ADMIN)
def lihat_akun():
    print("\n=== DAFTAR AKUN SISTEM ===")
    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT username, role FROM login")
    akun_list = cursor.fetchall()

    print(f"{'No':<4} | {'Username':<15} | {'Role':<10}")
    print("-" * 35)
    for i, akun in enumerate(akun_list, 1):
        print(f"{i:<4} | {akun['username']:<15} | {akun['role'].upper():<10}")

    cursor.close()
    conn.close()


def tambah_akun():
    print("\n=== TAMBAH AKUN BARU ===")
    username = input("Username baru       : ").strip()
    password = input("Password baru       : ").strip()
    role = input("Role (admin/user)   : ").strip().lower()

    if role not in ["admin", "user"]:
        print("Gagal: Role tidak valid! Harus 'admin' atau 'user'.")
        return

    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO login (username, password, role) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, password, role))
        conn.commit()
        print(f"Berhasil! Akun [{username}] ditambahkan sebagai [{role.upper()}].")
    except mysql.connector.IntegrityError:
        print(f"Gagal: Username '{username}' sudah terdaftar di Database!")
    finally:
        cursor.close()
        conn.close()


def hapus_akun():
    print("\n=== HAPUS AKUN ===")
    target_user = input("Masukkan username yang akan dihapus: ").strip()

    # Cegah admin menghapus akun diri sendiri saat aktif
    if target_user == current_user:
        print("Gagal: Anda tidak boleh menghapus akun sendiri saat sedang login!")
        return

    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM login WHERE username=%s", (target_user,))
    if not cursor.fetchone():
        print("Gagal: Username tidak ditemukan!")
    else:
        konfirmasi = (
            input(f"Yakin ingin menghapus '{target_user}'? (y/n): ")
            .strip()
            .lower()
        )
        if konfirmasi == "y":
            cursor.execute("DELETE FROM login WHERE username=%s", (target_user,))
            conn.commit()
            print(f"Berhasil! Akun '{target_user}' telah dihapus.")
        else:
            print("Penghapusan dibatalkan.")

    cursor.close()
    conn.close()


def renew_password():
    print("\n=== RENEW PASSWORD ===")
    target_user = input(
        "Masukkan username yang akan diubah passwordnya: "
    ).strip()

    conn = get_connection()
    if not conn:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM login WHERE username=%s", (target_user,))
    if not cursor.fetchone():
        print("Gagal: Username tidak ditemukan!")
    else:
        pass_baru = input(
            f"Masukkan password baru untuk '{target_user}': "
        ).strip()
        pass_konfirmasi = input("Konfirmasi password baru: ").strip()

        if pass_baru != pass_konfirmasi:
            print("Gagal: Konfirmasi password tidak cocok! Silakan coba lagi.")
        else:
            cursor.execute(
                "UPDATE login SET password=%s WHERE username=%s",
                (pass_baru, target_user),
            )
            conn.commit()
            print(
                f"Berhasil! Password untuk akun '{target_user}' telah diperbarui."
            )

    cursor.close()
    conn.close()


def menu_kelola_akun():
    while True:
        print("\n=== SUB MENU: KELOLA AKUN SISTEM ===")
        print("1. List Akun")
        print("2. Tambah Akun")
        print("3. Hapus Akun")
        print("4. Renew Password")
        print("0. Kembali ke Menu Utama")

        pilihan = input("Pilih menu (0-4): ").strip()
        if pilihan == "1":
            lihat_akun()
        elif pilihan == "2":
            tambah_akun()
        elif pilihan == "3":
            hapus_akun()
        elif pilihan == "4":
            renew_password()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid!")


# BAGIAN 4: MENU UTAMA (ROLE-BASED ACCESS CONTROL)
def menu_utama():
    global current_user, current_role
    while True:
        print(f"\n=== MENU UTAMA ({current_role.upper()}) ===")
        print("1. Kelola Data Mahasiswa (Segera L16B)")

        # Menu 2 hanya tampil bagi role admin
        if current_role == "admin":
            print("2. Kelola Akun Sistem")
        print("0. Logout")

        pilihan = input("Pilih menu: ").strip()
        if pilihan == "0":
            print("Logout berhasil...")
            current_user = None
            current_role = None
            break
        elif pilihan == "2" and current_role == "admin":
            menu_kelola_akun()
        elif pilihan == "1":
            print(">> (Fitur CRUD Mahasiswa MySQL akan dilanjutkan pada L16B)")
        else:
            print("Pilihan tidak valid / Anda tidak memiliki akses ke menu ini.")


# PROGRAM UTAMA
if __name__ == "__main__":
    while True:
        print("\n--- SISTEM INFORMASI (MYSQL VER) ---")
        print("1. Login")
        print("2. Keluar Aplikasi")

        opsi = input("Pilih: ").strip()
        if opsi == "1":
            proses_login()
        elif opsi == "2":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")