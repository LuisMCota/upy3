import math
pollos = lambda nombre, edad, peso, habilidades:(nombre, edad, peso, habilidades) #Declara la función del pollo 
ginger = pollos("ginger",8968410, 150, ["kung fu", "tai chichuan",])
rocky = pollos("rocky",8968300, 300, ["karate"])

años = lambda pollo:(pollo[1] / (math.pi*365**2))  #calcula años astronomicos llamando al pollo 
esjoven = lambda pollo: (años(pollo) < 5) 
esadulto = lambda pollo: not esjoven(pollo) #calcula si es joven o adulto 
desnutrido = lambda pollo: (esjoven(pollo) and pollo[2] < 50) or (esadulto(pollo) and pollo[2] < 200) or (len(pollo[0]) %2 == 0) #Revisa si es desnutrido
engordar = lambda pollo, alpiste:(pollo[0], pollo[1], pollo[2] + alpiste, pollo[3]) #Engorda, esto se usa para añadir al entrenador
arguiniano = lambda pollo: engordar(pollo, 100)
miyagi = lambda pollo: (pollo[0], pollo[1], pollo[2] ,pollo[3] + [('karate')])
marcelito = lambda pollo: (pollo[0], pollo[1], pollo[2] ,[])
raton = lambda peso, altura, bigotes: (peso, altura, bigotes) #ratón para añadir a entrenador 
brujaTapia = lambda pollo, raton: (pollo[0], pollo[1], pollo[2] + raton[0]*raton[1] - raton[2], pollo[3])
marioBross = lambda pollo, artemarcial: (pollo[0] + ' Super Mario', pollo[1], pollo[2], pollo[3]+[('saltar')] + [artemarcial])
marcenano = lambda pollo: arguiniano(marcelito(pollo))  
planeta = lambda pollo: [pollo] #se llama y se crea una lista del planeta en el que se incluyen los pollos
pollodebil = lambda pollo: len(pollo[3]) > 2 and esadulto(pollo)  
esdebil = lambda planeta: sum(map(pollodebil, planeta)) == 0
entrenar = lambda planeta, entrenador: list(map(entrenador, planeta)) 
def viajeastral(entrenadores, pollo):  #se hace función para el viaje y entrenen los pollos 
    for entrenador in entrenadores:
        pollo = entrenador(pollo)
    return pollo


print(round(años(ginger)))
print(esjoven(ginger))
print(esadulto(ginger))
print(desnutrido(ginger))
print(engordar(ginger, 100))
print(arguiniano(ginger))
print(miyagi(ginger))
print(marcelito(ginger))
print(marcenano(ginger))
print(planeta(ginger))
print(pollodebil(ginger))





