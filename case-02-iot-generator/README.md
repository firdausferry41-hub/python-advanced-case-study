# Case 02 — Streaming Data Sensor IoT

## Masalah
Data sensor diproses secara bertahap supaya semua pembacaan tidak harus disimpan sekaligus di dalam list besar.

## Konsep Python
- **Generator function** adalah fungsi yang menghasilkan nilai bertahap.
- **`yield`** mengembalikan satu suhu setiap kali diminta.
- **Iterator pattern** memungkinkan program membaca hasil generator satu per satu.
- Kategori: Dingin jika suhu < 20°C, Normal jika 20°C sampai 30°C, dan Panas jika > 30°C.

## Cara menjalankan
```bash
python main.py
```

## Bukti eksekusi
Jalankan program di terminal, lalu ambil screenshot output dan simpan sebagai `gambar.png` di folder ini.
