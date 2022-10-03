from cmath import pi
class pollos():
    def __init__(self, nombre, old, kg):
        self.nombre = nombre
        self.old = old
        self.kg = kg
    
ginger = pollos('ginger', 8000000, 150)
rocky = pollos('rocky', 1000000, 300)
little = pollos('little', 500000, 100)


def edad(pollo):
    res_edad = pollo / (pi*133225)
    print('Tiene', round(res_edad), 'años de edad')

    if res_edad > 5:
        print('Es Adulto!')
    elif res_edad <= 5:
        print('Es Joven!')
    elif res_edad <= 0:
        print('Todavia no nace!')
    else:
        print('Digite otro Numero')


def salud(nombre, edad, peso):
    if peso < 50 and edad <= 5:
        print('Esta desnutrido!')
    elif peso == range(50,200) and edad > 5:
        print('Esta desnutrido!')
    elif nombre % 2 == 0:
        print('Esta desnutrido!')
    else:
        print('El pollo esta al 100%!')

print('\n-------------- POLLOS ESPACIALES ---------------')
menu = int(input('Escoge un pollo espacial \n 1. Ginger \n 2. Rocky \n 3. Little \n 4. Engordar\n 5. Alimentar\n 6. Salir\n'))
while menu != 6:
    if menu == 1:
        print('---------- Ginger -----------')
        print('Peso:',ginger.kg, 'kg')
        edad(ginger.old)
        salud(len(ginger.nombre), 19 , ginger.kg)
    elif menu == 2:
        print('---------- Rocky -----------')
        edad(rocky.old)
        salud(len(rocky.nombre), 2, rocky.kg)
    elif menu == 3:
        print('---------- Little -----------')
        edad(little.old)
        salud(len(little.nombre), 1, little.kg)
    elif menu == 4:
        print('-------------- Prueba aumentando el peso :) ---------------')
        peso_extra = int(input('Cuantos Kilos lo quieres engordar?\n'))
        pollo = int(input('\nQue pollo desea engordar?\n 1. Ginger\n 2. Rocky\n 3. Little\n 4. Regresar al menu\n'))
        while pollo != 4:
            if pollo == 1:
                peso_ginger = ginger.kg + peso_extra
                print('\nTu pollo ahora pesa: ', peso_ginger, ' kg')
            elif pollo == 2:
                peso_rocky = rocky.kg + peso_extra
                print('\nTu pollo ahora pesa: ', peso_rocky, ' kg')
            elif pollo == 3:
                peso_little = little.kg + peso_extra
                print('\nTu pollo ahora pesa: ', peso_little, ' kg')
            else:
                print('Digite un Pollo Valido')
            pollo = int(input('\nQue pollo desea engordar?\n 1. Ginger\n 2. Rocky\n 3. Little\n 4. Regresar al menu\n'))
    elif menu == 5:
        alpiste = 200
        print('           Tienes 100 kg de alpiste          ')
        alimentar = int(input('------- Elijar un pollo para alimentar -------\n 1. Ginger\n 2. Rocky\n 3. Little\n 4. Regresar al menu\n'))
        while alimentar != 4:
            if alimentar == 1:
                ginger.kg = ginger.kg + alpiste
                print('\nTu pollo ahora esta alimentado\nPesa:', ginger.kg, 'kg')
            elif alimentar == 2:
                rocky.kg = rocky.kg + (alpiste/2)
                print('\nTu pollo ahora esta alimentado\nPesa:', rocky.kg, 'kg')
            elif alimentar == 3:
                little.kg = little.kg + alpiste
                print('\nTu pollo ahora esta alimentado\nPesa:', little.kg, 'kg')
            else:
                print('Digite un Pollo Valido')
            alimentar = int(input('\n------- Elijar un pollo para alimentar -------\n 1. Ginger\n 2. Rocky\n 3. Little\n 4. Regresar al menu\n'))

    else:
        print('Digite un Pollo Valido')
    
    menu = int(input('\nEscoge un pollo espacial \n 1. Ginger \n 2. Rocky \n 3. Little \n 4. Engordar\n 5. Alimentar\n 6. Salir\n'))
