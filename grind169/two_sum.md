---
title: two_sum
leetcode: https://leetcode.com/problems/two-sum
difficulty: easy
tags: [array, hash-table]
status: [done]
lang: [Go]
---

# two_sum

## Solution Overview

* [Go Solution](./golang/two_sum.go)

**Approach:**
- Use a hashmap to store previously seen numbers and their indices: `(num, index)`
- For each element, check if `target - num` exists in the hashmap before inserting the current number.

**Complexity:**
- Time: $O(N)$
- Space: $O(N)$

---

## Key Points

1. **No Solution Case:**
	- If no answer is found, return `nil` at the end of the loop.
2. **Duplicate Elements:**
	- Always check for `target - num` before inserting `num` into the hashmap to avoid using the same element twice.