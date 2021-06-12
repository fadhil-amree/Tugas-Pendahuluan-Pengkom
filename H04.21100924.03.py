# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : selasa, 27 April 2021 
# Deskripsi   : Program matriks segitiga pascal
import numpy as np
N = int(input('masukkan N : '))

A = [[1 for j in range (N)] for i in range(N)]

for i in range (1,N):
    for j in range (1, N):
        A[i][j] = A[i-1][j] + A[i][j-1]

print(np.array(A))