# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        out, queue = [[root.val]], [[root]]
        while len(queue) > 0:
            currOut, currQueue = [], []
            temp = queue.pop(0)
            for i in temp:
                if i.left:
                    currOut.append(i.left.val)
                    currQueue.append(i.left)
                if i.right:
                    currOut.append(i.right.val)
                    currQueue.append(i.right)
            if len(currOut) > 0:
                out.append(currOut)
                queue.append(currQueue)
        return out
