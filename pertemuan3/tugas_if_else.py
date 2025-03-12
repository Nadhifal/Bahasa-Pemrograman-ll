import os

nama = str(input("Nama  : "))
Nik = int(input("NIK   : "))
status = str(input("Status Pegawai (Tetap/Honor)  : ")).casefold()
golongan = str(input("Golongan (A/B/C): "))

if status == "tetap" :
    gaji = 1000000

    if golongan == "A" :
        bonus = 200000

    elif golongan == "B" :
        bonus = 400000

    elif golongan == "C" :
        bonus = 550000

if status == "honor" :
    gaji = 750000

    if golongan == "A" :
        bonus = 15000

    elif golongan == "B" :
        bonus = 275000

    elif golongan == "C" :
        bonus = 480000

total = gaji + bonus

os.system("cls")

print("Nama     : ",nama)
print("NIK      : ",Nik)
print("Status   : ",status)
print("Golongan : ",golongan, "\n")
print("Gaji : ",gaji)
print("Bonus: ",bonus)
print("Total: ",total)

