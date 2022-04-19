# En mi implementación de la Actividad 1 no hice uso de estas funciones explícitamente
# Aquí voy a definir algunas de las operaciones que calculé en forma de función para poder
# realizar los test unitarios con pytest.

# Esta función recorre x y trata de "castear" sus elementos a un float numpy de 32 bits
# Si falla, el valor se reescribe como '0'. Un string de tipo '122.3' podría castearse
# sin problema a un float y por tanto esto no arrojará excepción. Posteriormente cuando
# guardemos el dataframe como un conjunto de datos en coma flotante se forzará su conversión a un real.
import numpy as np

def correct_data(x):
    for i in range(0, len(x)):
        try:
            np.float32(x[i])
        except ValueError:
            x[i] = '0'
    return x

# Esta función devuelve la suma de los elementos mayores a 0 de una lista.
def suma_mayor_cero(x):
    return sum([i for i in x if i > 0])

# Esta función devuelve la suma de los elementos menores a 0 de una lista.
def suma_menor_cero(x):
    return sum([i for i in x if i < 0])

# Esta función devuelve la media de los elementos de una lista (o 0 si la lista está vacía).
def media_lista(x):
    return sum(x) / len(x) if(len(x) > 0) else 0

# Esta función devuelve la suma de todos los elementos de una lista.
def suma_lista(x):
    return sum(x)
