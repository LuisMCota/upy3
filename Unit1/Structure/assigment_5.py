'''
El metodo pop() elimina y retorna un elemento de una lista. Hay un parametro
opcional, el indice a ser eliminado de la lista, si no se especifica ningun 
indice, a.pop() elimina y retorna el ultimo elemento de la lista.
'''
from bisect import insort_right

# definimos una funcion en donde se va a poner la raiz del arbol y va a agregar dos espacios 
def ArbolBinario(raiz):
    return [raiz,[],[]]

def insertIzquierda(raiz,nuevoValor):#esta funcion sirve para agregar un valor a la raiz que ya definimos
    rama_izquierda = raiz.pop(1)# va a introducir un valor al arbol del lado izquierdo recorriendo un espacio con la funcion pop
    if len(rama_izquierda) > 1:# esirve para recorrer el arreglo y insertar el valor, luego recorrer la posicion de los valores dentro de la rama
        raiz.insert(1,[nuevoValor,rama_izquierda,[]])
    else:
        raiz.insert(1, [nuevoValor,[],[]])
        return raiz

def insertDerecha (raiz,nuevoValor):# va a agregar un avalor a la derecha de la raiz que ya definimos
    rama_derecha = raiz.pop(2)# va a empujar un espacio en el lado derecho para agregar el nuevo valos
    if len(rama_derecha) > 1:# aqui va a recorrer el arreglo y va a insertar el nuevo valor empujando a los demas valores dentro de la rama
        raiz.insert(2,[nuevoValor,[],rama_derecha])
    else:
        raiz.insert(2,[nuevoValor,[],[]])
        return raiz
#Probamos nuestras funciones creando una raiz y las ramas de estas
arbol = ArbolBinario('A')
insertIzquierda(arbol, 'B')
insertDerecha(arbol, 'C')
insertIzquierda(arbol, 'D')
insertIzquierda(arbol, 'E')
insertDerecha(arbol, 'F')
insertDerecha(arbol, 'G')

print(arbol)#lo imprimimos 

# resultado = ['A', ['E', ['D', ['B', [], []], []], []], ['G', [], ['F', [], ['C', [], []]]]]
