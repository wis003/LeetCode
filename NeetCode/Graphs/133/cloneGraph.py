"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        clones = {}
        
        stack = [node]
        while len(stack):
            curr = stack.pop()
            if curr.val not in clones:
                temp = []
                for i in curr.neighbors:
                    temp.append(i.val)
                clones[curr.val] = temp
                stack += curr.neighbors
        
        newMap = {}
        for key, _ in clones.items():
            newMap[key] = Node(val=key)
        for key, value in clones.items():
            temp = []
            for i in value:
                temp.append(newMap[i])
            newMap[key].neighbors = temp
        return newMap[node.val]
        
