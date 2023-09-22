import random


class ListNode:
    def __init__(self):
        self.next = None
        self.value = None


class LinkList:

    def tail_create_link_list(self, head: ListNode):
        value = random.randint(1, 100)
        new_node = ListNode()
        new_node.value = value
        p = head
        while p.next is not None:
            p = p.next
        p.next = new_node


    def display_linked_list(self,head: ListNode):
        if head.next is not  None:
            p = head.next
            while p is not  None:
                print(p.value,end="")
                if p.next is not  None:
                    print(" ->",end="")
                p = p.next
        else:
            print("空链表")


link_list = LinkList()
head = ListNode()
x = 0
while x < 5:
    link_list.tail_create_link_list(head)
    x += 1
link_list.display_linked_list(head)