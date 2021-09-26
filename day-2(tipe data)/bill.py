print("Bil pembayaran pesanan makanan ")

pesanan = input("Nama pesanan ? ")
jlh_pesanan = input("Berapa jumlah pesanan ?")
harga_pesanan = input("Harga pesanan ? ")
total = int(jlh_pesanan) * int(harga_pesanan)
print(f"anda memesan {pesanan} , dengan jumlah {jlh_pesanan} , maka total pembayaran pesanan anda {total}\n")

