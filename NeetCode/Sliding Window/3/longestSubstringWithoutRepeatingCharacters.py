class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        out = 0
        curr = set()
        leftPointer = 0
        for i in range(len(s)):
            if s[i] not in curr:
                curr.add(s[i])
            else:
                while s[leftPointer] != s[i]:
                    curr.remove(s[leftPointer])
                    leftPointer += 1
                leftPointer += 1
            out = max(out, len(curr))
        return out