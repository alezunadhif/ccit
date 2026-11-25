# ==========================================
# LATIHAN 9
# PENGENALAN LIST
# ==========================================

# Data mahasiswa
nama_mahasiswa = ["Budi", "Andi", "Siti", "Alezuna"]
kelas_mahasiswa = ["3CS1", "3CS1", "3CS2", "3CS1"]

# Nilai mahasiswa
nilai_uts = [90, 70, 90, 85]
nilai_uas = [85, 75, 95, 90]
nilai_tugas = [90, 80, 85, 85]

# MENAMPILKAN DATA MAHASISWA PERTAMA
print("DATA MAHASISWA PERTAMA")
print("======================")
print("Nama  :", nama_mahasiswa[0])
print("Kelas :", kelas_mahasiswa[0])
print("UTS   :", nilai_uts[0])
print("UAS   :", nilai_uas[0])
print("Tugas :", nilai_tugas[0])

# MENAMPILKAN DAFTAR NAMA
print()
print("DAFTAR MAHASISWA")
print("================")
for nama in nama_mahasiswa:
    print(nama)

# MENAMPILKAN SEMUA DATA DENGAN FOR
print()
print("DATA SEMUA MAHASISWA")
print("====================")
for i in range(len(nama_mahasiswa)):
    print("Nama  :", nama_mahasiswa[i])
    print("Kelas :", kelas_mahasiswa[i])
    print("UTS   :", nilai_uts[i])
    print("UAS   :", nilai_uas[i])
    print("Tugas :", nilai_tugas[i])
    print("--------------------")

# MENGHITUNG RATA-RATA NILAI
rata_uts = sum(nilai_uts) / len(nilai_uts)
rata_uas = sum(nilai_uas) / len(nilai_uas)
rata_tugas = sum(nilai_tugas) / len(nilai_tugas)

print()
print("RATA-RATA NILAI")
print("===============")
print("Rata-rata UTS   :", round(rata_uts, 2))
print("Rata-rata UAS   :", round(rata_uas, 2))
print("Rata-rata Tugas :", round(rata_tugas, 2))