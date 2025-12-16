package main

import (
	"sort"
)

func threeSum(nums []int) [][]int {
	numsLen := len(nums)
	ans := [][]int{}
	i, j, k := 0, 1, 2
	for i < numsLen-2 {
		j = i + 1
		for j < numsLen-1 {
			k = j + 1
			for k < numsLen {
				if nums[i]+nums[j]+nums[k] == 0 {
					ans = append(ans, []int{nums[i], nums[j], nums[k]})
				}
				k += 1
			}
			j += 1
		}
		i += 1
	}
	return ans
}

func threeSum_2(nums []int) [][]int {
	sort.Ints(nums)
	numsLen := len(nums)
	ans := [][]int{}
	i, j, k := 0, 1, numsLen-1
	sumInts := 0
	for i < numsLen-2 {
		if i > 0 && nums[i] == nums[i-1] { // for main loop, also check duplication
			i++
			continue
		}

		j = i + 1
		k = numsLen - 1
		for j < k {
			sumInts = nums[i] + nums[j] + nums[k]
			if sumInts == 0 {
				ans = append(ans, []int{nums[i], nums[j], nums[k]})
				j++
				k--
				for j < k && nums[j] == nums[j-1] { // do right-shift if duplicated
					j++
				}
				for j < k && nums[k] == nums[k+1] { // do left-shift if duplicated
					k--
				}
			} else if sumInts > 0 {
				k--
			} else if sumInts < 0 {
				j++
			}
		}
		i++
	}
	return ans
}

func main() {
	// TODO: implement
	ans := threeSum_2([]int{-2, 0, 3, -1, 4, 0, 3, 4, 1, 1, 1, -3, -5, 4, 0})
	println("----------")
	for _, i := range ans {
		println(i[0], i[1], i[2])
	}

}
