class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        m = prices[0]
        for i in prices:
            m = min(i, m)
            out = max(out, i - m)
        return out
        