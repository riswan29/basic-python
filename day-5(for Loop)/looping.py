def input_data():
    data = []
    while True:
        tinggi = input("Masukkan tinggi badan (misal: 170): ")
        if tinggi == "":
            break
        else:
            data.append(int(tinggi))
    return data

def total_tinggi():
    data = input_data()
    total = 0
    jumlah = 0
    for tinggi in data:
        total += tinggi
    for jlh in data:
        jumlah += 1
    return total,jumlah

ukuran =total_tinggi()
rata_rata= round(ukuran[0] / ukuran[1])
print(f"total tinggi badan = {ukuran[0]} , jumlah data = {ukuran[1]} , maka rata-rata tinggi dari setiap siswa adalah {rata_rata}")

     
    