import random


def sort(arr):
    n = len(arr)
    for i in range(1, n):
        tmp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > tmp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = tmp


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

    one_el = [2]
    sort(one_el)
    print(one_el)

    two_els = [2, 1]
    sort(two_els)
    print(two_els)
