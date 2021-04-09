# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = []
        levelOrderView = []
        out = []
        if root is not None:
            queue.append(root)
            
        while len(queue) > 0:
            currLevel = []
            for i in range(len(queue)):
                currTreeNode = queue.pop(0)
                currLevel.append(currTreeNode.val)
                if currTreeNode.left is not None:
                    queue.append(currTreeNode.left)
                if currTreeNode.right is not None:
                    queue.append(currTreeNode.right)
            levelOrderView.append(currLevel)
        for level in levelOrderView:
            out.append(level[len(level) - 1])
        return out

test1 = TreeNode(1)
test1.left = TreeNode(2)
test1.right = TreeNode(3)
test1.left.right = TreeNode(5)
test1.right.right = TreeNode(4)

solutionTest = Solution()
print(str(solutionTest.rightSideView(test1)))