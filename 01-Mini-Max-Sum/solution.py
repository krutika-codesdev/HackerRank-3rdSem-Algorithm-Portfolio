def miniMaxSum(arr):
    total = sum(arr)
    minimum = total - max(arr)
    maximum = total - min(arr)

    print(minimum, maximum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)