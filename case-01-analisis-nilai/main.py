"""Studi Kasus 1: Analisis Nilai Mahasiswa."""

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 88, "uts": 91, "uas": 86},
]

# List comprehension untuk menambahkan nilai akhir ke setiap data mahasiswa.
mahasiswa_dengan_nilai = [
    {
        **m,
        "nilai_akhir": round(m["tugas"] * 0.30 + m["uts"] * 0.30 + m["uas"] * 0.40, 2),
    }
    for m in data_mahasiswa
]

# Filter mahasiswa yang nilai akhirnya di atas 80.
mahasiswa_berprestasi = [
    m for m in mahasiswa_dengan_nilai if m["nilai_akhir"] > 80
]

# Urutkan dari nilai akhir tertinggi ke terendah dengan lambda.
ranking = sorted(
    mahasiswa_dengan_nilai,
    key=lambda m: m["nilai_akhir"],
    reverse=True,
)

print("=" * 58)
print("             ANALISIS NILAI MAHASISWA")
print("=" * 58)
print("DAFTAR NILAI AKHIR:")
for m in mahasiswa_dengan_nilai:
    print(f'{m["nama"]:<10} NIM: {m["nim"]} | Nilai akhir: {m["nilai_akhir"]:.2f}')

print("\nMAHASISWA BERP​​RESTASI (nilai akhir > 80):".replace("\u200b", ""))
for m in mahasiswa_berprestasi:
    print(f'- {m["nama"]}: {m["nilai_akhir"]:.2f}')

print("\nRANKING MAHASISWA:")
for nomor, m in enumerate(ranking, start=1):
    print(f'{nomor}. {m["nama"]} (NIM {m["nim"]}) — {m["nilai_akhir"]:.2f}')

terbaik = ranking[0]
print("\nMAHASISWA TERBAIK:")
print(f'Nama       : {terbaik["nama"]}')
print(f'NIM        : {terbaik["nim"]}')
print(f'Tugas      : {terbaik["tugas"]}')
print(f'UTS        : {terbaik["uts"]}')
print(f'UAS        : {terbaik["uas"]}')
print(f'Nilai akhir: {terbaik["nilai_akhir"]:.2f}')
