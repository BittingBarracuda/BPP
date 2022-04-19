import funciones
import pytest

def test_correct_data():
    lista = [1, 3.14, 2.68, 10.00, "abcd", "efg", "100", 20]
    resultado = [1, 3.14, 2.68, 10.00, "0", "0", "100", 20]
    assert resultado == funciones.correct_data(lista)

def test_suma_menor_cero():
    lista = [-1, -2, 1, 2, 5, -7, 10]
    resultado = -10
    assert resultado == funciones.suma_menor_cero(lista)

def test_suma_mayor_cero():
    lista = [1, 2, 3, 4, -5, -6, 10, 20, -100]
    resultado = 40
    assert resultado == funciones.suma_mayor_cero(lista)

def test_media_lista():
    lista1 = [10, 20, 30, 40, 50]
    resultado1 = 30
    lista2 = []
    resultado2 = 0
    assert resultado1 == funciones.media_lista(lista1) and resultado2 == funciones.media_lista(lista2)

def test_suma_lista():
    lista = [1, 2, 3, 4, 5, 6]
    resultado = 21
    assert resultado == funciones.suma_lista(lista)