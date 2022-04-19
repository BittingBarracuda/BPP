from primePy import primes
import pdb

pdb.set_trace()

def num_primos(lista):
    return list(filter(primes.check, lista))

def maximo_lista_listas(lista):
    res = [max(sub_lista) for sub_lista in lista]
    return res
    
if __name__ == "__main__":
    lista = [[2, 4, 1], [1, 2, 3, 4, 5, 6, 7, 8], [100, 250, 43]]
    print(f"Máximo de cada lista -> {maximo_lista_listas(lista)}")
    nums = [3, 4, 8, 5, 5, 22, 13]
    print(f"Primos de la lista -> {num_primos(nums)}")