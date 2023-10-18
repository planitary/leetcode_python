"""
给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：

输入：root = [3,9,20,null,null,15,7]
输出：3
"""
from typing import Optional, List
import collections

from LeetCode.binaryTree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # // 使用层序遍历获取树的深度
        if root is None:
            return 0
        queue_node = collections.deque()
        queue_node.append(root)
        level = 0
        while len(queue_node) > 0:
            size = len(queue_node)
            for i in range(size):
                current_node:TreeNode = queue_node.popleft()
                if current_node.left is not None:
                    queue_node.append(current_node.left)
                if current_node.right is not None:
                    queue_node.append(current_node.right)
            level += 1
        return level

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
    nodes = [3,9,20,None,None,15,7]
    root:TreeNode = s.create_Tree(nodes,0)
    print(s.maxDepth(root))
