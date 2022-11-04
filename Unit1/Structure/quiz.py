import random
import numpy as np
from collections import Counter

num_vector = int(input('Tamaño del vector => '))
vector = np.random.randint(15, size = num_vector)

print('----------- YOUR ARRAY -----------\n', vector)

menu = int(input('\nWhat do you want to do?\n 1. Add a element\n 2. Elimitaned a element\n 3. Enlist a element\n 4. Count a element\n 5. Calculate mean and the max number\n 6. End\n'))
while menu != 6:
    if menu == 1:
        add = int(input('Put the element => '))
        print(np.append(vector, add))
        
    elif menu == 2:
        print(vector)
        eliminated = int(input('Choose the position of the element => '))
        print(np.delete(vector, eliminated))
        
    elif menu == 3:
        for i in vector:
            print(i)
    elif menu == 5:
        sum = 0
        for i in vector:
            sum = sum + i
        elementos = len(vector)
        mean = sum/elementos
        print('The mean is =>', mean)
        max = max(vector, key=int)
        print('The max number is =>', max )
        
    elif menu == 4:
        repetido = []
        unico = []
        for x in vector:
            if x not in unico:
                unico.append(x)
            else:
                if x not in repetido:
                    repetido.append(x)
        print('valores repetidos',repetido)
    else:
        print('Error bro')
    menu = int(input('\nWhat do you want to do?\n 1. Add a element\n 2. Elimitaned a element\n 3. Enlist a element\n 4. Count a element\n 5. Calculate mean and the max number\n 6. End\n'))
