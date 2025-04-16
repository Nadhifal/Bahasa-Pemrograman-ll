matriks_list_1 = [
    [1,2,3,4,5],
    [2,1,3,4,5],
    [2,1,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
matriks_list_2 = [
    [1,2,3,4,5],
    [2,1,3,4,5],
    [2,1,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]
matriks_hasil = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
   
]


for i in range(5) :
    for j in range(5) :
        for k in range(5) :
            matriks_hasil[i][k] += matriks_list_1[i][j] * matriks_list_2[j][k]


print("Hasil perkalian matriks A x B:")
for baris in matriks_hasil:
    print(baris)