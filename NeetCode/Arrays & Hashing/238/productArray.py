class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix, output = [], [], []
        precurr, postcurr = 1, 1
        for i in range(len(nums)):
            precurr *= nums[i]
            postcurr *= nums[len(nums) - 1 - i]
            prefix.append(precurr)
            postfix.insert(0, postcurr)
        for i in range(len(prefix)):
            premul, postmul = 0, 0
            if i == 0:
                premul = 1
                postmul = postfix[i + 1]
            elif i == len(prefix) - 1:
                premul = prefix[i - 1]
                postmul = 1
            else:
                premul = prefix[i - 1]
                postmul = postfix[i + 1]
            output.append(premul * postmul)
        return output
                