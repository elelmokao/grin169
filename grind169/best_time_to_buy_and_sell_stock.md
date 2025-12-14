---
title: best-time-to-buy-and-sell-stock
leetcode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
difficulty: easy
tags: [array, dynamic programming]
status: [todo]
lang: [Go]
---

# best-time-to-buy-and-sell-stock

## Solution Overview

* [Go Solution](./golang/best-time-to-buy-and-sell-stock.go)

**Approach:**

Key point is to find out the minimal value in `prices`. There is no possible answer that sell price - (second min after min) is larger than sell price - min. 

**Complexity:**
- Time: $O(N)$
- Space: $O(1)$

---

## Key Points
