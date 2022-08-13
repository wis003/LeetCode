class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return True
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        lastCol = len(matrix[0]) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # print(pivot)
            if pivot == 0 and matrix[pivot][lastCol] >= target:
                # print("a")
                return self.search(matrix[pivot], target)
            if pivot == len(matrix) - 1 and matrix[pivot][lastCol] >= target:
                # print("b")
                return self.search(matrix[pivot], target)
            if pivot + 1 <= len(matrix) - 1:
                if matrix[pivot][lastCol] < target and matrix[pivot + 1][lastCol] >= target:
                    # print("c")
                    return self.search(matrix[pivot + 1], target)
            if pivot - 1 >= 0:
                if matrix[pivot][lastCol] >= target and matrix[pivot - 1][lastCol] < target:
                    # print("d")
                    return self.search(matrix[pivot], target)
            if target <= matrix[pivot][lastCol]:
                # print("no")
                right = pivot - 1
            else:
                left = pivot + 1
        return False