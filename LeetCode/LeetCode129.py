"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
示例 1：
输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
示例 2：


输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026
"""
from typing import Optional, List
import collections

from LeetCode.binaryTree import TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        nodeQueue = collections.deque()
        sumQueue = collections.deque()
        node_sum,sum = 0,0
        nodeQueue.append(root)
        sumQueue.append(root.val)
        while len(nodeQueue) != 0:
            # // 每次pop一个队列元素的时候分别计算其左右孩子的节点值，节点值为父结点 * 10 + 当前孩子节点
            node:TreeNode = nodeQueue.popleft()
            node_sum = sumQueue.popleft()
            if node.left is not None:
                nodeQueue.append(node.left)
                sumQueue.append(node_sum * 10 + node.left.val)
            if node.right is not None:
                nodeQueue.append(node.right)
                sumQueue.append(node_sum * 10 + node.right.val)
            # 当前节点为叶子结点，进入sum的累加和
            if node.left is None and node.right is None:
                sum += node_sum
        return sum

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
    nodes = [4,9,0,5,1]
    root:TreeNode = s.create_Tree(nodes,0)
    print(s.sumNumbers(root))