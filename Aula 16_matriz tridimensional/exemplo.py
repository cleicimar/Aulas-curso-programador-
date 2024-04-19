matriz_tridimensional = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                         [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                         [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

for i in range(len(matriz_tridimensional)):
    for j in range(len(matriz_tridimensional[i])):
        for k in range(len(matriz_tridimensional[i][j])):
            print(matriz_tridimensional[i][j][k])
