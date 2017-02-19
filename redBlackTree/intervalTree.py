# coding: utf8
'''
对一种数据结构的扩张过程可分为四个步骤：
1、选择基础数据结构
2、确定要在基础数据结构中添加哪些信息
3、验证可用基础数据结构上的基本修改操作来维护这些新添加的信息
4、设计新的操作
'''
############# 区间树 ###############

g_black = 'black'
g_red = 'red'

class NonNode:
    def __init__(self, parent_node):
        self.key = None
        self.color = g_black
        self.left_node = None
        self.right_node = None
        self.parent_node = parent_node
        #self.max_value_in_subtree = 0
        
class Node:
    def __init__(self, interval_range):
        # Note: node.left_node.key <= node.key < node.right_node.key
        self.key = interval_range
        self.color = g_red
        self.left_node = NonNode(self)
        self.right_node = NonNode(self)
        self.parent_node = None
        self.max_value_in_subtree = self.key[1]

    def __repr__(self):
        return '<Node(key=%s, color=%s)>' % (self.key, self.color)


def is_overlap(node, check_node):
    if check_node.key[1] < node.key[0] or node.key[1] < check_node.key[0]:
        return False
    return True

def interval_search(root, node):
    temp_node = root
    while not temp_node.key and not is_overlap(temp_node, node):
        if temp_node.left_node.key and temp_node.left_node.max_value_in_subtree >= node.key[0]:
            temp_node = temp_node.left_node
        else:
            temp_node = temp_node.right_node
    return temp_node
