from unittest import result


baobab = ['Baobab',5,10,1.7]
maple = ['Maple',6,7,10]

def frondoso(arbol):
    if arbol[1] >= 6 and arbol[1] <= 15 and arbol[2] > arbol[1] and arbol[3] > 1:
        print('El arbol',arbol[0],'es frondoso')
    else:
        print('El arbol',arbol[0],'no es frondoso')

def vida(arbol):
    print('La esperanza de vida de tu arbol es de:',(arbol[3]*45)/2)

def fact_climaticos(arbol):
    def lluvia(arbol):
        choose = str(input('Llovio? '))
        if choose =='si' or choose == 'Si' or choose == 's':
            lluvia = int(input('Cuantos mm llovio? '))
            altura = arbol[1]+1
            vitalidad = arbol[3]+lluvia%arbol[3]
            print('Ahora',arbol[0],'mide', altura, 'y su vitalidad incremento a', round(vitalidad))
        else:
            print('OK')

    def granizo(arbol):
        granizo = str(input('Granizo? '))
        if granizo == 'si' or granizo == 'Si' or granizo == 's':
            result = arbol[1] - 2
            if result >= 1:
                print('Ahora tu arbol mide', result)
            else:
                print('OK')
    
    def tormenta(arbol):
        altura = arbol[1]+1-2
        vitalidad = arbol[3]+arbol[3]
        print('\nLos datos de {} quedan asi:\n 1. Altura => {}\n 2. Vitalidad => {}\n'.format(arbol[0], altura, vitalidad))

    lluvia(arbol)
    granizo(arbol)
    tormenta(arbol)

def buen_dia(arbol):
    result = 150%arbol[3]+arbol[3]
    if result > 5:
        print('Es un buen dia para tu arbol {} :) '.format(arbol[0]))
    else:
        print('Fue un mal dia para {} :('.format(arbol[0]))


print()
frondoso(baobab)
frondoso(maple)
print()
vida(baobab)
vida(maple)
print()
fact_climaticos(baobab)
fact_climaticos(maple)
print()
buen_dia(baobab)
buen_dia(maple)
print()