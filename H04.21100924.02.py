# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : selasa, 27 April 2021 
# Deskripsi   : Program matriks N X M

import numpy as np
N = int(input('masukkan N: '))
M = int(input('masukkan M: '))
A = [[0 for j in range (M)] for i in range (N)]
positif = 0

for i in range(1, N+1):
    for x in range(1, M+1):
        A[i-1][x-1] = int(input(f'masukkan nilai A[{i}][{x}] :  '))
        if A[i-1][x-1] > 0:
            positif += 1

print('ada', positif,'bilangan positif di matriks.')
print(np.array(A))
        