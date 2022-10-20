def symetric(matrix,orden):
    
    simetrica = True
    for i in range(orden):
        for j in range(orden):
            if(matrix[i][j]!=matrix[j][i]):
                simetrica=False
    return simetrica



rows = int(input('Enter number of rows => '))
cols  = int(input('Enter number of column => '))

print('Enter values for matrix')
matrix = [[int(input(f"column {j+1} -> Enter {i+1} element: ")) for j in range(cols)] for i in range(rows) ]  

print('\n---------Matrix---------')

for i in matrix:
    print(i)

respuesta = symetric(matrix,len(matrix))
if respuesta == True:
    print('\nSymmetric')
else:
    print('\nNo symmetric')