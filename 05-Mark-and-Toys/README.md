# Mark and Toys

## Problem Summary

Given a list of toy prices and a fixed amount of money, determine the maximum number of toys that can be purchased without exceeding the available budget.

**HackerRank:**  
https://www.hackerrank.com/challenges/mark-and-toys/problem

---

## Algorithm Used

The solution uses a greedy approach.

The toy prices are sorted in ascending order. The cheapest toys are purchased first because buying lower-priced toys allows the maximum possible number of toys to be purchased within the given budget.

---

## Key Steps

1. Read the number of toys and the available budget.
2. Read the prices of all toys.
3. Sort the prices in ascending order.
4. Start with a total cost of `0` and a toy count of `0`.
5. Iterate through the sorted prices.
6. If purchasing the current toy does not exceed the budget, purchase it and update the total cost and count.
7. Stop when the next toy cannot be purchased within the remaining budget.
8. Return the number of toys purchased.

---

## Example

**Input:**

```text
7 50
1 12 5 111 200 1000 10
```

**Output:**
```text
4
```

After sorting the prices:

```text
1 5 10 12 111 200 1000

The four cheapest toys cost:

1 + 5 + 10 + 12 = 28
```

The next toy costs `111`, which would exceed the budget of `50`.

Therefore, the maximum number of toys that can be purchased is `4`.

## Complexity Analysis

### Time Complexity

**O(n log n)**

Sorting the toy prices takes **O(n log n)** time. The subsequent traversal takes **O(n)** time, so the overall complexity is **O(n log n)**.

### Auxiliary Space Complexity

**O(1)**

The algorithm uses only a few additional variables apart from the input array. The sorting operation is performed in place in the Python implementation.

## Alternative Approach

An alternative approach would be to use a data structure such as a min-heap to repeatedly select the cheapest available toy.

However, since all toy prices are available in advance, sorting them once provides a straightforward solution with **O(n log n)** time complexity.

## Why This Solution Is Efficient

The greedy strategy of purchasing the cheapest toys first maximizes the number of toys that can be purchased within the budget.

Sorting the prices allows the algorithm to consider the cheapest options first and stop as soon as the budget cannot accommodate the next toy.

## HackerRank Result

The solution was accepted by HackerRank and passed all test cases.

**Status:** Accepted
**Score:** 10/10