from typing import Optional, List
import queue


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    # 前序遍历
    def pre_order(self,root:Optional[TreeNode]):
        if root is None:
            return None
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    # 中序遍历
    def mid_order(self,root:Optional[TreeNode]):
        if root is None:
            return None
        self.pre_order(root.left)
        print(root.val)
        self.pre_order(root.right)

    # 后序遍历
    def post_order(self,root:Optional[TreeNode]):
        if root is None:
            return None
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val)

    # 层序遍历
    def level_order(self,root:Optional[TreeNode]):
        if root is None:
            return None
        level_queue = queue.Queue()
        level_queue.put(root)
        while not level_queue.empty():
            node:TreeNode = level_queue.get()
            print(node.val)
            if node.left is not None:
                level_queue.put(node.left)
            if node.right is not None:
                level_queue.put(node.right)

    # 创建一颗二叉树
    def create_birary_tree(self,nums:List[int], index:int) -> TreeNode:
        root = None
        if index < len(nums):
            if nums[index] is not None:
                root = TreeNode(nums[index])
                root.left = self.create_birary_tree(nums,index * 2 + 1)
                root.right = self.create_birary_tree(nums,index * 2 + 2)
        return root

if __name__ == "__main__":
    bTree = BinaryTree()
    ll = [3,8,10,15,20,6]
    root:TreeNode = bTree.create_birary_tree(ll,0)
    bTree.level_order(root)

