# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : selasa, 27 April 2021 
# Deskripsi   : Program memeriksa apakah suatu string itu palindrom

A = int(input('masukkan panjang string:  '))
B = input('masukkan string:  ')
x = True

for i in range(0,A):
    if B[i] == B[A-1-i]:
        pass
    else:
        x = False
        print(B,'bukan palindrom')
        break

if x == True:
    print(B,'adalah palindrom')