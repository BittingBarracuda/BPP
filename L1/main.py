import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class CustomException(Exception):
    pass

# Esta función recorre x y trata de "castear" sus elementos a un float numpy de 32 bits
# Si falla, el valor se reescribe como '0'. Un string de tipo '122.3' podría castearse
# sin problema a un float y por tanto esto no arrojará excepción. Posteriormente cuando
# guardemos el dataframe como un conjunto de datos en coma flotante se forzará su conversión a un real.
def correct_data(x):
    for i in range(0, len(x)):
        try:
            np.float32(x[i])
        except ValueError:
            x[i] = '0'
    return x

def main():
    # Primero escribo el apartado 2 para leer el fichero y comprobar
    # que el contenido está bien formado y puedo operar sobre él

    # Utilizamos pandas para leer el fichero csv
    # Utilizamos una estructura try - except para controlar las posibles excepciones que se puedan dar
    df = None
    try:
        df = pd.read_csv('finanzas2020[1].csv', sep = '\t', dtype='string')
        # Comprobamos si el fichero tiene 12 columnas.
        if len(df.columns.tolist()) != 12:
            # En caso contrario lanzamos una excepción indicando el error.
            raise CustomException("Deben existir 12 columnas, una para cada mes del año!")

        # Comprobamos si todas las columnas tienen algún tipo de contenido
        # Para ello utilizamos una función lambda -> lambda x: len(x) > 0
        # Esta función toma cada columna y comprueba que tiene algún elemento
        # El resultado de cada columna se irá almacenando en una lista de booleanos.
        # Utilizamos la función all() para computar una AND con todos los elementos de dicha lista.
        if not all(df.apply(lambda x: len(x) > 0, axis = 0).tolist()):
            raise CustomException("Alguna fila no tiene contenido")
        
        # Para comprobar si los datos son correctos, vamos a tratar de guardar el dataframe
        # convirtiendo los datos a enteros numpy de 32 bits. En caso de que se genere alguna excepción, 
        # la capturaremos y eliminaremos los datos incorrectos.
        df = df.astype(np.int32)
    except FileNotFoundError:
        print("Fichero no encontrado o imposible de leer")
    except ValueError:
        print("Alguno de los valores contenidos en el dataframe no es de tipo numérico")
        print("Eliminando datos incorrectos...")
        df.apply(correct_data, axis = 0)
        # Una vez se han retirado los datos no numéricos, convertimos el dataframe
        # a un conjunto de datos del tipo np.float32
        df = df.astype(np.float32)
        print("Datos incorrectos eliminados.")
    
    if df is not None:
        meses = df.columns.tolist()
        # 1.- Calculamos los gastos de cada mes
        gastos = df.apply(lambda x: sum(i for i in x if i < 0))
        # 2.- Calculamos los ingresos de cada mes
        ingresos = df.apply(lambda x: sum(i for i in x if i > 0))
        # 3.- Media de gastos del año
        media_gastos = np.mean(gastos)
        # 4.- Gasto total del año
        gasto_total = np.sum(gastos)
        # 5.- Ingresos totales del año
        ingreso_total = np.sum(ingresos)

        # Mostramos la información por pantalla
        print(f"Gastos de cada mes -> \n{gastos}\n")
        print(f"Mes con mayor gasto {meses[np.argmin(gastos)]}\n\n")
        print(f"Ingresos de cada mes -> \n{ingresos}\n\n")
        ahorros = ingresos + gastos
        print(f"Ahorros de cada mes -> \n{ahorros}\n")
        print(f"Mes con mas ahorro {meses[np.argmax(ahorros)]}")
        print(f"Media de gastos anual -> {media_gastos}")
        print(f"Gastos totales del año -> {gasto_total}")
        print(f"Ingresos totales del año -> {ingreso_total}")
        
        plt.plot(meses, ingresos)
        plt.xlabel("Meses")
        plt.ylabel("Ingresos en €")
        plt.title("Ingresos mensuales")
        plt.show()

if __name__ == "__main__":
    main()