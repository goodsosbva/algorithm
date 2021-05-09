from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


stocks = [7, 1, 5, 3, 6, 4]
sol = Solution()
chk = sol.maxProfit(stocks)
print(chk)