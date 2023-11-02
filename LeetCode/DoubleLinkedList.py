import random

class DoubleListNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    head: DoubleListNode = DoubleListNode()
    tail: DoubleListNode = DoubleListNode()

    # 双链表尾插法
    def append(self, val: int):
        newNode = DoubleListNode(val)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # 双链表头插法
    def insert(self, val: int):
        newNode = DoubleListNode(val)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    # 遍历双链表
    @staticmethod
    def display_linked_list(head: DoubleListNode):
        if head.value is None:
            print("empty linkedlist")
        current_node: DoubleListNode = head
        while current_node is not None:
            if current_node.next is not None:
                print("%d<-->" %current_node.value,end="")
            else:
                print(current_node.value)
            current_node = current_node.next

if __name__ == "__main__":
    d = DoubleLinkedList()
    # 尾插
    # for i in range(8):
    #     value = random.randint(0,100)
    #     d.append(value)
    #     print(value,end=" ")
    # 头插
    for i in range(8):
        value = random.randint(0,100)
        d.insert(value)
        print(value,end=" ")
    print(" ")
    d.display_linked_list(d.head)


