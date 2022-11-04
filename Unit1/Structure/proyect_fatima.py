import random
import numpy as np
import statistics

matriz=[]
years=5;branches=8
def elementos():
    for inicializar in range(years):
        matriz.append([0]*branches)
    for i in range(years):
        for j in range(branches):
            matriz[i][j]=random.randint(1500,10000)

def Mostrar():
    print("La matriz es la siguiente:")
    for i in matriz:
        print(i)
    elementos()

#highest number function




#Average function

