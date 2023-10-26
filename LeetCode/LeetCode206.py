"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
 * 示例 1：
 *
 *
 * 输入：head = [1,2,3,4,5]
 * 输出：[5,4,3,2,1]
 * 示例 2：
 *
 *
 * 输入：head = [1,2]
 * 输出：[2,1]
"""
# 迭代法
# 1 -> 2 -> 3 -> 4 -> null,假设3  -> 4 已经被翻转，我们处于2，下一步目标是让3的next指向2
# 有 1 -> 2 <- 3 <- 4 此时有2.next.next = 2，这就是递归的公式
from typing import Optional

from LeetCode.LinkedList import ListNode
import LinkedList


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        # 因为这里返回的值是head.next,所以上一步函数返回的值和new_node共享一个引用，即new_node = head.next
        # 所以这里new_node实际上就是下一步函数调用的头结点
        new_node:ListNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_node

if __name__ == "__main__":
    s = Solution()
    link_list = LinkedList.LinkList()
    head:ListNode = ListNode(-1)
    for i in range(3):
        link_list.tail_create_link_list(head)
    link_list.display_linked_list(head)
    print("\n")
    new_head:ListNode = s.reverseList(head)
    link_list.display_linked_list(new_head)


