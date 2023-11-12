"""请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
 * 实现 LRUCache 类：
 * LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
 * int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
 * void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value
 * 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
 * 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
 * <p>
 * 示例：
 * <p>
 * 输入
 * ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
 * [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
 * 输出
 * [null, null, null, 1, null, -1, null, -1, 3, 4]
 * <p>
 * 解释
 * LRUCache lRUCache = new LRUCache(2);
 * lRUCache.put(1, 1); // 缓存是 {1=1}
 * lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
 * lRUCache.get(1);    // 返回 1
 * lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
 * lRUCache.get(2);    // 返回 -1 (未找到)
 * lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
 * lRUCache.get(1);    // 返回 -1 (未找到)
 * lRUCache.get(3);    // 返回 3
 * lRUCache.get(4);    // 返回 4
 """
from LeetCode.DoubleLinkedList import DoubleListNode


class LRUCache:


    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = DoubleListNode()
        self.tail = DoubleListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # // 如果关键字
    # key
    # 存在于缓存中，则返回关键字的值，否则返回 - 1。
    # // 注意这里访问然以后要将当前节点放到链表的头部
    def get(self, key: int) -> int:
        if key in self.cache:
            current_node: DoubleListNode = self.cache[key]
            # 获取到了结点，则该结点被访问，移入链表头
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev

            self.insert_with_head(current_node)
            return current_node.value
        else:
            return -1

    # // 如果关键字
    # key
    # 已经存在，则变更其数据值value；如果不存在，则向缓存中插入该组 key - value
    # // 上述两个操作都会导致当前节点更新至头部
    # // 如果插入操作导致关键字数量超过 capacity ，则应该逐出最久未使用的关键字。
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node:DoubleListNode = self.cache.get(key)
            node.value = value
            node.prev.next = node.next
            node.next.prev = node.prev

            self.insert_with_head(node)
        else:
            self.size += 1
            if self.size > self.capacity:
                # 逐出链表尾部元素
                delete_node:DoubleListNode = self.tail.prev
                self.delete_from_tail(delete_node)
                del self.cache[delete_node.key]
                self.size -= 1
            new_node = DoubleListNode(key=key, value=value)
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

if __name__ == "__main__":
    s = LRUCache(2)
    s.put(1,1)
    s.put(2,2)
    print(s.get(1))
    s.put(3,3)
    print(s.get(2))
    s.put(4,4)
    print(s.get(1))
    print(s.get(3))
    print(s.get(4))
