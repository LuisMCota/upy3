'''
El metodo pop() elimina y retorna un elemento de una lista. Hay un parametro
opcional, el indice a ser eliminado de la lista, si no se especifica ningun 
indice, a.pop() elimina y retorna el ultimo elemento de la lista.
'''
from bisect import insort_right


def ArbolBinario(raiz):
    return [raiz,[],[]]

def insertIzquierda(raiz,nuevoValor):
    rama_izquierda = raiz.pop(1)
    if len(rama_izquierda) > 1:
        raiz.insert(1,[nuevoValor,rama_izquierda,[]])
    else:
        raiz.insert(1, [nuevoValor,[],[]])
        return raiz

def insertDerecha (raiz,nuevoValor):
    rama_derecha = raiz.pop(2)
    if len(rama_derecha) > 1:
        raiz.insert(2,[nuevoValor,[],rama_derecha])
    else:
        raiz.insert(2,[nuevoValor,[],[]])
        return raiz

arbol = ArbolBinario('A')
insertIzquierda(arbol, 'B')
insertDerecha(arbol, 'C')
insertIzquierda(arbol, 'D')
insertIzquierda(arbol, 'E')
insertDerecha(arbol, 'F')
insertDerecha(arbol, 'G')

print(arbol)
