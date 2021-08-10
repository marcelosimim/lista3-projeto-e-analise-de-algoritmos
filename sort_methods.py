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


def quick(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        pi = partition(array, low, high)

        quick(array, low, pi-1)
        quick(array, pi+1, high)
    return array


def partition(array, low, high):
    i = (low-1)
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)


def heap(n):
    print(n)
