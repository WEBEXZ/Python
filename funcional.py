def suma(x, y):
    return x + y
#Lista de elementos
lista = [1, 2, 3, 4]
lista2 = [10, 10, 10, 10]
listaMap = map(suma, lista, lista2)
print listaMap

def positivo(x):
    return (x > 0)
listaNumeros = [1, -10, -20, -78.6, 80, 100]
listaFilter = filter(positivo, listaNumeros)
print listaFilter

def multiplicacion(x, y):
    return x * y
listaReduce = reduce(multiplicacion, lista)
print listaReduce
