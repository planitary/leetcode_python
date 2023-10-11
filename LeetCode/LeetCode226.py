"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
示例 2：
输入：root = [2,1,3]
输出：[2,3,1]
示例 3：

输入：root = []
输出：[]
"""
from typing import Optional

from LeetCode.binaryTree import TreeNode


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 递归交换左右子树
        current_node: TreeNode = root
        if root is None:
            return None
        temp_node: TreeNode = current_node.right
        current_node.right = current_node.left
        current_node.left = temp_node
        self.invertTree(current_node.left)
        self.invertTree(current_node.right)
        return root