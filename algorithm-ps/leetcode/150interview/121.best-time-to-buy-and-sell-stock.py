"""https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=study-plan-v2&envId=top-interview-150

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 주가가 아예 없거나 하루치밖에 없다면 거래를 할 수 없으므로 이익은 0
        if len(prices) < 2:
            return 0
            
        min_price = prices[0] # 가장 싼 주가, 첫 날 주가로 초기화
        max_profit = 0

        # 다음날 주가부터 탐색
        for price in prices[1:]:
            if price <= min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit