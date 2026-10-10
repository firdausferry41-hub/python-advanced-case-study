# Case 03 — Sistem Keamanan Akun & Audit Log

## Masalah
Program memvalidasi format username dan password, lalu mencatat waktu, username, status login, dan alasan jika percobaan ditolak.

## Aturan validasi
- Username minimal 5 karakter dan hanya huruf/angka.
- Password minimal 8 karakter dan wajib mengandung angka.
- Validasi format dilakukan dengan modul `re` (RegEx).

## Konsep Python
- **Class `User` dan `@property`** mengenkapsulasi username serta password.
- **Decorator** membungkus fungsi login untuk mencatat audit log otomatis.
- **Closure** terbentuk karena fungsi `wrapper` berada di dalam `audit_log` dan membungkus fungsi yang diterima.

## Cara menjalankan
```bash
python main.py
```

## Catatan keamanan
Contoh ini untuk pembelajaran. Aplikasi nyata sebaiknya menyimpan hash password, bukan password asli.

## Bukti eksekusi
Jalankan program di terminal, lalu ambil screenshot output dan simpan sebagai `gambar.png` di folder ini.
