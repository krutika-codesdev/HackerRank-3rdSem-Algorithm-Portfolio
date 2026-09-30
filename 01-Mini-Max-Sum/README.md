# Mini-Max Sum

## Problem Summary

Given five positive integers, find the minimum and maximum sums that can be calculated by summing exactly four of the five integers.

The program prints the minimum sum and maximum sum as two space-separated integers.

**HackerRank:**  
https://www.hackerrank.com/challenges/mini-max-sum/problem

---

## Algorithm Used

The solution uses the total sum of all five elements.

- The minimum sum is obtained by excluding the largest element.
- The maximum sum is obtained by excluding the smallest element.

Therefore:

- `minimum = total_sum - maximum_element`
- `maximum = total_sum - minimum_element`

---

## Key Steps

1. Read the five integers into an array.
2. Calculate the total sum of all elements.
3. Find the largest element using `max()`.
4. Find the smallest element using `min()`.
5. Subtract the largest element from the total to obtain the minimum sum.
6. Subtract the smallest element from the total to obtain the maximum sum.
7. Print both values.

---

## Example

**Input:**

```text
1 2 3 4 5
```

**Output:**
```text
10 14
```

The minimum sum is:

1 + 2 + 3 + 4 = 10

The maximum sum is:

2 + 3 + 4 + 5 = 14

## Complexity Analysis

### Time Complexity

**O(n)**

The array is traversed to calculate the sum, minimum, and maximum. Since the problem always contains five elements, this is effectively constant time, but the general complexity is **O(n)**.

### Auxiliary Space Complexity

**O(1)**

No additional data structure proportional to the input size is created. Only a few variables are used for the calculations.

## Alternative Approach

An alternative approach is to sort the array first and then:

- Sum the first four elements to obtain the minimum sum.
- Sum the last four elements to obtain the maximum sum.

However, sorting requires **O(n log n)** time, making it less efficient than directly using the total sum with the minimum and maximum elements.

## Why This Solution Is Efficient

The solution avoids sorting the array. By calculating the total sum once and identifying the minimum and maximum elements, both required sums can be obtained directly.

This results in a linear-time solution with constant auxiliary space.

## HackerRank Result

The solution was accepted by HackerRank and passed all test cases.

**Status:** Accepted
**Score:** 10/10