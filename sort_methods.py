
import time


def bubble(array):
    comparisons = 0
    movements = 0
    start = time.time()
    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            comparisons += 1
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                movements += 3
    end = time.time()
    total_time = end - start

    return comparisons, movements, total_time


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
    comparisons = 0
    movements = 0
    start = time.time()
    for i in range(0, len(array)-1):
        min_index = i
        for j in range(i, len(array)-1):
            comparisons += 1
            if array[min_index] > array[j]:
                min_index = j
        aux = array[i]
        array[i] = array[min_index]
        array[min_index] = aux
        movements += 3
    end = time.time()
    total_time = end - start

    return comparisons, movements, total_time


def shell(array):
    comparisons = 0
    movements = 0
    start = time.time()

    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i

            while j >= interval and array[j - interval] > temp:
                comparisons += 1
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2

    end = time.time()
    total_time = end - start

    return comparisons, movements, total_time


def quick(array, low, high):
    comparisons = 0
    movements = 0
    start = time.time()

    comparisons += 1
    if len(array) == 1:
        end = time.time()
        total_time = end - start
        return comparisons, movements, total_time
    if low < high:
        pi = partition(array, low, high)

        c1, m1, t1 = quick(array, low, pi-1)
        c2, m2, t2 = quick(array, pi+1, high)
    end = time.time()
    comparisons += c1 + c2
    movements += m1 + m2
    total_time = end - start + t1 + t2

    return comparisons, movements, total_time


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
    comparisons = 0
    movements = 0
    time_aux = 0
    start = time.time()
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        c, m, t = heapify(array, n, i)
        comparisons += c
        movements += m
        time_aux += t

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        movements += 2
        c, m, t = heapify(array, i, 0)
        comparisons += c
        movements += m
        time_aux += t

    end = time.time()
    total_time = end - start + time_aux

    return comparisons, movements, total_time


def heapify(array, n, i):
    comparisons = 0
    movements = 0
    time_aux = 0
    start = time.time()

    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    comparisons += 1
    if l < n and array[i] < array[l]:
        largest = l
    comparisons += 1
    if r < n and array[largest] < array[r]:
        largest = r
    comparisons += 1
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        movements += 2
        c, m, t = heapify(array, n, largest)
        comparisons += c
        movements += m
        time_aux = t
    end = time.time()
    total_time = end - start + time_aux

    return comparisons, movements, total_time
