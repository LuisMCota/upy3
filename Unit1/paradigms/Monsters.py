gatito = ['AAAAAHG', 10, 'TRUE']
wasowski = ['uf', 2, 'FALSE']

def energiaDeGrito(monster):
    print('La energia que produjo fue de =>',len(monster[0])*monster[1]**2)

energiaDeGrito(gatito)
energiaDeGrito(wasowski)