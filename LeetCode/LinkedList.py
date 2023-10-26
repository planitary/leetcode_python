import random


class ListNode:
    def __init__(self,value = None,next = None):
        self.value = value
        self.next = next


class LinkList:
    head:ListNode = None

    # 尾插法(有头结点)
    def tail_create_link_list(self, head: ListNode):
        value = random.randint(1, 100)
        new_node = ListNode()
        new_node.value = value
        p = head
        while p.next is not None:
            p = p.next
        p.next = new_node

    # 头插法(无头结点)
    def head_crate_without_head(self,value: int):
        new_node:ListNode = ListNode()
        new_node.value = value
        new_node.next = self.head
        self.head = new_node

    # 头插法(有头结点）
    def head_create_with_head(self,head:ListNode,value:int):
        new_node:ListNode = ListNode()
        new_node.value = value
        new_node.next = head.next
        head.next = new_node

    # 打印链表
    def display_linked_list(self, head: ListNode):
        if head.next is not  None:
            # 无头结点
            p = head
            # 有头结点
            if p.value is None:
                p = p.next
            while p is not  None:
                print(p.value,end="")
                if p.next is not  None:
                    print(" ->",end="")
                p = p.next
        else:
            print("空链表")

    def get_linked_list_size(self,head:ListNode) -> int:
        p: ListNode = head
        if head.next is not None:
            if p.value is None:
                p = p.next
        count = 0
        while p is not None:
            count += 1
            p = p.next
        return count


if __name__ == "__main__":
    link_list = LinkList()
    link_list.head = ListNode()
    i = 0
    j = 1
    # 带头结点
    # while i < 8:
    #     value = random.randint(0,99)
    #     print("%d " %value)
    #     link_list.head_create_with_head(link_list.head,value)
    #     i += 1
    # # 不带头结点
    link_list.head = ListNode(random.randint(0,20))
    while j < 8:
        value = random.randint(0,99)
        print("%d " %value)
        link_list.head_crate_without_head(value)
        j += 1

    link_list.display_linked_list(link_list.head)


    print("链表长度为:%d" %link_list.get_linked_list_size(link_list.head))

