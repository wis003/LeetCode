class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            m = int((l + r) / 2)
            if sum(ceil(curr / m) for curr in piles) > h:
                l = m + 1
            else:
                r = m - 1
        return l