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


def select(n):
    print(n)


def shell(n):
    print(n)


def quick(n):
    print(n)


def heap(n):
    print(n)
