#Escribir una función que reciba un número entero positivo y devuelva su factorial. Realiza el ejercicio mediante bucles interactivos y mediante una función recursiva.
def factorial (n):
    """ Realizar funcion de factorial

    Parametros:
    n= numero entero
    Salida: n
    """
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
