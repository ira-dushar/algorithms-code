from Intro.BinarySearch import binary_search_slice


def three_sum_binary_search(arr, M):
    n = len(arr)
    arr.sort()
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if binary_search_slice(arr, M - arr[i] - arr[j], j + 1, len(arr) - 1) is not None:
                print("%d + %d + %d == %d" % (arr[i], arr[j], M - arr[i] - arr[j], M))
                count += 1
    return count

# examples
if __name__ == "__main__":
    print("\nNumber of triples = %s" % three_sum_binary_search([3, 1, 13, 9, 21, 11, 5, 10, 6, 34], 25))

