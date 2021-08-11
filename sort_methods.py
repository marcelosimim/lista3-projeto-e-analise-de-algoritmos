
import time


def bubble(array):
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


def insert(array):
    comparisons = 0
    movements = 0
    start = time.time()

    for index in range(1, len(array)):

        value = array[index]
        i = index - 1

        comparisons += 1
        movements += 1

        while i >= 0 and array[i] > value:
            array[i+1] = array[i]
            i = i - 1
            movements += 1
        array[i+1] = value
        movements += 1

    end = time.time()
    total_time = end - start

    return comparisons, movements, total_time


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


def heap(array):
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

    return array


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        heapify(array, n, largest)
