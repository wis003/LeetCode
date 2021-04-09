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
            
        # BFS
        while len(queue) > 0:
            currLevel = []

            # level order traversal
            for i in range(len(queue)):
                currTreeNode = queue.pop(0)
                currLevel.append(currTreeNode.val)
                if currTreeNode.left is not None:
                    queue.append(currTreeNode.left)
                if currTreeNode.right is not None:
                    queue.append(currTreeNode.right)
            levelOrderView.append(currLevel)

        # right side view is last element of each list
        for level in levelOrderView:
            out.append(level[len(level) - 1])

        return out

test1 = TreeNode(1)
test1.left = TreeNode(2)
test1.right = TreeNode(3)
test1.left.right = TreeNode(5)
test1.right.right = TreeNode(4)

test2 = TreeNode(1)
test2.left = TreeNode(2)
test2.right = TreeNode(3)
test2.left.left = TreeNode(5)

solutionTest = Solution()
print(str(solutionTest.rightSideView(test1)))
print(str(solutionTest.rightSideView(test2)))