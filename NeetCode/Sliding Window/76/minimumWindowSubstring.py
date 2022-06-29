class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict1 = {}
        dict2 = {}
        for i in t:
            if i not in dict2:
                dict2[i] = 1
            else:
                dict2[i] += 1
        matching = 0
        p1 = 0
        p2 = 0
        out = ""
        while p2 < len(s):
            while matching != len(dict2):
                if p2 >= len(s):
                    return out
                if s[p2] not in dict1:
                    dict1[s[p2]] = 1
                else:
                    dict1[s[p2]] += 1
                if s[p2] in dict2:
                    if dict1[s[p2]] == dict2[s[p2]]:
                        matching += 1
                p2 += 1
            while matching == len(dict2):
                if p1 > p2:
                    break
                if s[p1] in dict2:
                    dict1[s[p1]] -= 1
                    if dict1[s[p1]] < dict2[s[p1]]:
                        matching -= 1
                p1 += 1 
            if out == "" or len(out) > len(s[p1 - 1:p2]):
                out = s[p1 - 1:p2]
        return out