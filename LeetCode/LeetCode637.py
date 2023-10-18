"""
给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
 *
 * 示例 1：
 *
 * 输入：root = [3,9,20,null,null,15,7]
 * 输出：[3.00000,14.50000,11.00000]
 * 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
 * 因此返回 [3, 14.5, 11] 。
"""
from typing import Optional, List
import collections

from LeetCode.binaryTree import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res_list:List[float] = []
        if root is None:
            res_list.append(0.0)
            return res_list
        node_queue = collections.deque()
        node_queue.append(root)
        while len(node_queue) > 0:
            size = len(node_queue)
            sum = 0.0
            for i in range(size):
                current_node:TreeNode = node_queue.popleft()
                sum += current_node.val
                if current_node.left is not None:
                    node_queue.append(current_node.left)
                if current_node.right is not None:
                    node_queue.append(current_node.right)
            res_list.append(sum / size)
        return res_list

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
    print(s.averageOfLevels(root))
