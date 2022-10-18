import pandas as pd
gatito = ['AAAAAHG', 10, 'TRUE']
wasowski = ['uf', 2, 'FALSE']

def energiaDeGrito(monster):
    print('La energia que produjo fue de =>',len(monster[0])*monster[1]**2)

sullivan = lambda niño: (len(niño[0])*'A'+'GH', 20/niño[1], True if niño[1]>3 else False )
vocales = lambda palabra: palabra.count('a') + palabra.count('e') + palabra.count('i') + palabra.count('o') + palabra.count('u')
Randall = lambda niño: ('Mamamdera', vocales(niño[0].lower()), True if niño[2] >= 0.8 and niño[2] <= 1.2 else False)
ChuckNorris = lambda niño: ('abcdefghijklmnopqrstuvwxyz', 1000, True)
aplicacion = lambda funciones, elemento: list(map(lambda funcion: funcion(elemento), funciones))
team = lambda monstruos, niño: aplicacion(monstruos, niño)
niño = lambda nombre, edad, altura: (nombre, edad, altura)

energiaDeGrito(gatito)
energiaDeGrito(wasowski)
niño1= niño('Luis', 21, 1.75)
print(sullivan(niño1))
print(Randall(niño1))
print(ChuckNorris(niño1))
niño2 = niño('Boo', 6, 96)
print(aplicacion([str.lower, str.upper], "AaAaAAa"))
print(team([sullivan, Randall, ChuckNorris], niño2))
