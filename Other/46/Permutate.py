# Permutations

def permute(nums):
    out = []
    if len(nums) == 1:
        return [nums]
    
    else:
        for i in range(len(nums)):
            temp = nums[:]
            temp.remove(nums[i])
            for permutations in permute(temp):
                out.append([nums[i]] + permutations)
        return out

test1 = [1, 2, 3]
test2 = [0, 1]
test3 = [1]
print(str(permute(test1)))
print(str(permute(test2)))
print(str(permute(test3)))