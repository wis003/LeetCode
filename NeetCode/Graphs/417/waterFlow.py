class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        stack = []
        for i in range(row):
            pacific.add((i, 0))
            stack.append((i, 0))
        for j in range(1, col):
            pacific.add((0, j))
            stack.append((0, j))
        while len(stack):
            curr = stack.pop()
            if curr[0] > 0 and (curr[0] - 1, curr[1]) not in pacific and heights[curr[0] - 1][curr[1]] >= heights[curr[0]][curr[1]]:
                pacific.add((curr[0] - 1, curr[1]))
                stack.append((curr[0] - 1, curr[1]))
            if curr[0] < row - 1 and (curr[0] + 1, curr[1]) not in pacific and heights[curr[0] + 1][curr[1]] >= heights[curr[0]][curr[1]]:
                pacific.add((curr[0] + 1, curr[1]))
                stack.append((curr[0] + 1, curr[1]))
            if curr[1] > 0 and (curr[0], curr[1] - 1) not in pacific and heights[curr[0]][curr[1] - 1] >= heights[curr[0]][curr[1]]:
                pacific.add((curr[0], curr[1] - 1))
                stack.append((curr[0], curr[1] - 1))
            if curr[1] < col - 1 and (curr[0], curr[1] + 1) not in pacific and heights[curr[0]][curr[1] + 1] >= heights[curr[0]][curr[1]]:
                pacific.add((curr[0], curr[1] + 1))
                stack.append((curr[0], curr[1] + 1))
                
        for i in range(row):
            atlantic.add((i, col - 1))
            stack.append((i, col - 1))
        for j in range(col - 1):
            atlantic.add((row - 1, j))
            stack.append((row - 1, j))
        while len(stack):
            curr = stack.pop()
            if curr[0] > 0 and (curr[0] - 1, curr[1]) not in atlantic and heights[curr[0] - 1][curr[1]] >= heights[curr[0]][curr[1]]:
                atlantic.add((curr[0] - 1, curr[1]))
                stack.append((curr[0] - 1, curr[1]))
            if curr[0] < row - 1 and (curr[0] + 1, curr[1]) not in atlantic and heights[curr[0] + 1][curr[1]] >= heights[curr[0]][curr[1]]:
                atlantic.add((curr[0] + 1, curr[1]))
                stack.append((curr[0] + 1, curr[1]))
            if curr[1] > 0 and (curr[0], curr[1] - 1) not in atlantic and heights[curr[0]][curr[1] - 1] >= heights[curr[0]][curr[1]]:
                atlantic.add((curr[0], curr[1] - 1))
                stack.append((curr[0], curr[1] - 1))
            if curr[1] < col - 1 and (curr[0], curr[1] + 1) not in atlantic and heights[curr[0]][curr[1] + 1] >= heights[curr[0]][curr[1]]:
                atlantic.add((curr[0], curr[1] + 1))
                stack.append((curr[0], curr[1] + 1))
        
        out = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    out.append([i, j])
        return out
