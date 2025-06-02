# Meminta input jumlah baris dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris piramida: "))

# Perulangan untuk membuat piramida
for i in range(1, jumlah_baris + 1):
    spasi = jumlah_baris - i  # Menghitung jumlah spasi di kiri
    bintang = 2 * i - 1       # Menghitung jumlah bintang di setiap baris
    print(" " * spasi + "*" * bintang)
