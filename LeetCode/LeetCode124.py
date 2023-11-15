"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
 *
 * 路径和 是路径中各节点值的总和。
 *
 * 给你一个二叉树的根节点 root ，返回其 最大路径和 。
 *
 * 示例 1：
 *   1
 *  / \
 *2    3
 *
 * 输入：root = [1,2,3]
 * 输出：6
 * 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
输入：root = [-10,9,20,null,null,15,7]
        -10
        / \
       9  20
         / \
        15 7
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
"""
from typing import Optional

from LeetCode.binaryTree import TreeNode,BinaryTree


# // 从叶子结点开始递归，每次返回当前节点的最大贡献值(Max(左右子树的最大贡献值)+当前节点的值)。
#     //若为叶子结点，则返回本身，即递归边界
#     // 注意，最大路径和是由一个个子树的最大贡献值决定的，每次参与计算最大路径和的左右子树一定拥有自身当前最大的贡献值
class Solution:
    current_max_sum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.get_current_node_max(root)
        return self.current_max_sum

    # 递归主体，计算每个节点的最大贡献值
    def get_current_node_max(self, node: Optional[TreeNode]) -> int:
        # 递归边界
        if node is None:
            return 0

        # 分别计算当前节点的左右子树的最大贡献值
        left_max = max(self.get_current_node_max(node.left), 0)
        right_max = max(self.get_current_node_max(node.right), 0)

        # 计算当前节点的最大路径和
        current_node_max = node.val + left_max + right_max
        self.current_max_sum = max(current_node_max, self.current_max_sum)
        # 返回当前节点的最大贡献值
        return node.val + max(left_max, right_max)

if __name__ == "__main__":
    s = Solution()
    nums = [-10,9,20,None,None,15,7]
    root:TreeNode = BinaryTree.create_birary_tree(nums,0)
    print(s.maxPathSum(root))
