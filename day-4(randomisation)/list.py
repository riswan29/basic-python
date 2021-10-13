
kec_di_samosir = ['ronggur nihuta', 'pangururan',
                  'simanindo','palipi','nainggolan',
                  'onan runggu','sitio tio',
                  'sianjur mula mula',
                  'harian']
# mencetak list dari terakhir dengan menggunakan tanda minus(-)
# print(kec_di_samosir[-1]) #mencetak kec.harian

# mencetak list dari awal dimulai dari index 0 dst.
# print(kec_di_samosir[0]) #mecetak kec.ronggur nihuta

# mengganti nilai index 
# kec_di_samosir[2] = "siminindi" # mengganti nilai simanindo menjadi siminindi


# # menambahkan satu nilai list
# kec_di_samosir.append("riswan") #menambhakan list yang bernilai riswan


# menambahkan lebih dari satu list dengan menambahkan bracket ke dalam str
kec_di_samosir.extend(["riswan","indra","simbolon"])
print(kec_di_samosir)