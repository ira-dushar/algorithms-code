import random


def sort(arr):
    # shuffle
    sort_subroutine(arr, 0, len(arr) - 1)


def sort_subroutine(arr, lo, hi):
    if lo >= hi:
        return
    pivot_index = partition(arr, lo, hi)
    sort_subroutine(arr, lo, pivot_index - 1)
    sort_subroutine(arr, pivot_index + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo + 1
    j = hi

    while True:
        while i < hi and arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        swap(arr, i, j)
        i += 1
        j -= 1

    swap(arr, lo, j)
    return j


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


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

