# Insertion Sort – Part 1

## Problem Summary

Given an array in which the first `n - 1` elements are already sorted, insert the last element into its correct position while maintaining the sorted order.

The program prints the array after each shift and after the element is inserted into its correct position.

**HackerRank:**  
https://www.hackerrank.com/challenges/insertionsort1/problem

---

## Algorithm Used

The solution uses the insertion sort technique.

The last element is stored as the value to be inserted. Starting from the element before it, each element greater than the value is shifted one position to the right. Once the correct position is found, the stored value is inserted there.

---

## Key Steps

1. Store the last element of the array as the value to be inserted.
2. Start comparing it with the elements to its left.
3. If the current element is greater than the value, shift it one position to the right.
4. Print the array after each shift.
5. Continue until the correct position is found.
6. Insert the stored value at that position.
7. Print the final sorted array.

---

## Example

**Input:**

```text
5
2 4 6 8 3
```
**Output:**

```text
2 4 6 8 8
2 4 6 6 8
2 4 4 6 8
2 3 4 6 8
```

The value `3` is initially at the end of the array.

It is compared with the elements on its left:

- `8` is shifted right.
- `6` is shifted right.
- `4` is shifted right.
- `3` is inserted before `4`.

The resulting sorted array is:
```text
2 3 4 6 8
```

## Complexity Analysis

### Time Complexity

**O(n)**

In the worst case, the last element may need to be compared with and shift past all preceding elements.

### Auxiliary Space Complexity

**O(1)**

Only a few variables are used, and no additional data structure proportional to the input size is required.

## Alternative Approach

A general insertion sort implementation could repeatedly insert each element into the sorted portion of the array.

However, this problem specifically requires inserting only the final element into an already sorted portion, so processing just that element avoids unnecessary work.

## Why This Solution Is Efficient

The first `n - 1` elements are already sorted, so there is no need to sort the entire array.

The solution only shifts elements that are greater than the final element and then places the element in its correct position. This gives **O(n)** worst-case time and **O(1)** auxiliary space.

## HackerRank Result

The solution was accepted by HackerRank and passed all test cases.

**Status:** Accepted
**Score:** 10/10