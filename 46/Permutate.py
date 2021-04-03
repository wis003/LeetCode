# Permutations

def permute(nums):
    out = []
    if len(nums) == 0:
        return out
    
    else:
        for i in range(len(nums)):
            temp = nums[:]
            temp.remove(nums[i])
            out.append([nums[i]] + permute(temp))
        return out

test1 = [1, 2, 3]
print(str(permute(test1)))