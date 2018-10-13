from Intro.BinarySearch import binary_search_slice


def two_sum_binary_search(arr, M):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        if binary_search_slice(arr, M - arr[i], i + 1, len(arr) - 1) is not None:
            print("%d + %d == %d" % (arr[i], M - arr[i], M))
            count += 1
    return count

# examples
if __name__ == "__main__":
    print("\n\nNumber of pairs = %s" % two_sum_binary_search([3, 1, 13, 9, 21, 11, 5, 10, 6, 34], 11))
