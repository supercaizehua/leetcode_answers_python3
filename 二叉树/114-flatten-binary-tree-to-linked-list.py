'''
1. recursion
'''
# 后序遍历
class Solution1_1:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #base case
        if not root: return root
        
        self.flatten(root.left)
        self.flatten(root.right)

		#operate root
        temp = root.right
        root.left, root.right = None, root.left
        head = root
        while head.right:
        	head = head.right
        head.right = temp
        
        return root

# 前序遍历
class Solution1_2:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #base case
        if not root: return root
        
        right = root.right
        root.left, root.right = None, root.left

        p = root
        while p.right:
            p = p.right
        p.right = right

        self.flatten(root.left)
        self.flatten(root.right)

        return root