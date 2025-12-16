---
title: product-of-array-except-self
leetcode: https://leetcode.com/problems/product-of-array-except-self
difficulty: medium
tags: [array, prefix sum]
status: [done, review]
lang: [Go]
---

# product-of-array-except-self

## Solution Overview

The problem limits to time complexity of $O(N)$. This suggests using something like prefix sum. For `nums[i]`, it should be the product of a sequence from prefix (`nums[0]` to `nums[i-1]`) and suffix(`nums[i+1]` to `nums[n-1]`).

* [Go Solution](./golang/product_of_array_except_self.go)

**Approach:**

`productExceptSelf` is an distinct method of how to record both `prefix` and `suffix`. Then element-wise production is done.

The advanced `productExceptSelf_2`, without further saving `prefix` and `suffix`, implements same logic directly on the `ans` array. We do same thing like prefix to ans first. Then, we accumulate the suffix product in a backward pass.

**Complexity:**
- Time: $O(N)$
- Space: $O(N)$ for saving

---

## Key Points
* Prefix problem with O(N) in time