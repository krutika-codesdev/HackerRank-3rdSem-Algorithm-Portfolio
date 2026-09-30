# Birthday Cake Candles

## Problem Summary

Given an array representing the heights of birthday cake candles, determine how many candles have the maximum height.

The program returns the number of candles that have the tallest height.

**HackerRank:**  
https://www.hackerrank.com/challenges/birthday-cake-candles/problem

---

## Algorithm Used

The solution finds the maximum candle height and then counts how many times that height occurs in the array.

---

## Key Steps

1. Read the number of candles.
2. Read the candle heights into an array.
3. Find the maximum candle height.
4. Count the number of candles equal to the maximum height.
5. Return the count.

---

## Example

**Input:**

```text
4
3 2 1 3
```
**Output:**

```text
2
```

The maximum candle height is 3.

There are two candles with height 3, so the answer is 2.

## Complexity Analysis

### Time Complexity

**O(n)**

The array is traversed to find the maximum height and to count the occurrences of that height.

### Auxiliary Space Complexity

**O(1)**

No additional data structure proportional to the input size is required.

## Alternative Approach

An alternative approach is to sort the candle heights first and then count how many elements at the end of the sorted array are equal to the maximum element.

However, sorting requires **O(n log n)** time, while directly finding and counting the maximum requires only **O(n)** time.

## Why This Solution Is Efficient

The solution avoids sorting the entire array. It only needs to identify the maximum height and count its occurrences, resulting in linear time and constant auxiliary space.

## HackerRank Result

The solution was accepted by HackerRank and passed all test cases.

**Status:** Accepted
**Score:** 10/10