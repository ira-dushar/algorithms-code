def three_sum_brute_force(arr, M):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == M:
                    print("%d + %d + %d == %d" % (arr[i], arr[j], arr[k], M))
                    count += 1
    return count

if __name__ == "__main__":
    print("\nNumber of triples = %s" % three_sum_brute_force([3, 1, 13, 9, 21, 11, 5, 10, 6, 34], 25))
