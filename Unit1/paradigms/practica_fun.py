import math
import cmath

class mov():
    def __init__(self):
        self.direccion = []
        self.ejex = int(input('Put the value of x => '))
        self.ejey = int(input('Put the value of y => '))

pepe = ('Pepe', 34,'M',['Campana', 'Zarate'])
lucho = ('Lucho', 60, 'M', ['Campana', 'Casa Matriz'])
lola = ('Lola', 45, 'F', ['Buenos Aires', 'Campana'])

def factorial(num):
    print(math.factorial(num))

def cuadratica(a,b,c):
    dis = (b**2) - (4 * a*c)
    ans1 = (-b-cmath.sqrt(dis))/(2 * a)
    ans2 = (-b + cmath.sqrt(dis))/(2 * a)
  
    print('The roots are',ans1,'&', ans2)

def signo(num):
    if num > 0:
        print('Positive')
    elif num < 0:
        print('Negative')
    else:
        print('Is neutral')
        
def factoriales(num):
    lista = []
    p = 1
    for i in range(1,num+1):
        lista.append(i)
    for numeros in lista:
        p = p * numeros
    print('El factorial de', num, 'es', p)

def palabras(input):
    def contar_vocales(input):
        contador = 0
        for letra in input:
            if letra.lower() in "aeiouAEIOU":
                contador += 1
        return contador

    def check(input):
        vocals = contar_vocales(input)
        consonants = len(input)-vocals
        if vocals < consonants:
            print('Have more consonats!')
        elif vocals > consonants:
            print('Have more vocals!')
        else:
            print('Have the same vocals and consonants')
    print('The word have',contar_vocales(input), 'vocals')
    check(input)

def acronims(phrase):
    oupt = phrase[0]
    for i in range(1, len(phrase)):
        if phrase[i-1] == ' ':
            oupt += phrase[i]
    oupt = oupt.upper()
    return oupt

def movimientos(mov1,mov2):
    x = mov1.ejex + mov2.ejex
    y = mov1.ejey + mov2.ejey
    
    if x > 0 and y > 0:
        mov.direccion = 'Northeast'
    elif x < 0 and y > 0:
        mov.direccion = 'Northwest' 
    elif x < 0 and y < 0:
        mov.direccion = 'Southwest'
    elif x > 0 and y < 0:
        mov.direccion = 'Southeast'
    elif x == 0 and y < 0:
        mov.direccion = 'West'
    elif x == 0 and y > 0:
        mov.direccion = 'east'
    elif x < 0 and y == 0:
        mov.direccion = 'South'
    elif x > 0 and y == 0:
        mov.direccion = 'North'

    distancia = cmath.sqrt((mov2.ejex-mov1.ejex)**2+(mov2.ejey-mov1.ejey)**2) 
    print('\nPoint 1({},{})'.format(mov1.ejex,mov1.ejey))
    print('Point 2({},{})'.format(mov2.ejex,mov2.ejey))
    print(mov.direccion, '({},{}) la distancia entre los puntos es {}'.format(x,y,distancia))

def empleados(empleado):
    first = [x for x in empleado[3]]
    print('The first sucursal of {} is {}'.format(empleado[0],first[0]))
    for i in empleado[3]:
        if i == 'Casa Matriz':
            print('{} works in Casa Matriz'.format(empleado[0]))
        else:
            print('FALSE')

    

'''number = int(input('Put a number sir => '))
factorial(number)
number = int(input('\nPut a number sir => '))
factoriales(number)
signo(number)
a = int(input('\nPut a number a => '))
b = int(input('Put a number b => '))
c = int(input('Put a number c => '))
cuadratica(1,2,1)
word = str(input('\nPut a word => '))
palabras(word)
frase = str(input('\nPut a phrase => '))
print(acronims(frase))
print('\nPut the depazamiento of the cardinal points according to the x-axis and y-axis')
mov_1 = mov()
print('The next cardinal point:')
mov_2 = mov()
movimientos(mov_1, mov_2)'''
empleados(pepe)
empleados(lucho)
empleados(lola)

