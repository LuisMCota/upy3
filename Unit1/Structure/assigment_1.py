

class vertice:
    def __init__(self, clave):
        self.id = clave
        self.conexiones = {}

    def incluirVecino(self, vecino,peso=0):
        self.conexiones[vecino] = peso

    def verConexiones(self):
        return self.conexiones.keys()

    def verId(self):
        return self.id

    def verPeso(self,vecino):
        return self.conexiones[vecino]

    def __str__(self):
        return str(self.id) + ' conectado con '+ str([x for x in self.verConexiones()])

vertice1 = vertice(1)
vertice1.incluirVecino(2,4), vertice1.incluirVecino(4,2)
print(vertice1)
vertice1.verId

vertice_2 = vertice(2)
vertice_2.incluirVecino(3,1), vertice_2.incluirVecino(4,1)
print(vertice_2)
vertice_2.verId

vertice_3 = vertice(4)
vertice_2.incluirVecino(2,1), vertice_2.incluirVecino(2,2)
print(vertice_2)
vertice_2.verId