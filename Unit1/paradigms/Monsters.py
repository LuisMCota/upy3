import pandas as pd
gatito = ['AAAAAHG', 10, 'TRUE']
wasowski = ['uf', 2, 'FALSE']
niños = {
    'Nombre':['Luis', 'Fatima', 'Mike'],
    'Edad':[21,19,20]
}

def energiaDeGrito(monster):
    print('La energia que produjo fue de =>',len(monster[0])*monster[1]**2)

def sullivan():
    result = str(input('Select a name => '))
    
    print()

energiaDeGrito(gatito)
energiaDeGrito(wasowski)
print()
df = print(pd.DataFrame(niños))
