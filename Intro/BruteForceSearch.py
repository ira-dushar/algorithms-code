def brute_force_search(arr, el):

    for i in range(len(arr)):
        if arr[i] == el:
            return i

    return None


def brute_force_output(arr, el):
    index = brute_force_search(arr, el)
    if index is not None:
        print("%d is found at index %d" % (el, index))
    else:
        print("%d not found in the array" % el)


# examples
if __name__ == "__main__":
    arr = [1, 3, 5, 6, 9, 10, 11, 13, 21, 34]
    for x in arr:
        brute_force_output(arr, x)

    brute_force_output(arr, 7)


