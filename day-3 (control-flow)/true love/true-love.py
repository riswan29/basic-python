print("True Love Calkulator")

your_name = input("Nama Kamu ? \n")
your_lover = input("Nama Doi ? \n")

gabung_nama = your_name + your_lover

lower_case_string = gabung_nama.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

skor_love = int(str(true) + str(love))

if(skor_love < 10 ) or (skor_love > 90):
    print(f"Love score anda {skor_love}% , Kamu cocok dan serasi bersamanya ")
elif (skor_love >= 40) and (skor_love <= 50):
    print(f"Skor love anda {skor_love}% , kamu serasi bersamanya")
else:
    print(f"Skor love anda {skor_love}%")

