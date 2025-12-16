---
title: 3sum
leetcode: https://leetcode.com/problems/3sum
difficulty: medium
tags: [array, two pointers, sorting]
status: [done, review]
lang: [Go]
---

# 3sum

## Solution Overview

* [Go Solution](./golang/3sum.go)

The hardest part of the problem is how to avoid duplicated set in the answer array.

### Approach: Brute force
`threeSum()` just checks the array with 3 for loop. But it cannot easily solve the duplicated (we need to build set).

**Complexity:**
- Time: $O(N^3)$
- Space: $O(N)$ for saving answer

---
### Approach: Two Pointer
`threeSum_2()` uses a for loop with two pointers to check a SORTED array. If the sum is positive, right pointer should do left-shift and if the sum is negative, left pointer should do right-shift.

We should also note for the way we deal with the depulicated set -- we additionally do while loop to check if the pointer points to same number or not.

**Complexity:**
- Time: $O(N^2)$
- Space: $O(N)$ for saving answer

---
## Key Points
* Know brute-force method of O(N^3)
* Two pointer