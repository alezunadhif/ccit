# print("Hello World! \n Nama Saya Nadhif \n Dari kelas 3CS1")

# name = "Alezuna M. Nadhif Pohan"
# kelas = "3CS1"

# print(f"Nama saya {name}, dari kelas {kelas}")

name2 = input("Nama  : ")
kelas2 = input("Kelas : ")

# print(f"Nama {name2} Kelas {kelas2}")

uts = float(input("Nilai UTS: "))
uas = float(input("Nilai UAS: "))
tugas = float(input("Nilai Tugas: "))

tugas_bulat = round(tugas)
avg = (uts + uas + tugas) / 3

print(f"Nama {name2} Kelas {kelas2} Rata-rata Nilai(UTS, UAS, & Tugas): {avg}")
