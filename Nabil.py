#buat variabel untuk ngambil inputan
ingput = input("Masukkan nilai-nilai numerik, pisahkan dengan koma : ")

#dipisahin nomor2 nya biar jadi list
listi = ingput.split(",")

#ubah string menjadi float
listi = [float(nilai) for nilai in listi]

#menghitung rata-rata
ratatoulie = sum(listi) / len(listi)

#print hasil akhir
print('Nilai rata-rata nya adalah : ', ratatoulie)