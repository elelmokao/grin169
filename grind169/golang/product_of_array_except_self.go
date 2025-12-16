package main

import "fmt"

func productExceptSelf(nums []int) []int {
	lenNums := len(nums)
	ans := []int{}
	prefix := []int{1}
	suffix := []int{1}

	for idx := 0; idx < lenNums; idx++ {
		if idx > 0 {
			prefix = append(prefix, nums[idx-1]*prefix[len(prefix)-1])
		}
		if idx < lenNums-1 {
			suffix = append(suffix, nums[lenNums-(idx+1)]*suffix[len(suffix)-1])
		}
	}

	for idx, _ := range nums {
		ans = append(ans, prefix[idx]*suffix[lenNums-idx-1])
	}

	return ans
}

func productExceptSelf_2(nums []int) []int {
	accum := 1
	ans := make([]int, len(nums))

	for i := 0; i < len(nums); i++ {
		ans[i] = accum
		accum *= nums[i]
	}
	accum = 1
	for i := len(nums) - 1; i >= 0; i-- {
		ans[i] *= accum
		accum *= nums[i]
	}
	return ans
}

func main() {
	// TODO: implement
	result := productExceptSelf_2([]int{-1, 1, 0, -3, 3})
	fmt.Println(result)
}
