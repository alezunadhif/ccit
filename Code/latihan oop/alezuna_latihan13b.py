# =====================================================
# LATIHAN 13B: Rekursi
# Login + Menu demo rekursi (hubungkan ke pola L13)
# =====================================================

def login():
    username_benar = "nadhif"      # Ganti 
    password_benar = "nadhif123"   # Ganti 
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
                print("\nAkses ditolak.")
                return False


def info_rekursi():
    print("\n" + "=" * 50)
    print("               INFORMASI REKURSI")
    print("=" * 50)
    print("""
Rekursi: fungsi yang memanggil DIRINYA SENDIRI.

Syarat agar tidak infinite loop:
1. BASE CASE      : kondisi berhenti
2. RECURSIVE CASE : panggil diri dengan masalah LEBIH KECIL

Contoh kerangka:
def f(n):
    if n <= 0:          # base case
        return ...
    else:               # recursive case
        return ... f(n - 1)

Risiko: tanpa base case -> RecursionError (stack overflow)
""")
    print("=" * 50)


def hitung_mundur(n):
    """Rekursi sederhana: cetak n, n-1, ... 1 lalu Selesai!"""
    if n <= 0:
        print("Selesai!")  # BASE CASE
        return
    print(n)
    hitung_mundur(n - 1)   # RECURSIVE CASE


def faktorial(n):
    """n! = n * (n-1) * ... * 1"""
    if n == 0 or n == 1:
        return 1           # BASE CASE
    return n * faktorial(n - 1)  # RECURSIVE CASE


def fibonacci(n):
    """Suku ke-n deret Fibonacci (0, 1, 1, 2, 3, 5, ...) versi sederhana."""
    if n <= 0:
        return 0           # BASE CASE 1
    if n == 1:
        return 1           # BASE CASE 2
    return fibonacci(n - 1) + fibonacci(n - 2)  # RECURSIVE CASE


def jumlah_list(data):
    """Jumlahkan elemen list secara rekursif."""
    if len(data) == 0:
        return 0           # BASE CASE: list kosong
    # Elemen pertama + jumlah sisa list
    return data[0] + jumlah_list(data[1:])  # RECURSIVE CASE


def faktorial_loop(n):
    """Versi LOOP untuk dibandingkan dengan rekursi."""
    hasil = 1
    for i in range(1, n + 1):
        hasil = hasil * i
    return hasil


def main():
    if not login():
        return

    # Data contoh (berhubungan dengan tema nilai mahasiswa)
    nilai_contoh = [80, 70, 90, 85]

    while True:
        print("\n===== MENU REKURSI (L13B) =====")
        print("1. Informasi rekursi")
        print("2. Hitung mundur (rekursi)")
        print("3. Faktorial (rekursi)")
        print("4. Fibonacci (rekursi)")
        print("5. Jumlah list nilai (rekursi)")
        print("6. Bandingkan faktorial: rekursi vs loop")
        print("0. Keluar")

        pilih = input("Pilihan: ")

        if pilih == "1":
            info_rekursi()
        elif pilih == "2":
            n = int(input("Masukkan n (contoh 5): "))
            print("Hasil hitung mundur:")
            hitung_mundur(n)
        elif pilih == "3":
            n = int(input("Masukkan n (contoh 5): "))
            if n < 0:
                print("n harus >= 0")
            else:
                print(f"faktorial({n}) = {faktorial(n)}")
        elif pilih == "4":
            n = int(input("Suku ke-n (contoh 7): "))
            if n < 0:
                print("n harus >= 0")
            else:
                print(f"fibonacci({n}) = {fibonacci(n)}")
        elif pilih == "5":
            print(f"List nilai: {nilai_contoh}")
            print(f"Jumlah (rekursi) = {jumlah_list(nilai_contoh)}")
            print(f"Cek sum() biasa  = {sum(nilai_contoh)}")
        elif pilih == "6":
            n = int(input("Masukkan n (contoh 6): "))
            if n < 0:
                print("n harus >= 0")
            else:
                r = faktorial(n)
                L = faktorial_loop(n)
                print(f"Rekursi : faktorial({n}) = {r}")
                print(f"Loop    : faktorial({n}) = {L}")
                print("Hasil sama?", "Ya" if r == L else "Tidak")
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()