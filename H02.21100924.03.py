# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Jum'at, 16 April 2021 
# Deskripsi   : Program menerima bilangan X dan apakah X prima

X = int(input('masukkan nilai X = '))
i = 2

while i < X :
    
    if X % i == 0:
        A = ( ' x bukan bilangan prima')  
        break  
    else :
        A = ('x adalah bilangan prima')
    i +=1

print(A)
