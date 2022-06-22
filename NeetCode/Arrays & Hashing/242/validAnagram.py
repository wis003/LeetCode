class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}
        for i in s:
            if i not in s_count:
                s_count[i] = 1
            else:
                s_count[i] += 1
        for i in t:
            if i not in t_count:
                t_count[i] = 1
            else:
                t_count[i] += 1
        for i in s_count:
            if i not in t_count:
                return False
            elif s_count[i] != t_count[i]:
                return False
        for i in t_count:
            if i not in s_count:
                return False
            elif s_count[i] != t_count[i]:
                return False
        return True