class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
1.递归
'''

class Solution1_1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        def helper(node1, node2):
            if not node1 or not node2: return
            
            node1.next = node2
            
            helper(node1.left, node1.right)
            helper(node2.left, node2.right)

            helper(node1.right, node2.left)
        
        helper(root.left, root.right)
        return root


'''
2. BFS
'''
from collections import deque
class Solution2_1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:#node is the last one
                    node.next = None
                else:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return root


'''
3.将每一行当成链表来处理,避免使用队列
'''
class Solution3_1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        cur_node = root
        while cur_node != None:
            dummy = Node(0)
            child_node = dummy
            
            while cur_node != None and cur_node.left != None:
                child_node.next = cur_node.left
                child_node = child_node.next
                child_node.next = cur_node.right
                child_node = child_node.next

                cur_node = cur_node.next
            
            cur_node = dummy.next

        return root

'''由于是完全二叉树，可以进一步优化，不用dummy'''
class Solution3_2:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        head = root
        cur = None
        while head.left:
            cur = head
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            
            head = head.left
        return root