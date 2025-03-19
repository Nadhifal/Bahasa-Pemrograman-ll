
jumlah_pegawai = int(input("Masukkan jumlah pegawai: "))

for i in range(jumlah_pegawai):
    print("\nPegawai ke-{i+1}")
    
    nama = input("Nama: ")
    nik = input("NIK: ")
    status = input("Status Pegawai (Tetap/Honor): ").strip().lower()
    golongan = input("Golongan (A/B/C): ").strip().upper()

    # Menentukan gaji berdasarkan status dan golongan
    if status == "tetap":
        gaji = 1000000
        bonus = 200000 if golongan == "A" else 400000 if golongan == "B" else 550000 if golongan == "C" else 0
    elif status == "honor":
        gaji = 750000
        bonus = 150000 if golongan == "A" else 275000 if golongan == "B" else 480000 if golongan == "C" else 0
    else:
        print("Status pegawai tidak valid!")
        continue

    total = gaji + bonus

    # Menampilkan hasil
    print("\n=== Detail Gaji ===")
    print(f"Nama     : {nama}")
    print(f"NIK      : {nik}")
    print(f"Status   : {status.capitalize()}")
    print(f"Golongan : {golongan}")
    print(f"Gaji     : Rp{gaji:,}")
    print(f"Bonus    : Rp{bonus:,}")
    print(f"Total Gaji: Rp{total:,}\n")

print("Perhitungan selesai!")
