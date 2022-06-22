class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        sortedCount = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        result = []
        
        for i in sortedCount:
            if k > 0:
                result.append(i)
                k -= 1
            else:
                break
        return result