# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        pass

'''
解法1:递归
'''
#按照遍历框架
class Solution1_1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #base case
        if not root: return root

        #preorder
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

#pythonic
class Solution1_2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #base case
        if not root: return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

'''
2. BFS
'''
class Solution2_1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root

        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            # 先交换，再将子节点添加到队列，顺序相反也可以
            node.left, node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return root

'''
3. DFS
'''
class Solution3_1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return root

        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        
        return root