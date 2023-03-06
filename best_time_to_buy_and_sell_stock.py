class Solution:
    def maxProfit(self, prices):
        min_price, max_profit = float('inf'), 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


prices = [7, 1, 5, 3, 6, 4]

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProfit(prices))
