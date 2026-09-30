def maximumToys(prices, k):
    prices.sort()

    count = 0
    total = 0

    for price in prices:
        if total + price > k:
            break

        total += price
        count += 1

    return count


if __name__ == '__main__':
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))

    result = maximumToys(prices, k)

    print(result)