def three_sum_bucket_search(arr, M):
    n = len(arr)

    bucket = [0] * 100001

    for i in range(len(arr)):
        bucket[arr[i]] = i

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = bucket[M - arr[i] - arr[j]]
            if k is not None and k > j:
                print("%d + %d + %d == %d" % (arr[i], arr[j], M - arr[i] - arr[j], M))
                count += 1
    return count

# examples
if __name__ == "__main__":
    print("\nNumber of triples = %s" % three_sum_bucket_search([3, 1, 13, 9, 21, 11, 5, 10, 6, 34], 25))
