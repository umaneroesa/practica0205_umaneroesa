#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus valores al cuadrado.
def cuadrado(numeros):
    """Funcion calcular lista al cuadrado
    Parametros:
    numeros: lista de numeros
    Salida: los numeros de la lista al cuadrado
    """
    lista=[]
    for i in numeros:
        lista.append(i**2)
    return lista
print(cuadrado([1,2,3,4,5,6]))