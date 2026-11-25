import mysql.connector
import hashlib
from datetime import datetime


def get_db():
    # konek dulu tanpa milih database biar ga error Unknown database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ExpenseTracker")
    cursor.execute("USE ExpenseTracker")

    # auto-create tables kalo belom ada
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(64) NOT NULL,
            role ENUM('admin', 'user') DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            type ENUM('INCOME', 'EXPENSE') NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT NOT NULL,
            category_id INT NOT NULL,
            amount DECIMAL(15, 2) NOT NULL,
            transaction_date DATE NOT NULL,
            description TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT
        )
    """)

    conn.commit()
    cursor.close()
    return conn

# 2. Hash Password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# 3. Class User
class User:
    def __init__(self, user_id, username, role):
        self.user_id = user_id
        self.username = username
        self.role = role

    def render_menu(self):
        print("\nMenu User")


# 4. Class Admin - Inheritance
class Admin(User):
    def render_menu(self):
        print("\n" + "=" * 55)
        print("              ADMIN DASHBOARD")
        print("=" * 55)
        print("1. Kelola Kategori")
        print("2. Kelola Pengguna")
        print("3. Ringkasan Global")
        print("4. Logout")
        print("=" * 55)


# 5. Class RegularUser - Inheritance
class RegularUser(User):
    def render_menu(self):
        print("\n" + "=" * 55)
        print("             CATATAN KEUANGAN PRIBADI")
        print("=" * 55)
        print("1. Ringkasan Saldo")
        print("2. Catat Transaksi Baru")
        print("3. Riwayat Transaksi")
        print("4. Edit Transaksi")
        print("5. Hapus Transaksi")
        print("6. Logout")
        print("=" * 55)


# 6. Polymorphism pada Transaksi
class Transaction:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError("Nominal harus lebih dari 0")
        self.amount = amount

    def affect_balance(self, balance):
        return balance


class IncomeTransaction(Transaction):
    def affect_balance(self, balance):
        return balance + self.amount


class ExpenseTransaction(Transaction):
    def affect_balance(self, balance):
        return balance - self.amount


# 7. Login
def login():
    db = get_db()
    cursor = db.cursor()

    print("\n" + "=" * 55)
    print("                 EXPENSE TRACKER")
    print("=" * 55)

    username = input("Username : ")
    password = input("Password : ")

    query = """
        SELECT id, username, role
        FROM users
        WHERE username = %s AND password = %s
    """

    cursor.execute(query, (username, hash_password(password)))
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result:
        print("\nLogin berhasil. Selamat datang,", result[1])

        if result[2] == "admin":
            return Admin(result[0], result[1], result[2])
        else:
            return RegularUser(result[0], result[1], result[2])

    print("\nUsername atau password salah!")
    return None


# 8. Tabel Kategori
def tampil_kategori():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, name, type
        FROM categories
        ORDER BY id
    """)

    results = cursor.fetchall()

    print("\n--- DAFTAR KATEGORI ---")
    print(f"{'ID':<5} | {'Nama Kategori':<20} | {'Jenis'}")
    print("-" * 45)

    for row in results:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]}")

    cursor.close()
    db.close()


# 9. Tambah Kategori
def tambah_kategori():
    nama = input("Nama kategori : ")
    jenis = input("Jenis (INCOME/EXPENSE): ").upper()

    if jenis not in ["INCOME", "EXPENSE"]:
        print("Jenis kategori tidak valid!")
        return

    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO categories (name, type) VALUES (%s, %s)",
        (nama, jenis)
    )

    db.commit()
    cursor.close()
    db.close()

    print("Kategori berhasil ditambahkan!")


