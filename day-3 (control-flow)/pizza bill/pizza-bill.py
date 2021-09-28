pizza = input("Size pizza ? s(small) , m(medium) , l(large)")
tambahan_daging = input("Mau tambahan daging ? y or n")
ekstra_keju = input("Mau tambahan ekstra keju ? y or n ")
harga = 0

if pizza == "s":
    harga += 70000
elif pizza == "m":
    harga += 100000
elif pizza == "l":
    harga += 150000
else:
    harga
    
if tambahan_daging == "y":
    harga += 30000
if ekstra_keju == "y":
    harga += 20000
    print(f"Total pembayaran : Rp.{harga}")
else:
    print(f"Total semua menjadi {harga}")
