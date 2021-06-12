# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Minggu, 18 April 2021 
# Deskripsi   : Program menerima N buah bilangan dan menuliskan kembali bilangan tersebut lalu dibalik

N = int(input('Masukkan nilai N =  '))

Z = []
i = 0
while i < N :
    A = int(input())
    Z.append(A)

    i += 1

print('Hasil Dibalik')
i = N - 1
while i >= 0 :
    print (Z[i])

    i -= 1




    