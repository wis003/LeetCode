class Solution:
    def climbStairs(self, n: int) -> int:
        output = [1 for _ in range(n + 1)]
        for i in reversed(range(n - 1)):
            output[i] = output[i + 1] + output[i + 2]
        return output[0]
