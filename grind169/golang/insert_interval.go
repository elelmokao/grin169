package main

func insert(intervals [][]int, newInterval []int) [][]int {
	ansIntervals := [][]int{}
	isInserted := false
	for _, interval := range intervals {
		if interval[1] < newInterval[0] { // not overlapped, before newInterval
			ansIntervals = append(ansIntervals, interval)
		} else if interval[0] > newInterval[1] { // not overlapped, after newInterval
			if !isInserted {
				ansIntervals = append(ansIntervals, newInterval)
				isInserted = true
			}
			ansIntervals = append(ansIntervals, interval)
		} else { // overlapped, update newInterval
			newInterval[0] = min(newInterval[0], interval[0])
			newInterval[1] = max(newInterval[1], interval[1])
		}
	}
	if !isInserted {
		ansIntervals = append(ansIntervals, newInterval)
	}
	return ansIntervals
}

func insert_2(intervals [][]int, newInterval []int) [][]int {
	ansIntervals := [][]int{}
	for idx, interval := range intervals {
		if interval[1] < newInterval[0] { // not overlapped, before newInterval
			ansIntervals = append(ansIntervals, interval)
		} else if interval[0] > newInterval[1] { // not overlapped, after newInterval
			ansIntervals = append(ansIntervals, newInterval)
			return append(ansIntervals, intervals[idx:]...)
		} else { // overlapped, update newInterval
			newInterval[0] = min(newInterval[0], interval[0])
			newInterval[1] = max(newInterval[1], interval[1])
		}
	}
	return append(ansIntervals, newInterval)
}

func main() {
	results := insert_2([][]int{{1, 2}, {3, 5}, {6, 7}, {8, 10}, {12, 16}}, []int{4, 8})
	for _, result := range results {
		println(result[0], result[1])
	}
}
