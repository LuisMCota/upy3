'''Ejercicio 7
Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente

Entrada: pow(2, -3)
Salida: 0.125

Entrada: pow(3, 5)
Salida: 234'''

class potencia:
    def potencia_numero(base, exponente):
        resultado = 1
        
        for i in range(exponente):
            resultado *= base
            
        return resultado
    
base = int(input("Base de la potencia: "))
exponente = int(input("Exponente de la potencia: "))

print(base, "^", exponente, "=", potencia.potencia_numero(base, exponente))

'''Ejercicio 8
Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"'''

class inverted_string:
   
    def invert(sentence):
        inverted_sentence = ' '.join(reversed(sentence.split()))
        return inverted_sentence
    
sentence = 'mi diario python'

print(sentence)
print(inverted_string.invert(sentence))

'''Ejercicio 9
Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una cadena ingresada por el usuario y 
print_string imprime la cadena en mayúsculas.'''

class cadena():
    def __init__(self):
        self.cadena_input = ""

    def get_String(self):
        self.cadena_input = input()

    def print_String(self):
        print(self.cadena_input.upper())

print("Ingrese una oración en minusculas: ")
entrada = cadena()
entrada.get_String()
print("Oración en mayusculas: ")
entrada.print_String()

'''Ejercicio 10
Escribir una clase en python llamada rectangulo que contenga una base y una altura, y que contenga un método que devuelva el área del
 rectángulo. '''

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        resultado = self.base * self.altura

        return resultado

altura = int(input("Medidas de la altura: "))
base = int(input("Medidas de la base: "))
medidas = rectangulo(base, altura)

print("Área del rectangulo: ", medidas.area())

'''Ejercicio 11
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro 
del circulo.'''

from math import pi

class circulo:
    def __init__(self, radio):
        self.radio = radio
        
    def area(self):
        resultado_area = pi*(self.radio**2)
        return resultado_area
    
    def perimetro(self):
        resultado_perimetro = 2*pi*self.radio
        return resultado_perimetro
    
radio = int(input("Ingresa la medida del radio del circulo: "))
medidas = circulo(radio)

print("El area del circulo es: ", medidas.area())
print("El perimetro del circulo es: ", medidas.perimetro())