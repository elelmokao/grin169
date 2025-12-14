package main

func twoSum(nums []int, target int) []int {
	nummap := make(map[int]int)
	for idx, num := range nums {
		if pair_idx, ok := nummap[target-num]; ok {
			return []int{pair_idx, idx}
		}
		nummap[num] = idx
	}
	return []int{0, 1}
}

func main() {
	result := twoSum([]int{3, 2, 4}, 6)
	println(result[0], result[1])
}
