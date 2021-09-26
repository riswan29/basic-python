
# 1#####
# num = input("")
# angka1 = num[0]
# angka2 = num[1]
# print(int(angka1) + int(angka2))


# 2######
# print(3*((3+3)/3)-3)


#3#####

# bmi

# tinggi = input("masukkan tinggi anda dalam m :  ")
# berat = input("masukkan berat anda dalam kg:  ")

# bmi = float(berat) / int(tinggi) ** 2
# int_bmi = int(bmi)
# print(int_bmi)

# #### 4
# dengan menggunakan f-string kita tidak perlu lagi mengkonvert tipe data lain ke dalam sting 
# dikarenakan fungsi f-string akan mengubah secara otomatis bilangan apapun ke dalam string
# tinggi = 12
# lebar = 12

# luas = lebar * tinggi
# print(f"luas persegi tersebut adalah  {tinggi * lebar}cm")

# #### 5
# challenge menentukan sisa waktu dalam 90 tahun
age = input("berapa umur mu sekarang ?")

tahun = 30 - int(age)
sisa_hari = tahun * 365
sisa_minggu = tahun * 52
sisa_tahun = tahun * 12

print(f"sisa hari kamu adalah {sisa_hari},{sisa_minggu} minggu dan {sisa_tahun} bulan")

