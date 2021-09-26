jlh_nama = len(input("siapa nama kamu ?"))
# apabila kita langsung memprint jlh karakter ke dalam string makan akan terjadi error 
# karena var jlh nama menghsilkan nilai integer 
# jadi pada saat memprint nilai string tidak dapat mencetak 2 jenis tipe data sekaligus 
# jadi untuk mengatasinya kita harus mengubah nilai integer ke string dengan menggunakan function *str*

new_jlh_nama = str(jlh_nama)

# maka var jlh_nama sudah berubah menjadi string
# kemudian kita menggantikan var jlh_nama menjadi new_jlh_nama 
# dan dapat di print secara langsung
print("nama kamu memilih " + new_jlh_nama + " huruf.")

# begitu juga dengan tipe data lainnya 
# kita bisa menggunakan fungsi tipe data lain untuk mengubah tipe data tersebut
# seperti float str int dan boolean
# exp
print(1234 + 4567) #integer + integer
print(str(1234) + str(4567)) #string + string