
nama_costumer = input("Masukkan nama costumer: ")

print(f"Selamat datang, {nama_costumer}!")

data_belanja = []

while True:
    print("\nMenu:")
    print("1. Belanja")
    print("2. Tampilkan Keranjang")
    print("3. Checkout")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama_barang = input("Masukkan nama barang: ")
        harga_satuan = int(input("Masukkan harga satuan barang: "))
        qty = int(input("Masukkan jumlah qty: "))
        data_belanja.append({
            "nama": nama_barang,
            "qty": qty,
            "harga_satuan": harga_satuan
        })
        print(f"Berhasil menambahkan {qty} {nama_barang} ke keranjang belanja")

    elif pilihan == "2":
        total_harga = 0
        print("Keranjang Belanja:")
        for i, barang in enumerate(data_belanja, start=1):
            total_harga += barang["qty"] * barang["harga_satuan"]
            print(f"{i}. {barang['nama']}: {barang['qty']} x {barang['harga_satuan']} = {barang['qty'] * barang['harga_satuan']}")
        print(f"Total Harga: {total_harga}")

    elif pilihan == "3":
        total_harga = 0
        print("Nota Belanja:")
        print(f"Nama Costumer: {nama_costumer}")
        for i, barang in enumerate(data_belanja, start=1):
            total_harga += barang["qty"] * barang["harga_satuan"]
            print(f"{i}. {barang['nama']}: {barang['qty']} x {barang['harga_satuan']} = {barang['qty'] * barang['harga_satuan']}")
        print(f"Total Harga: {total_harga}")
        print("Terima kasih telah berbelanja!")
        data_belanja = []

    elif pilihan == "4":
        break

    else:
        print("Pilihan tidak valid")
