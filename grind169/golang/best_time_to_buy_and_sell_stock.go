package main

func maxProfit(prices []int) int {
	buyPrice := 10000 // Max of prices
	profit := 0

	for _, price := range prices {
		buyPrice = min(buyPrice, price)
		profit = max(profit, price-buyPrice)
	}
	return profit
}

func main() {
	// TODO: implement
	result := maxProfit([]int{7, 1, 5, 3, 6, 4})
	println(result)
}