# 10. Edit Kategori
def edit_kategori():
    tampil_kategori()

    kategori_id = input("\nMasukkan ID kategori: ")
    nama = input("Nama baru: ")
    jenis = input("Jenis baru (INCOME/EXPENSE): ").upper()

    if jenis not in ["INCOME", "EXPENSE"]:
        print("Jenis kategori tidak valid!")
        return

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE categories
        SET name = %s, type = %s
        WHERE id = %s
    """, (nama, jenis, kategori_id))

    db.commit()
    cursor.close()
    db.close()

    print("Kategori berhasil diubah!")


# 11. Hapus Kategori
def hapus_kategori():
    tampil_kategori()

    kategori_id = input("\nMasukkan ID kategori yang dihapus: ")

    db = get_db()
    cursor = db.cursor()

    try:
        cursor.execute(
            "DELETE FROM categories WHERE id = %s",
            (kategori_id,)
        )
        db.commit()
        print("Kategori berhasil dihapus!")
    except mysql.connector.Error:
        db.rollback()
        print("Kategori tidak dapat dihapus karena masih digunakan!")

    cursor.close()
    db.close()


# 12. Menu Kelola Kategori
def kelola_kategori():
    while True:
        print("\n--- KELOLA KATEGORI ---")
        print("1. Lihat Kategori")
        print("2. Tambah Kategori")
        print("3. Edit Kategori")
        print("4. Hapus Kategori")
        print("5. Kembali")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampil_kategori()
        elif pilihan == "2":
            tambah_kategori()
        elif pilihan == "3":
            edit_kategori()
        elif pilihan == "4":
            hapus_kategori()
        elif pilihan == "5":
            break
        else:
            print("Pilihan tidak valid!")


# 13. Kelola Pengguna
def kelola_user():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, username, role, created_at
        FROM users
        ORDER BY id
    """)

    results = cursor.fetchall()

    print("\n--- DAFTAR PENGGUNA ---")
    print(f"{'ID':<5} | {'Username':<20} | {'Role':<10} | {'Dibuat'}")
    print("-" * 65)

    for row in results:
        print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<10} | {row[3]}")

    cursor.close()
    db.close()


# 14. Ringkasan Global Admin
def ringkasan_global():
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(CASE
                WHEN c.type = 'INCOME' THEN t.amount
                ELSE 0
            END), 0),
            COALESCE(SUM(CASE
                WHEN c.type = 'EXPENSE' THEN t.amount
                ELSE 0
            END), 0),
            COUNT(t.id)
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
    """)

    income, expense, jumlah = cursor.fetchone()
    saldo = income - expense

    print("\n--- RINGKASAN GLOBAL ---")
    print(f"{'Keterangan':<25} | {'Jumlah'}")
    print("-" * 45)
    print(f"{'Total Pemasukan':<25} | Rp{income:,.2f}")
    print(f"{'Total Pengeluaran':<25} | Rp{expense:,.2f}")
    print(f"{'Saldo':<25} | Rp{saldo:,.2f}")
    print(f"{'Jumlah Transaksi':<25} | {jumlah}")

    cursor.close()
    db.close()


# 15. Ringkasan Saldo User
def ringkasan_saldo(user_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            COALESCE(SUM(CASE
                WHEN c.type = 'INCOME' THEN t.amount
                ELSE 0
            END), 0),
            COALESCE(SUM(CASE
                WHEN c.type = 'EXPENSE' THEN t.amount
                ELSE 0
            END), 0)
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.user_id = %s
    """, (user_id,))

    income, expense = cursor.fetchone()
    saldo = income - expense

    print("\n--- RINGKASAN SALDO ---")
    print(f"{'Keterangan':<25} | {'Jumlah'}")
    print("-" * 45)
    print(f"{'Total Pemasukan':<25} | Rp{income:,.2f}")
    print(f"{'Total Pengeluaran':<25} | Rp{expense:,.2f}")
    print(f"{'Sisa Saldo':<25} | Rp{saldo:,.2f}")

    cursor.close()
    db.close()


