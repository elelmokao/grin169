---
title: insert-interval
leetcode: https://leetcode.com/problems/insert-interval
difficulty: medium
tags: [array]
status: [review]
lang: [Go]
---

# insert-interval

## Solution Overview

* [Go Solution](./golang/insert_interval.go)

**Approach:**

The given approach use for loop to check whether the `intervals[i]` is overlapped with `newInterval` or not. It should be noted that how to ensure if:
1. `newInterval` is ahead of / after `intervals`
2. `newInterval` is not overlapped with `intervals`
In the approach `insert()`, we update `newInterval` if merge is happened.
In the approach `insert_2()`, without flag of `isInserted`, we return earlier if the newInterval is inserted yet.

**Complexity:**
- Time: $O(N)$
- Space: $O(N)$

---

## Key Points
