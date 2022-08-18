class Solution:
    def euclidian(self, curr: List[int]) -> float:
        return sqrt(curr[0] ** 2 + curr[1] ** 2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        out = []
        points.sort(key=self.euclidian)
        for i in range(k):
            out.append(points[i])
        return out
