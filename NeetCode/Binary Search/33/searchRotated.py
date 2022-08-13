class Solution:
    def bsearch(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = int((l + r) / 2)
            if m < len(nums) - 1:
                if nums[m] > nums[m + 1]:
                    if target < nums[0]:
                        if self.bsearch(nums[m + 1:], target) == -1:
                            return -1
                        else:
                            return self.bsearch(nums[m + 1:], target) + m + 1
                    else:
                        return self.bsearch(nums[:m + 1], target)
                else:
                    if nums[l] < nums[m]:
                        l = m + 1
                    if nums[r] > nums[m]:
                        r = m
            else:
                break
        return self.bsearch(nums, target)
                  