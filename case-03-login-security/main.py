"""Studi Kasus 3: Sistem Keamanan Akun dan Audit Log."""

import re
from datetime import datetime


class User:
    """Menyimpan kredensial dengan validasi melalui property."""

    def __init__(self, username, password):
        self._username = ""
        self._password = ""
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if not re.fullmatch(r"[A-Za-z0-9]{5,}", value):
            raise ValueError(
                "Username harus minimal 5 karakter dan hanya berisi huruf/angka."
            )
        self._username = value

    @property
    def password(self):
        # Password tidak ditampilkan secara langsung.
        return self._password

    @password.setter
    def password(self, value):
        if not re.fullmatch(r"(?=.*\d).{8,}", value):
            raise ValueError(
                "Password harus minimal 8 karakter dan mengandung setidaknya satu angka."
            )
        self._password = value


def audit_log(func):
    """Decorator untuk mencatat setiap percobaan login."""

    def wrapper(username, password, akun):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            hasil = func(username, password, akun)
            print(f"[{waktu}] Username: {username} | Status: BERHASIL")
            return hasil
        except (ValueError, PermissionError) as error:
            print(
                f"[{waktu}] Username: {username} | Status: DITOLAK | Alasan: {error}"
            )
            return False

    return wrapper


@audit_log
def login(username, password, akun):
    """Memvalidasi format dan mencocokkan kredensial akun."""
    # Validasi input percobaan juga memakai RegEx.
    if not re.fullmatch(r"[A-Za-z0-9]{5,}", username):
        raise ValueError("format username tidak sesuai aturan")
    if not re.fullmatch(r"(?=.*\d).{8,}", password):
        raise ValueError("password terlalu pendek atau tidak mengandung angka")
    if username != akun.username or password != akun.password:
        raise PermissionError("username atau password tidak cocok")
    return True


def main():
    print("=" * 66)
    print("              SISTEM KEAMANAN AKUN & AUDIT LOG")
    print("=" * 66)

    akun = User("Aisyah23", "Belajar123")

    print("\n1. Uji username tidak valid:")
    login("Ai!", "Belajar123", akun)

    print("\n2. Uji password terlalu pendek/tanpa angka:")
    login("Aisyah23", "belajar", akun)

    print("\n3. Uji login sukses:")
    login("Aisyah23", "Belajar123", akun)


if __name__ == "__main__":
    main()
