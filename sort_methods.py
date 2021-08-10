def bubble(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def insert(array):
    for index in range(1, len(array)):

        value = array[index]
        i = index - 1

        while i >= 0 and array[i] > value:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = value

    return array


def select(array):
    for i in range(0, len(array)-1):
        min_index = i
        for j in range(i, len(array)-1):
            if array[min_index] > array[j]:
                min_index = j
        aux = array[i]
        array[i] = array[min_index]
        array[min_index] = aux
    return array


def shell(n):
    print(n)


def quick(n):
    print(n)


def heap(n):
    print(n)
