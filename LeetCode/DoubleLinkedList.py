import random
from typing import Optional


class DoubleListNode:
    def __init__(self, key=None, value=None):
        self.value = value
        self.next = None
        self.prev = None
        self.key = key


class DoubleLinkedList:
    head: Optional[DoubleListNode] = DoubleListNode()
    tail: Optional[DoubleListNode] = DoubleListNode()

    def __init__(self, with_head: bool):
        if with_head:
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            pass

    # 双向链表头插法（伪头尾节点）
    def insert_with_head(self, value: int):
        node: DoubleListNode = DoubleListNode(value=value)
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    # 双向链表尾部删除
    def delete_from_tail(self,tail_prev_node:DoubleListNode):
        tail_prev_node.prev.next = self.tail
        self.tail.prev = tail_prev_node.prev
        tail_prev_node.prev = None
        tail_prev_node.next = None

    # 获取任意位置的双链表节点
    def get_node_by_index(self,index:int )-> DoubleListNode:
        node:DoubleListNode = DoubleListNode()
        linked_size = self.get_size_of_linked_list(self.head)
        if 0 <= index <= linked_size:
            if index >= 0:
                if index <= (linked_size >> 1) - 1:
                    node = self.head
                    while index > 0:
                        node = node.next
                        index -= 1
                else:
                    node = self.tail
                    i = linked_size - 1
                    while i > index:
                        node = node.prev
                        i -= 1
        return node

    # 带头结点的双链表任意节点移入末尾
    def move_2_tail(self,node:DoubleListNode):
        # 先删除当前节点，在尾插法
        node.prev.next = node.next
        node.next.prev = node.prev

        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node


    # 双链表尾插法
    def append(self, val: int):
        newNode = DoubleListNode(value=val)
        if self.head.value is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    # 双链表头插法
    def insert(self, val: int):
        newNode = DoubleListNode(value=val)
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
        if head is None:
            print("empty linkedlist")
        current_node: DoubleListNode = head
        while current_node is not None:
            if current_node.next is not None:
                print("%s<-->" % current_node.value, end="")
            else:
                print(current_node.value)
            current_node = current_node.next

    # 获取链表长度
    @staticmethod
    def get_size_of_linked_list(head: DoubleListNode) -> int:
        if head is None:
            return -1
        current_node: DoubleListNode = head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    # 任意位置插入链表
    def add(self, index: int, value: int):
        linked_list_size: int = DoubleLinkedList.get_size_of_linked_list(self.head)
        if 0 <= index <= linked_list_size:
            # 索引在开头，直接头插法
            if index == 0:
                self.insert(value)
                return
            # 索引在结尾，直接尾插法
            elif index == linked_list_size:
                self.append(value)
                return
            # 其余情况分开讨论，索引在左半边和右半边
            current_node: DoubleListNode = DoubleListNode()
            if index <= (linked_list_size >> 1) - 1:
                current_node = self.head
                while index > 0:
                    current_node = current_node.next
                    index -= 1
            else:
                current_node = self.tail
                i = linked_list_size - 1
                while i > index:
                    current_node = current_node.prev
                    i -= 1
            # 找到当前位置后进行插入，插入位置节点的prev的next（即前一个节点的next）指向新结点，新节点的next指向当前插入位置的节点
            new_node: DoubleListNode = DoubleListNode(value=value)
            current_node.prev.next = new_node
            new_node.next = current_node

    # 任意位置删除(todo:这里有个bug，仅有一个节点是删除会报错）
    def delete(self, index: int):
        linked_size = self.get_size_of_linked_list(self.head)
        if 0 <= index <= linked_size:
            if index >= 0:
                # 仅一个节点时
                if linked_size == 1:
                    self.head = None
                    self.tail = None
                    return
                delete_node: DoubleListNode = DoubleListNode()
                # 头部删除
                if index == 0:
                    delete_node = self.head
                    self.head = self.head.next
                    self.head.prev = None
                    delete_node.next = None
                    delete_node.prev = None
                    print("删除的链表节点为:%d" % delete_node.value)
                    return
                # 尾部删除
                if index == linked_size - 1:
                    delete_node = self.tail
                    self.tail = self.tail.prev
                    self.tail.next = None
                    delete_node.prev = None
                    delete_node.next = None
                    print("删除的链表结点为:%d" % delete_node.value)
                    return
                # 任意位置删除
                current_node: DoubleListNode = DoubleListNode()
                if index <= (linked_size >> 1) - 2:
                    current_node = self.head
                    while index > 0:
                        current_node = current_node.next
                        index -= 1
                else:
                    current_node = self.tail
                    j = linked_size - 1
                    while j > index:
                        current_node = current_node.prev
                        j -= 1
                # // 任意位置删除，将该节点的next指针指向空，prev指针指向空，下一个节点的prev指向该结点的上一个节点；
                # // 上一个节点的next指向该节点的下一个节点
                delete_node = current_node
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
                delete_node.prev = None
                delete_node.next = None
                print("删除的链表结点为:%d" % delete_node.value)


if __name__ == "__main__":
    # 带头结点的构造函数传True，不带的传False
    d = DoubleLinkedList(False)
    # 尾插
    for i in range(1):
        value = random.randint(0, 100)
        d.append(value)
        print(value, end=" ")
    print("")
    # 伪头结点插入
    # for i in range(7):
    #     value = random.randint(0,100)
    #     d.insert_with_head(value)
    #     print(value,end = " ")
    # print(" ")
    # 头插
    # for i in range(8):
    #     value = random.randint(0,100)
    #     d.insert(value)
    #     print(value,end=" ")
    # print(" ")
    d.display_linked_list(d.head)
    print("链表长度:%d" % DoubleLinkedList.get_size_of_linked_list(d.head))
    # d.move_2_tail(d.get_node_by_index(3))
    # d.delete_from_tail(d.tail.prev)
    d.delete(0)
    d.display_linked_list(d.head)


    # d.delete(6)
    # d.display_linked_list(d.head)
    # print("链表长度:%d" % DoubleLinkedList.get_size_of_linked_list(d.head))
