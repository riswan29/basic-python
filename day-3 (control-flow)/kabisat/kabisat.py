print("tahun kabisat")

tahun = int(input("Tahun berapa sekarang ?"))

if tahun % 4 == 0:
    if tahun % 100 == 0 :
        if tahun % 400 == 0 :
            print("kabisat ")
        else:
            print("bukan kabisat")
    else:
        print("kabisat")
else:
    print("bukan kabisat")
