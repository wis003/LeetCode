class Solution:    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            order = str(sorted(i))
            if order not in anagrams:
                anagrams[order] = [i]
            else:
                anagrams[order].append(i)
        return list(anagrams.values())