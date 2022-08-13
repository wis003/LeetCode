class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = int((l + r) / 2)
            if m < len(nums) - 1:
                if nums[m] > nums[m + 1]:
                    return nums[m + 1]
                else:
                    if nums[l] < nums[m]:
                        l = m + 1
                    if nums[r] > nums[m]:
                        r = m
            else:
                break
        return nums[0]
        