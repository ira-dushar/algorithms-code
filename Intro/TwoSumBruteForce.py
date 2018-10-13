def two_sum_brute_force(arr, M):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == M:
                print("%d + %d == %d" % (arr[i], arr[j], M))
                count += 1
    return count


# examples
if __name__ == "__main__":
    print("\n\nNumber of pairs = %s" % two_sum_brute_force([3, 1, 13, 9, 21, 11, 5, 10, 6, 34], 11))
