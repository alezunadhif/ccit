# =====================================================
# LATIHAN 14: Exception / Error Handling
# Login + Menu + Data Mahasiswa + try/except
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


def hitung_grade(uts, uas, tugas):
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


def input_angka(label, min_val=0, max_val=100):
    """Input angka aman dengan try/except + validasi rentang."""
    while True:
        try:
            nilai = float(input(f"{label} ({min_val}-{max_val}): "))
            if nilai < min_val or nilai > max_val:
                raise ValueError(f"Nilai harus {min_val}-{max_val}")
            return nilai
        except ValueError as e:
            print(f" [!] Input tidak valid: {e}")
            print("     Coba lagi (harus angka dalam rentang).")


def cari_indeks(data, nama):
    for i, mhs in enumerate(data):
        if mhs["nama"].lower() == nama.lower():
            return i
    return -1


def info_exception():
    print("\n" + "=" * 50)
    print("           INFORMASI EXCEPTION HANDLING")
    print("=" * 50)
    print("""
Exception: error saat program berjalan (runtime).

Struktur dasar:
    try:
        # kode yang mungkin error
    except JenisError:
        # penanganan jika error terjadi
    else:
        # dijalankan jika TIDAK ada error
    finally:
        # SELALU dijalankan (ada error atau tidak)

Jenis yang sering muncul:
    ValueError        : input bukan angka / nilai di luar rentang
    IndexError        : indeks list tidak ada
    KeyError          : key dict tidak ada
    ZeroDivisionError : pembagian dengan nol

Keyword:
    raise             : melempar error sendiri (sengaja)
""")
    print("=" * 50)


def lihat_semua(data):
    if not data:
        print("Data masih kosong.")
        return
    for i, mhs in enumerate(data):
        print(f"\n--- [{i}] ---")
        tampil_detail(mhs)


def tambah_data(data):
    print("\n--- TAMBAH DATA ---")
    try:
        nama = input("Nama  : ").strip()
        kelas = input("Kelas : ").strip()

        if not nama or not kelas:
            raise ValueError("Nama/kelas tidak boleh kosong")

        uts = input_angka("UTS")
        uas = input_angka("UAS")
        tugas = input_angka("Tugas")

        data.append({
            "nama": nama, "kelas": kelas,
            "uts": uts, "uas": uas, "tugas": tugas
        })
        print(f"\n[v] Ditambahkan. Total: {len(data)}")
    except ValueError as e:
        print(f"[!] Gagal menambah data: {e}")
    finally:
        print("(Blok finally: proses input selesai.)")


def cari_data(data):
    if not data:
        print("Data masih kosong.")
        return
    nama = input("Nama yang dicari: ").strip()
    i = cari_indeks(data, nama)
    if i != -1:
        print(f"Ditemukan di indeks ke-{i}")
        tampil_detail(data[i])
    else:
        print("Tidak ditemukan.")


def hapus_data(data):
    """Hapus berdasarkan nama ATAU indeks dengan exception handling."""
    if not data:
        print("Data masih kosong.")
        return

    print("\n--- HAPUS DATA ---")
    print("1. Berdasarkan nama")
    print("2. Berdasarkan indeks")

    try:
        cara = input("Pilih cara: ").strip()
        if cara == "1":
            nama = input("Nama yang akan dihapus: ").strip()
            i = cari_indeks(data, nama)
            if i == -1:
                print("Tidak ditemukan.")
                return
        elif cara == "2":
            print(f"Indeks tersedia: 0 s/d {len(data) - 1}")
            i = int(input("Indeks: "))
            _ = data[i]  # memicu IndexError jika index out of range
        else:
            print("Pilihan tidak valid.")
            return

        print("\nData yang akan dihapus:")
        tampil_detail(data[i])

        yakin = input("\nYakin hapus? (y/n): ").lower()
        if yakin == "y":
            terhapus = data.pop(i)
            print(f"\n[v] '{terhapus['nama']}' dihapus. Sisa: {len(data)}")
        else:
            print("Dibatalkan.")

    except ValueError:
        print("[!] Indeks harus berupa angka.")
    except IndexError:
        print("[!] Indeks di luar jangkauan list.")
    except Exception as e:
        print(f"[!] Error lain: {e}")


def demo_error():
    print("\n--- DEMO EXCEPTION ---")
    print("1. ValueError (input bukan angka)")
    print("2. IndexError (indeks list salah)")
    print("3. ZeroDivisionError")
    print("4. raise ValueError sendiri")

    pilih = input("Pilih demo: ").strip()

    if pilih == "1":
        try:
            x = int(input("Ketik huruf (sengaja): "))
            print("Hasil:", x)
        except ValueError:
            print("[Tertangkap] ValueError: input harus angka!")
        else:
            print("Tidak ada error.")
        finally:
            print("Finally: selalu dijalankan.")

    elif pilih == "2":
        data = ["Budi", "Andi"]
        try:
            print(data[10])
        except IndexError:
            print("[Tertangkap] IndexError: indeks 10 tidak ada.")

    elif pilih == "3":
        try:
            hasil = 10 / 0
        except ZeroDivisionError:
            print("[Tertangkap] ZeroDivisionError: tidak boleh bagi 0.")

    elif pilih == "4":
        try:
            nilai = float(input("Nilai (coba > 100): "))
            if nilai < 0 or nilai > 100:
                raise ValueError("Nilai harus 0-100")
            print("Nilai OK:", nilai)
        except ValueError as e:
            print(f"[Tertangkap / raise] {e}")
    else:
        print("Pilihan tidak valid.")


def main():
    if not login():
        return

    data_mahasiswa = [
        {"nama": "Budi", "kelas": "3CS1", "uts": 80, "uas": 85, "tugas": 90},
        {"nama": "Andi", "kelas": "3CS1", "uts": 70, "uas": 75, "tugas": 80},
        {"nama": "Siti", "kelas": "3CS2", "uts": 90, "uas": 95, "tugas": 85},
    ]

    while True:
        print("\n===== MENU EXCEPTION (L14) =====")
        print(f"Jumlah data: {len(data_mahasiswa)}")
        print("1. Lihat semua data")
        print("2. Cari data")
        print("3. Tambah data")
        print("4. Hapus data")
        print("5. Demo exception (sengaja error)")
        print("6. Informasi Exception")
        print("0. Keluar")

        try:
            pilih = input("Pilihan: ").strip()
        except Exception:
            print("[!] Input bermasalah.")
            continue

        if pilih == "1":
            lihat_semua(data_mahasiswa)
        elif pilih == "2":
            cari_data(data_mahasiswa)
        elif pilih == "3":
            tambah_data(data_mahasiswa)
        elif pilih == "4":
            hapus_data(data_mahasiswa)
        elif pilih == "5":
            demo_error()
        elif pilih == "6":
            info_exception()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()