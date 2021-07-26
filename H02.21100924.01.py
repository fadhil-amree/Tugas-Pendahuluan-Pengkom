# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : Jum'at, 16 April 2021 
# Deskripsi   : program menerima bil N, menuliskan 1 sampai N dalam satu baris
print(5*'=' + 'program menerima bil N, menuliskan 1 sampai N dalam satu baris' +  5*'=')
N = int(input('masukkan nilai N = '))
for i in range(1,N+1):
    print(i,end=" ")
