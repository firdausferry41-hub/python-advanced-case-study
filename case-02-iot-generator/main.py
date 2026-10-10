"""Studi Kasus 2: Streaming Data Sensor IoT Hemat Memori."""

def baca_sensor(jumlah=10):
    """Menghasilkan suhu satu per satu tanpa membuat list besar."""
    suhu_sensor = [18.5, 19.8, 20.0, 22.4, 25.6, 29.9, 30.0, 31.2, 34.7, 37.5]
    for suhu in suhu_sensor[:jumlah]:
        yield suhu


def kategori_suhu(suhu):
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    print("=" * 48)
    print("       STREAMING DATA SENSOR CUACA IoT")
    print("=" * 48)
    sensor = baca_sensor(10)  # sensor adalah generator/iterator
    for nomor, suhu in enumerate(sensor, start=1):
        print(f"Pembacaan {nomor:02}: {suhu:>4.1f} °C | Status: {kategori_suhu(suhu)}")


if __name__ == "__main__":
    main()
