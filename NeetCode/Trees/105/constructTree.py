# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        valueToIndex = {}
        for i, val in enumerate(inorder):
            valueToIndex[val] = i
        
        rootIndex = 0
        def subtree(left, right) -> Optional[TreeNode]:
            nonlocal rootIndex
            if left > right:
                return None
            
            root = TreeNode(val = preorder[rootIndex])
            inorderIndex = valueToIndex[root.val]
            rootIndex += 1
            root.left = subtree(left, inorderIndex - 1)
            root.right = subtree(inorderIndex + 1, right)
            return root
        
        return subtree(0, len(inorder) - 1)
