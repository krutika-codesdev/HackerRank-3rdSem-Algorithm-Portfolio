# Binary Search

## Problem Summary

Given a sorted array and a target value, determine whether the target exists in the array using the binary search algorithm.

If the target is found, the program returns its index. Otherwise, it reports that the element is not present.

---

## Algorithm Used

The solution uses binary search, a divide-and-conquer searching technique.

The algorithm repeatedly compares the target with the middle element of the current search range. If the target is smaller, the search continues in the left half. If the target is larger, the search continues in the right half. This process continues until the target is found or the search range becomes empty.

---

## Key Steps

1. Read the sorted array and the target value.
2. Set the left boundary to the first element and the right boundary to the last element.
3. Calculate the middle index.
4. Compare the middle element with the target.
5. If they are equal, return the middle index.
6. If the target is smaller, search the left half.
7. If the target is larger, search the right half.
8. Continue until the target is found or the search range becomes empty.

---

## Example

**Input:**

```text
Sorted array: 1 3 5 7 9 11 13
Target: 7
```

**Output:**

```text
Element found at index: 3
```

The target `7` is found at index `3`.

### Target Not Found

**Input:**

```text
Sorted array: 1 3 5 7 9 11 13
Target: 6
```

**Output:**

```text
Element not found
```

Since `6` is not present in the sorted array, the search ends without finding the target.

## Complexity Analysis

### Time Complexity

**O(log n)**

At each step, binary search eliminates approximately half of the remaining search space.

### Auxiliary Space Complexity

**O(1)**

The implementation is iterative and uses only a few variables to maintain the search boundaries and middle index.

## Alternative Approach

An alternative approach is linear search, where each element is checked sequentially until the target is found.

Linear search has **O(n)** time complexity, whereas binary search reduces the search space by half at every step and has **O(log n)** time complexity.

## Why This Solution Is Efficient

The array is sorted, which allows binary search to eliminate half of the remaining elements after every comparison.

This makes binary search significantly more efficient than checking every element individually for large sorted arrays.

## HackerRank Result

This problem was implemented as the approved binary-search component of the portfolio activity because the activity instructions specify implementing a suitable sorted-array binary search rather than requiring a specifically named HackerRank challenge.

**Status:** Completed
**Test Cases:** Verified locally