# Responsavel por gerar os vetores de tamanho 'n' conforme a necessidade
from random import randint


def ordered_array(n):
    array = []
    for i in range(0, n):
        array.append(i+1)
    return array


def disordered_array(n):
    array = []
    for i in range(n, 0, -1):
        array.append(i)
    return array


def random_array(n):
    array = []
    for i in range(0, n):
        array.append(randint(1, n))
    return array


def partially_random_array(n):
    array = []
    for i in range(0, n):
        if i < n*0.1:
            array.append(randint(1, n))
        else:
            array.append(i+1)
    return array
