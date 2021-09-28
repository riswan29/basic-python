# hint
# dibawah 18,5 = berat badan kurang
# 18,5 - 22,9 = berat badan normal
# 23-29,9 = berat badan berlebih
# 30 keatas = obesitas

print("Kalkulator BMI")

tinggi = float(input("Masukkan tinggi badan anda (m) : "))
berat = float(input("Masukkan berat badan anda (Kg) :" ))
bmi = round(berat / tinggi ** 2 )

# if statement
if bmi > 30 :
    print(f"Nilai BMI anda {bmi} ,Berat badan anda mencapai obesitas")
elif bmi >= 23:
    print(f"Nilai BMI anda {bmi} ,Berat badan berlebih (hampir mencapai obesitas)")
elif bmi >= 18.5:
    print(f"Nilai BMI anda {bmi} , Berat badan normal")
else:
    print(f"Nilai BMI anda {bmi} , Berat badan kurang")