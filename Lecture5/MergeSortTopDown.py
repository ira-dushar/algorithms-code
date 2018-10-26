import random


def sort(arr):
    aux = [None] * len(arr)
    sort_subroutine(arr, aux, 0, len(arr) - 1)


def sort_subroutine(arr, aux, lo, hi):
    if lo >= hi:
        return
    mid = (lo + hi) // 2
    sort_subroutine(arr, aux, lo, mid)
    sort_subroutine(arr, aux, mid + 1, hi)
    merge(arr, aux, lo, mid, hi)


def merge(arr, aux, lo, mid, hi):
    if arr[mid] <= arr[mid + 1]:
        return

    i = lo
    j = mid + 1

    aux[lo:hi + 1] = arr[lo:hi + 1]
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi or aux[i] < aux[j]:
            arr[k] = aux[i]
            i += 1
        else:
            arr[k] = aux[j]
            j += 1

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

