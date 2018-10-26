import random
import math


def sort(arr):
    h = 1
    while h <= math.ceil(len(arr)/3):
        h = 3 * h + 1

    h_sequence = []
    h //= 3

    while h > 0:
        h_sequence.append(h)
        h //= 3

    sort_using_sequence(arr, h_sequence)


def sort_using_sequence(arr, h_sequence):
    n = len(arr)

    for h in h_sequence:
        for i in range(h, n):
            tmp = arr[i]
            j = i
            while j >= h and arr[j - h] > tmp:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = tmp


if __name__ == "__main__":
    reversed_arr = list(reversed(range(40)))
    sort(reversed_arr)
    print(reversed_arr)

    sorted_arr = list(range(40))
    sort(sorted_arr)
    print(sorted_arr)

    random_arr = [random.randint(0, 100) for i in range(40)]
    sort(random_arr)
    print(random_arr)

    ones = [1] * 40
    sort(ones)
    print(ones)

    zeros_ones = [random.randint(0, 1) for i in range(40)]
    sort(zeros_ones)
    print(zeros_ones)

    one_el = [2]
    sort(one_el)
    print(one_el)

    two_els = [2, 1]
    sort(two_els)
    print(two_els)
