"""
在146的基础上，额外添加一个节点的过期时间，当该节点的时间超过过期时间，则该节点自动失效，移入末尾
 """
from LeetCode.DoubleLinkedList import DoubleListNode
import time


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        self.expired_time = 3

    # 如果关键字key存在于缓存中，校验结点是否失效则返回关键字的值，否则返回 - 1。
    # // 注意这里访问然以后要将当前节点放到链表的头部
    def get(self, key: int) -> int:
        current_node: DoubleListNode = self.cache.get(key)

        if current_node is not None and not self.is_expired(current_node):
            # 获取到了结点，则该结点被访问，移入链表头
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

            self.insert_with_head(current_node)
            return current_node.value
        else:
            return -1

    # 如果关键字key已经存在，则变更其数据值value以及时间戳；如果不存在，则向缓存中插入该组 key - value
    # // 上述两个操作都会导致当前节点更新至头部
    # // 如果插入操作导致关键字数量超过 capacity ，则应该逐出最久未使用的关键字。
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node: DoubleListNode = self.cache.get(key)
            node.value = value
            node.time_stamp = int(time.time() * 1000)

            node.prev.next = node.next
            node.next.prev = node.prev

            self.insert_with_head(node)
        else:
            self.size += 1
            if self.size > self.capacity:
                # 逐出链表尾部元素
                delete_node: DoubleListNode = self.tail.prev
                self.delete_from_tail(delete_node)
                del self.cache[delete_node.key]
                self.size -= 1
            new_node = DoubleListNode(key=key, value=value)
            new_node.time_stamp = int(time.time() * 1000)
            self.insert_with_head(new_node)
            self.cache[key] = new_node

    # 双向链表头插法
    def insert_with_head(self, node: DoubleListNode):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    # 双向链表尾部删除
    def delete_from_tail(self, tail_prev_node: DoubleListNode):
        tail_prev_node.prev.next = self.tail
        self.tail.prev = tail_prev_node.prev
        tail_prev_node.prev = None
        tail_prev_node.next = None

    # 时间戳校验
    def is_expired(self, node: DoubleListNode) -> bool:
        if node is None:
            return False
        current_time = int(time.time() * 1000)
        return (current_time - node.time_stamp) // 1000 > self.expired_time


if __name__ == "__main__":
    s = LRUCache(2)
    s.put(1, 1)
    s.put(2, 2)
    print(s.get(1))
    s.put(3, 3)
    print(s.get(2))
    s.put(4, 4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))
