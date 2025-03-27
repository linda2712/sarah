# Daftar untuk menyimpan data pendaftar
pendaftar_list = []
n = int(input("Input Jumlah Pendaftar: "))

# Input data pendaftar
for i in range(n):
    print(f"\nInput Data Pendaftar ke-{i + 1}:")
    nama = input("Nama: ")
    mata_kuliah = input("Mata kuliah yang diminati: ")
    nilai_wawancara = int(input("Nilai wawancara (rentang 1-100): "))
    nilai_tes_tulis = int(input("Nilai tes tulis (rentang 1-100): "))
    nilai_mengajar = int(input("Nilai mengajar (rentang 1-100): "))

    # Hitung nilai rata-rata
    nilai_rata_rata = (nilai_wawancara + nilai_tes_tulis + nilai_mengajar) / 3

    # Tentukan predikat
    if nilai_rata_rata > 80:
        predikat = "LULUS"
    else:
        predikat = "TIDAK LULUS"

    # Simpan data pendaftar
    pendaftar_list.append({
        'nomor': i + 1,
        'nama': nama,
        'mata_kuliah': mata_kuliah,
        'nilai_rata_rata': nilai_rata_rata,
        'predikat': predikat
    })

# Output hasil penilaian untuk setiap pendaftar
print("\nHasil Penilaian Pendaftar:")
for pendaftar in pendaftar_list:
    print(f"Nomor Pendaftar: {pendaftar['nomor']}")
    print(f"Nama: {pendaftar['nama']}")
    print(f"Mata Kuliah: {pendaftar['mata_kuliah']}")
    print(f"Nilai Rata-rata: {pendaftar['nilai_rata_rata']:.2f}")
    print(f"Predikat: {pendaftar['predikat']}\n")