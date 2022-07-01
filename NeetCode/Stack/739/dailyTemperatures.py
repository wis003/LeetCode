class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                curr = stack.pop()
                out[curr[1]] = i - curr[1]
            stack.append((temperatures[i], i))
        return out
                