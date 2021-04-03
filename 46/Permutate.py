# Permutations

def permute(nums):
    out = []
    if len(nums) == 0:
        return out
    
    else:
        for i in range(len(nums)):
            out.append(list(nums[i]) + permute(nums[1:]))

    return out