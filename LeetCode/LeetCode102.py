# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


"""
示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]
"""
from typing import Optional, List
import collections


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res_LL = []
        if root is None:
            return res_LL
        node_queue = collections.deque()
        node_queue.append(root)
        while len(node_queue) != 0:
            node_ll = []
            size = len(node_queue)
            for i in range(size):
                current_node: TreeNode = node_queue.popleft()
                if current_node is not None:
                    if current_node.left is not None:
                        node_queue.append(current_node.left)
                    if current_node.right is not None:
                        node_queue.append(current_node.right)
                node_ll.append(current_node.val)
            res_LL.append(node_ll)
        return res_LL

    def create_Tree(self, ll: List[int], index: int) -> TreeNode:
        root = None
        if index < len(ll):
            if ll[index] is not None:
                root = TreeNode(ll[index])
                root.left = self.create_Tree(ll, index * 2 + 1)
                root.right = self.create_Tree(ll, index * 2 + 2)
        return root


if __name__ == "__main__":
    s = Solution()
    nodes = [3, 9, 20, None, None, 15, 7]
    node: TreeNode = s.create_Tree(nodes, 0)
    print(s.levelOrder(node))
