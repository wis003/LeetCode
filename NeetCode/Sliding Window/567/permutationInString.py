class Solution:
    def checkEqual(self, dict1, dict2):
        for i in dict1:
            if i not in dict2:
                return False
            if dict1[i] != dict2[i]:
                return False
        return True
        
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        dict2 = {}
        
        for i in s1:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] += 1

        curr = s2[0:len(s1)]
        for j in curr:
            if j not in dict2:
                dict2[j] = 1
            else:
                dict2[j] += 1
                
        if self.checkEqual(dict1, dict2):
            return True
        
        p1 = 0
        for i in range(len(s1), len(s2)):
            if s2[i] not in dict2:
                dict2[s2[i]] = 1
            else:
                dict2[s2[i]] += 1
            dict2[s2[p1]] -= 1
            if self.checkEqual(dict1, dict2):
                return True
            p1 += 1
            
        return False