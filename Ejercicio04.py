#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media(numeros):
    """Funcion de calcular la media de numeros
    Parametros:
    numeros: lista de numeros
    Salida: devuelva su media
    """
    return sum(numeros)/len(numeros)
print(media([1,2, 3, 4,5, 6]))