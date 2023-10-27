"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
 *
 * 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
 *
 * 示例 1：
 *
 *
 * 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
 * 输出：3
 * 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
 * 示例 2：
 *
 *
 * 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
 * 输出：5
 * 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
 * 示例 3：
 *
 * 输入：root = [1,2], p = 1, q = 2
 * 输出：1
"""
from typing import List

from LeetCode.binaryTree import TreeNode
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        # // 自底向上进行查找，使用回溯（递归），由于是自底向上遍历，使用二叉树的后序遍历
        # // 若在左子树或右子树找到了目标节点p或q，则返回上一层，因为只要p，q存在，无论二者在何处，最终都会返回至根结点
        # // 当然若在左右子树同时找到了p，q, 则直接返回该结点， 因为该结点就是p，q的最近公共祖先
        if root is None:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        # 后序遍历自底向上
        left_node = self.lowestCommonAncestor(root.left,p,q)
        right_node = self.lowestCommonAncestor(root.right,p,q)

        if left_node is not None and right_node is not None:
            return root
        elif left_node is None and right_node is not None:
            return right_node
        elif left_node is not None and right_node is None:
            return left_node
        else:
            return None

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
    nodes = [8,10,4,1,7,15,20,None,None,6,5]
    root : TreeNode = s.create_Tree(nodes,0)
    ancestor:TreeNode = s.lowestCommonAncestor(root,TreeNode(6),TreeNode(5))
    print(ancestor.val)
