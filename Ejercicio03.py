#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def area(radio):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.14
    return pi*radio**2

def volumen(radio, altura):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return area(radio)*altura
print(volumen(10,15))