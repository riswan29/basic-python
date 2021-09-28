print("Bill Tiket Rollercoaster")

tinggi = float(input("Tinggi badan ? "))
umur = int(input("Umur ? "))
bayar = 0
if tinggi > 120:
  if umur < 12:
    bayar = 20000
    print("Anak anak => total pembayaran Rp.20.000")
  if umur <= 18:
    bayar = 30000
    print("Remaja => total pembayaran Rp.30.000 ")
  if umur > 18:
    bayar = 50000
    print("Dewasa => total pembayaran Rp.50.000")
  print("Untuk pengmbilan foto dikenai biaya sebesar Rp.5.000")
  t_foto = input("Apakah anda ingin dengan foto sekaligus ? y or n : ")
  if t_foto == "y":
    bayar += 5000
    print(f"Total pembayaran semua menjadi {bayar}")
  else:
    print(f"Total pembayaran semua menjadi {bayar}\n")
  print("Selamat bersenang senang !!! ")
else:
  print("Maaf tinggi anda belum mencapai batas minimum untuk mengikuti wahana ini.")
