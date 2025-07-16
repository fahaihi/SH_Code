# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行 [链表]。
# Note: 双向链表， 哨兵节点（简化操作）
# Note: 他说了最少使用，所以要按照最先使用的提升优先级才可以

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity  # 记录节点的容量
        self.nodes_dict = {}
        self.dummy = Node(None, None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
    def get_nodes(self, key): # 获取目标节点，并将节点转移到链表的头部
        if key not in self.nodes_dict:
            return None       # 不存在查询的节点
        node = self.nodes_dict[key] # 查询的节点存在
        self.remove(node)           # 满足最常用查询，需要更正链表
        self.update_node_list(node) # 更新RLU缓存
        return node
    def remove(self, node):
        # 移除链表中的当前节点
        node.prev.next = node.next
        node.next.prev = node.prev
    def update_node_list(self, node):
        # 更新链表的节点，把最常用的放到dunmmy的后面
        # 因为是双向链表，所以需要更新四次
        node.prev = self.dummy
        node.next = self.dummy.next
        node.prev.next = node
        node.next.prev = node


    def get(self, key):        # 查询是否存在
        node = self.get_nodes(key)
        return node.value if node else -1

    def put(self, key, value): # 压入新的节点
        node = self.get_nodes(key)
        if node: # 有这本书，并且已经移动到RLU最前面
            node.value = value
            return
        node = Node(key, value)
        self.nodes_dict[key] = node
        self.update_node_list(node)
        if len(self.nodes_dict) > self.capacity:
            back_node = self.dummy.prev
            del self.nodes_dict[back_node.key]
            self.remove(back_node)