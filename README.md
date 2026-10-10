# Python Advanced Topics — Studi Kasus

## Identitas Mahasiswa

- **Nama:** Mohamad Ferry Firdaus
- **NIM:** 2595114023
- **Program Studi:** Teknik Informatika
- **Mata Kuliah:** Pemrograman Berorientasi Objek

## Gambaran Proyek

Repository ini berisi tiga latihan Python yang membahas pengolahan data, pemrosesan data berurutan, serta validasi akun dan pencatatan aktivitas. Setiap kasus memiliki program utama (`main.py`) dan README tersendiri yang menjelaskan tujuan, konsep, serta cara menjalankannya.

## Studi Kasus

### 1. Pengolahan dan Pemeringkatan Nilai Mahasiswa

Program menghitung nilai akhir dari komponen tugas, UTS, dan UAS dengan bobot 30%, 30%, dan 40%. Hasilnya digunakan untuk menampilkan mahasiswa dengan nilai akhir lebih dari 80, menyusun peringkat dari nilai tertinggi, dan menentukan mahasiswa dengan nilai terbaik.

**Konsep yang digunakan:** list comprehension, lambda, filtering, dan `sorted()`.

Lokasi: `case-01-analisis-nilai/`

### 2. Pemrosesan Suhu Sensor IoT

Program mensimulasikan sepuluh pembacaan suhu. Data diberikan satu per satu menggunakan generator, kemudian setiap suhu dikelompokkan sebagai dingin (di bawah 20°C), normal (20–30°C), atau panas (di atas 30°C). Cara ini menunjukkan pemrosesan bertahap tanpa perlu menyimpan semua hasil dalam list besar.

**Konsep yang digunakan:** generator, `yield`, iterator, dan pemrosesan data bertahap.

Lokasi: `case-02-iot-generator/`

### 3. Validasi Login dan Audit Aktivitas

Program memeriksa format username dan password menggunakan RegEx. Class `User` menerapkan `@property` untuk mengatur atribut, sedangkan decorator dengan closure membantu mencatat waktu percobaan, username, status login, dan alasan ketika login gagal.

**Konsep yang digunakan:** RegEx, class dan `@property`, decorator, closure, serta audit log.

Lokasi: `case-03-login-security/`

## Struktur Folder

```text
python-advanced-case-study/
├── README.md
├── case-01-analisis-nilai/
│   ├── main.py
│   ├── README.md
│   └── gambar.png
├── case-02-iot-generator/
│   ├── main.py
│   ├── README.md
│   └── gambar.png
└── case-03-login-security/
    ├── main.py
    ├── README.md
    └── gambar.png
```

## Menjalankan Program

Pastikan Python 3 sudah terpasang. Jalankan perintah berikut dari folder utama repository:

**Kasus 1 — Nilai mahasiswa**
```bash
python case-01-analisis-nilai/main.py
```

**Kasus 2 — Sensor IoT**
```bash
python case-02-iot-generator/main.py
```

**Kasus 3 — Login dan audit log**
```bash
python case-03-login-security/main.py
```

Seluruh program menggunakan modul bawaan Python, jadi tidak memerlukan pemasangan library tambahan.

## Ringkasan

Ketiga program memperlihatkan penerapan fitur Python untuk kebutuhan yang berbeda: mengolah dan mengurutkan nilai, memproses data sensor secara bertahap, serta memeriksa data login sambil merekam aktivitasnya. README pada setiap folder memberikan penjelasan lebih khusus untuk kasus terkait.
