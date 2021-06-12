# NIM / Nama  : Muhammad Fadhil Amri
# Tanggal     : selasa, 27 April 2021 
# Deskripsi   : Program memeriksa apakah B anagram dari A

A = int(input('masukkan banyaknya elemen A :'))
elemen_A = ''
elemen_B = ''
count = 0

for i in range (1, A+1):
    elemen_input_A = input(f'masukkan elemen A ke-{i}:') 
    elemen_A += elemen_input_A

B = int(input('masukkan banyaknya elemen B :'))
for x in range (1, B+1):
    elemen_input_B = input(f'masukkan elemen B ke-{x}:') 
    elemen_B += elemen_input_B


if len (elemen_A) != len(elemen_B):
    print('B bukan anagram dari A')
    

else :
    for f in elemen_A:
        for g in elemen_B:
            if g == f:
                count += 1

    if count == len(elemen_A):
        print('B adalah anagram dari A')
    
    else:
        print('B bukan anagram dari A')        



