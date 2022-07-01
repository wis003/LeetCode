class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stacks = []
        for i in range(n):
            if i == 0:
                out.append("(")
                stacks.append(["("])
            else:
                curr = []
                stacks_curr = []
                temp = len(out)
                for j in range(temp):
                    temp2 = len(stacks[j])
                    for k in range(temp2 + 1):
                        add = ""
                        stacks_add = deepcopy(stacks[j])
                        for l in range(k):
                            add += ")"
                            stacks_add.pop()
                        
                        curr.append(out[j] + add + "(")
                        stacks_add.append("(")
                        stacks_curr.append(stacks_add)
                out = curr
                stacks = stacks_curr
        for i in range(len(out)):
            for j in range(len(stacks[i])):
                out[i] += ")"
        return out
                        