# 16. Tampilkan Kategori Sesuai Jenis
def pilih_kategori(jenis):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT id, name
        FROM categories
        WHERE type = %s
        ORDER BY id
    """, (jenis,))

    results = cursor.fetchall()

    print(f"\n--- KATEGORI {jenis} ---")
    print(f"{'ID':<5} | {'Nama Kategori'}")
    print("-" * 30)

    for row in results:
        print(f"{row[0]:<5} | {row[1]}")

    cursor.close()
    db.close()


# 17. Catat Transaksi
def catat_transaksi(user_id):
    print("\n--- CATAT TRANSAKSI BARU ---")
    print("1. Pemasukan")
    print("2. Pengeluaran")

    pilihan = input("Jenis transaksi: ")

    if pilihan == "1":
        jenis = "INCOME"
    elif pilihan == "2":
        jenis = "EXPENSE"
    else:
        print("Jenis transaksi tidak valid!")
        return

    pilih_kategori(jenis)

    try:
        category_id = int(input("ID Kategori : "))
        amount = float(input("Nominal     : "))

        if amount <= 0:
            print("Nominal harus lebih dari 0!")
            return

        tanggal = input("Tanggal (YYYY-MM-DD): ")
        datetime.strptime(tanggal, "%Y-%m-%d")

    except ValueError:
        print("Input tidak valid!")
        return

    description = input("Keterangan  : ")

    # Polymorphism
    if jenis == "INCOME":
        transaksi = IncomeTransaction(amount)
    else:
        transaksi = ExpenseTransaction(amount)

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (user_id, category_id, amount, transaction_date, description)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        user_id,
        category_id,
        transaksi.amount,
        tanggal,
        description
    ))

    db.commit()
    cursor.close()
    db.close()

    print("Transaksi berhasil disimpan!")


# 18. Riwayat Transaksi
def riwayat_transaksi(user_id):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            t.id,
            c.name,
            c.type,
            t.amount,
            t.transaction_date,
            t.description
        FROM transactions t
        JOIN categories c ON t.category_id = c.id
        WHERE t.user_id = %s
        ORDER BY t.transaction_date DESC, t.id DESC
    """, (user_id,))

    results = cursor.fetchall()

    print("\n--- RIWAYAT TRANSAKSI ---")
    print(f"{'ID':<5} | {'Kategori':<15} | {'Jenis':<10} | {'Nominal':<15} | {'Tanggal':<12} | {'Keterangan'}")
    print("-" * 90)

    for row in results:
        print(
            f"{row[0]:<5} | "
            f"{row[1]:<15} | "
            f"{row[2]:<10} | "
            f"Rp{row[3]:<12,.2f} | "
            f"{str(row[4]):<12} | "
            f"{row[5]}"
        )

    cursor.close()
    db.close()


# 19. Edit Transaksi
def edit_transaksi(user_id):
    riwayat_transaksi(user_id)

    try:
        transaksi_id = int(input("\nMasukkan ID transaksi: "))
        amount = float(input("Nominal baru: "))

        if amount <= 0:
            print("Nominal harus lebih dari 0!")
            return

    except ValueError:
        print("Input tidak valid!")
        return

    description = input("Keterangan baru: ")

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        UPDATE transactions
        SET amount = %s, description = %s
        WHERE id = %s AND user_id = %s
    """, (amount, description, transaksi_id, user_id))

    if cursor.rowcount > 0:
        db.commit()
        print("Transaksi berhasil diubah!")
    else:
        print("Transaksi tidak ditemukan!")

    cursor.close()
    db.close()


# 20. Hapus Transaksi
def hapus_transaksi(user_id):
    riwayat_transaksi(user_id)

    try:
        transaksi_id = int(input("\nMasukkan ID transaksi: "))
    except ValueError:
        print("ID tidak valid!")
        return

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        DELETE FROM transactions
        WHERE id = %s AND user_id = %s
    """, (transaksi_id, user_id))

    if cursor.rowcount > 0:
        db.commit()
        print("Transaksi berhasil dihapus!")
    else:
        print("Transaksi tidak ditemukan!")

    cursor.close()
    db.close()


# 21. Menu Admin
def admin_menu(admin):
    while True:
        admin.render_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            kelola_kategori()

        elif pilihan == "2":
            kelola_user()

        elif pilihan == "3":
            ringkasan_global()

        elif pilihan == "4":
            print("Logout berhasil.")
            break

        else:
            print("Pilihan tidak valid!")


# 22. Menu User
def user_menu(user):
    while True:
        user.render_menu()
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == "1":
            ringkasan_saldo(user.user_id)

        elif pilihan == "2":
            catat_transaksi(user.user_id)

        elif pilihan == "3":
            riwayat_transaksi(user.user_id)

        elif pilihan == "4":
            edit_transaksi(user.user_id)

        elif pilihan == "5":
            hapus_transaksi(user.user_id)

        elif pilihan == "6":
            print("Logout berhasil.")
            break

        else:
            print("Pilihan tidak valid!")


# 23. Main Program
def main():
    while True:
        user = login()

        if user:
            if isinstance(user, Admin):
                admin_menu(user)
            else:
                user_menu(user)

        lagi = input("\nKembali ke halaman login? (y/n): ").lower()

        if lagi != "y":
            print("\nTerima kasih telah menggunakan ExpenseTracker!")
            break


if __name__ == "__main__":
    main()