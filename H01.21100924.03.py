# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Jum'at, 16 April 2021 
# Deskripsi   : Menentukan bilangan positif, nol, atau negatif

angka = int(input('masukkan angka = '))

if angka > 0 :
    
    if angka % 2 == 0 :
        print( str(angka), 'adalah bilangan positif genap' )
    else :
        print( str(angka), 'adalah bilangan positif ganjil')
    
elif angka < 0:
    print( str(angka), 'adalah bilangan negatif')
else :
    print( str(angka), 'adalah bilangan nol')