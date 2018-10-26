import random


def sort(arr):
    # heapify
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        sink(arr, n, i)

    # sort
    heap_size = n
    for i in range(n - 1, 0, -1):
        tmp = pop_max(arr, heap_size)
        arr[i] = tmp
        heap_size -= 1


def sink(arr, heap_size, i):
    n = heap_size
    if i < 0 or i >= n:
        raise ValueError("invalid parameter")

    while 2 * i + 1 < n:
        k = 2 * i + 1
        if 2 * i + 2 < n and arr[2 * i + 1] < arr[2 * i + 2]:
            k += 1

        if arr[i] < arr[k]:
            swap(arr, i, k)
            i = k
        else:
            break


def pop_max(arr, heap_size):
    max_el = arr[0]
    arr[0] = arr[heap_size - 1]
    sink(arr, heap_size, 0)
    return max_el


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    reversed_arr = list(reversed(range(40)))
    sort(reversed_arr)
    print(reversed_arr)

    sorted_arr = list(range(40))
    sort(sorted_arr)
    print(sorted_arr)

    random_arr = [random.randint(0, 1000) for i in range(40)]
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
