'''Ejercicio 1
Escribir una clase en python que convierta un número entero a número romano'''

my_number = int(input("Write a number: "))

def roman(number):

    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rom = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    while number:
        div = number // arabic[i]
        number %= arabic[i]

        while div:
            print(rom[i], end = '')
            div -= 1
        i -= 1

print("1. Roman value is:", end = " ")
roman(my_number)

'''Ejercicio 2
Escribir una clase en python que convierta un número romano en un número entero'''

class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

my_number_1 = str(input('\nYour number: '))
print('2. Your number: ', py_solution().roman_to_int(my_number_1))

'''Ejercicio 3
Escribir una clase en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['  ']. Los paréntesis deben 
aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos, pero "[)", "({[)]" y "{{{" son inválidos.'''

class string_validation:
    def string_true(string):
        list = []
        parenthesis = {'{':'}', '(':')', '[':']'}


        for i in string:
            if i in parenthesis:
                list.append(i) 
            elif len(list) == 0 or i!= parenthesis[list.pop()]:
                return False


        return len(list) == 0

string = input("Please insert the parenthesis string to validate: ")
print('3. Is ',string, '=', string_validation.string_true(string))

'''Ejercicio 4
Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.
Entrada: [4, 5, 6]
Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]'''

class unique_subsets:
    def subsets(input):
        return recursive_subsets([], sorted(input))

def recursive_subsets(actual, set):
    if set:
        return recursive_subsets(actual, set[1:]) + recursive_subsets(actual + [set[0]], set[1:])
    return [actual]

input = [4, 5, 6]
result = unique_subsets.subsets(input)
print('4. ', result)

'''Ejercicio 5
Escribir una clase en python que encuentre un par de elementos (índice de los números) de una matriz dada cuya suma es igual a un número de destino especifico.
Entrada: numeros = [10,20,10,40,50,60,70], objetivo=50
Salida: 3, 4'''

class indice_numeros:
    def suma_indices(entrada, objetivo):
        indices = {}

        for i, n in enumerate(entrada):
            if objetivo - n in indices:
                return indices[objetivo - n], i
            
            indices[n] = i

numeros = [10,20,10,40,50,60,70]
objetivo = 50

salida = indice_numeros.suma_indices(numeros, objetivo)
print('5. ', salida)

'''Ejercicio 6
Escribir una clase en python que encuentre los 3 elementos que sumen 0 a partir de números reales
Entrada: [-25, -10, -7, -3, 2, 4, 8, 10]
Salida: [[-10, 2, 8], [-7, -3, 10]]'''

from itertools import combinations
from tkinter import N

class elements_sum:
    def sum_cero(entrada):
        sub_tres = list(combinations(entrada, 3))
        sublists = []

        for i in sub_tres:
            if sum(i) == 0:
                sublists.append(i)
        
        return sublists

input = [-25, -10, -7, -3, 2, 4, 8, 10]
ANS = elements_sum.sum_cero(input)

print('6. ',ANS)
