def function(child3,child2,child1):
    print("The youngest child is " + child3)

function("Emil", "Tobias", "Linus")

def function2(**kid):
    print('His last name is '+ kid['lname'])

function2(fname = "Tobias", lname = 'Cota')

def function3(food):
    for x in food:
        print(x)

fruits=['banana', 'mango', 'apple']

function3(fruits)

lista = [23,34,55,23,63,12,44,23,64,43,26,76,23]
def mayor(lista):
    max = lista[0];
    for x in lista:
        if x > max:
            max = x
    return max  

print ("El número mayor es ", mayor(lista))
