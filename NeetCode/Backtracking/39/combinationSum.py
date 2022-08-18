class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        
        def helper(inp: List[int], cand: List[int], tar: int):
            if tar == 0:
                out.append(inp)
                return
            elif tar < 0:
                return
            for i, element in enumerate(cand):
                b = deepcopy(inp)
                b.append(element)
                helper(b, cand[i:], tar - element)
                
        helper([], candidates, target)
        return out
