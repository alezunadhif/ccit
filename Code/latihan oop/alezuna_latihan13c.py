# =====================================================
# LATIHAN 13C: Lambda
# Login + Demo lambda, map, filter, sorted
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


def info_lambda():
    print("\n" + "=" * 50)
    print("               INFORMASI LAMBDA")
    print("=" * 50)
    print("""
Lambda: fungsi ANONIM (tanpa nama) dalam satu baris.
Sintaks:
    lambda parameter: ekspresi

Setara dengan:
    def nama(parameter):
        return ekspresi

Ciri:
- Hanya SATU ekspresi (bukan blok banyak baris)
- Otomatis me-return hasil ekspresi
- Cocok untuk fungsi kecil / sekali pakai

Sering dipakai bersama:
    map(fungsi, list)      -> terapkan ke setiap elemen
    filter(fungsi, list)   -> saring elemen yang True
    sorted(list, key=...)  -> urutkan dengan aturan key
""")
    print("=" * 50)


def demo_lambda_dasar():
    print("\n--- Lambda dasar ---")
    kali2 = lambda x: x * 2
    print(f"kali2(5) = {kali2(5)}")

    tambah = lambda a, b: a + b
    print(f"tambah(3, 4) = {tambah(3, 4)}")

    # Langsung panggil tanpa disimpan ke variabel
    print(f"(lambda x: x**2)(6) = {(lambda x: x**2)(6)}")


def demo_map():
    print("\n--- map() + lambda ---")
    nilai = [80, 70, 90, 55, 40]
    print(f"Nilai asli : {nilai}")

    # Tambah 5 poin ke setiap nilai
    bonus = list(map(lambda x: x + 5, nilai))
    print(f"Setelah +5 : {bonus}")

    # Konversi ke status lulus/tidak (sederhana)
    status = list(map(lambda x: "LULUS" if x >= 55 else "TIDAK LULUS", nilai))
    print(f"Status     : {status}")


def demo_filter():
    print("\n--- filter() + lambda ---")
    nilai = [80, 70, 90, 55, 40, 30]
    print(f"Nilai asli          : {nilai}")

    lulus = list(filter(lambda x: x >= 55, nilai))
    print(f"Yang LULUS (>=55)   : {lulus}")

    kurang = list(filter(lambda x: x < 55, nilai))
    print(f"Yang TIDAK LULUS    : {kurang}")


def demo_sorted():
    print("\n--- sorted() + lambda (key) ---")
    mahasiswa = [
        {"nama": "Budi", "uts": 80},
        {"nama": "Andi", "uts": 70},
        {"nama": "Siti", "uts": 90},
        {"nama": "Rina", "uts": 65},
    ]

    print("Data awal:")
    for m in mahasiswa:
        print(f"  {m}")

    # Urut naik berdasarkan UTS
    naik = sorted(mahasiswa, key=lambda m: m['uts'])
    print("\nUrut UTS naik:")
    for m in naik:
        print(f"  {m['nama']}: {m['uts']}")

    # Urut turun berdasarkan UTS
    turun = sorted(mahasiswa, key=lambda m: m['uts'], reverse=True)
    print("\nUrut UTS turun:")
    for m in turun:
        print(f"  {m['nama']}: {m['uts']}")


def demo_banding_def():
    print("\n--- Lambda vs def ---")

    def kuadrat_def(x):
        return x * x

    kuadrat_lambda = lambda x: x * x

    print(f"def    : kuadrat_def(7) = {kuadrat_def(7)}")
    print(f"lambda : kuadrat_lambda(7) = {kuadrat_lambda(7)}")
    print("Hasil sama. Lambda lebih singkat untuk fungsi 1 baris.")
    print("Untuk logika panjang / banyak baris lebih baik pakai def.")


def main():
    if not login():
        return

    while True:
        print("\n===== MENU LAMBDA (L13C) =====")
        print("1. Informasi lambda")
        print("2. Lambda dasar")
        print("3. map() + lambda")
        print("4. filter() + lambda")
        print("5. sorted() + lambda (data mahasiswa)")
        print("6. Bandingkan lambda vs def")
        print("0. Keluar")

        pilih = input("Pilihan: ")
        if pilih == "1":
            info_lambda()
        elif pilih == "2":
            demo_lambda_dasar()
        elif pilih == "3":
            demo_map()
        elif pilih == "4":
            demo_filter()
        elif pilih == "5":
            demo_sorted()
        elif pilih == "6":
            demo_banding_def()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()