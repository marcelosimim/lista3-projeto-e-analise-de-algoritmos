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


def shell(array):
    n = len(array)
    gap = n/2

    sublistcount = len(array)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            for i in range(startposition+gap, len(array), gap):
                currentvalue = alist[i]
                position = i

                while position >= gap and array[position-gap] > currentvalue:
                    array[position] = array[position-gap]
                    position = position-gap

                array[position] = currentvalue

    return array


def quick(n):
    print(n)


def heap(n):
    print(n)
