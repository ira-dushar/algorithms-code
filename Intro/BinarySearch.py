def binary_search(arr, el):
    return binary_search_slice(arr, el, 0, len(arr) - 1)


def binary_search_slice(arr, el, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == el:
            return mid
        elif arr[mid] > el:
            hi = mid - 1            # search left side
        else:
            lo = mid + 1            # search right side

    return None


def binary_search_output(arr, el):
    index = binary_search(arr, el)
    if index is not None:
        print("%d is found at index %d" % (el, index))
    else:
        print("%d not found in the array" % el)


# examples
if __name__ == "__main__":
    arr = [1, 3, 5, 6, 9, 10, 11, 13, 21, 34]
    for x in arr:
        binary_search_output(arr, x)

    binary_search_output(arr, 7)

