# coding: utf8
'''
对一种数据结构的扩张过程可分为四个步骤：
1、选择基础数据结构
2、确定要在基础数据结构中添加哪些信息
3、验证可用基础数据结构上的基本修改操作来维护这些新添加的信息
4、设计新的操作
'''
############# 顺序动态数 ###############

g_black = 'black'
g_red = 'red'

class NonNode:
    def __init__(self, parent_node):
        self.key = None
        self.color = g_black
        self.left_node = None
        self.right_node = None
        self.parent_node = parent_node
        self.size = 0
        
class Node:
    def __init__(self, key):
        # Note: node.left_node.key <= node.key < node.right_node.key
        self.key = key
        self.color = g_red
        self.left_node = NonNode(self)
        self.right_node = NonNode(self)
        self.parent_node = None
        self.size = 1

    def __repr__(self):
        return '<Node(key=%s, color=%s)>' % (self.key, self.color)


# 搜索某个节点下第几小的关键字节点。
def search_minth_node_under_one_node(node, minth):
    node_rank = node.left_node.size + 1
    if node_rank == minth:
        return node
    elif node_rank > minth:
        return search_minth_node_under_one_node(node.left_node, minth)
    else:
        return search_minth_node_under_one_node(node.right_node, minth-node_rank)


def compute_node_rank(root, node):
    rank = node.left_node.size + 1
    back_node = node
    while back_node is not root:
        if back_node is back_node.parent_node.right_node:
            rank = rank + back_node.parent_node.left_node.size + 1
        back_node = back_node.parent_node
    return rank


def left_rotate(root, node):
    # Note: inorder_tree_walk is not changed.
    temp_node = node.right_node
    if temp_node.key is None:
        print('No right node, forbid to make a left rotate!')
        return root
    temp_node.left_node.parent_node = node
    node.right_node = temp_node.left_node
    temp_node.parent_node = node.parent_node
    if node is root:
        root = temp_node
    elif node is node.parent_node.left_node:
        node.parent_node.left_node = temp_node
    else:
        node.parent_node.right_node = temp_node
        
    temp_node.left_node = node
    node.parent_node = temp_node

    temp_node.size = node.size
    node.size = node.left_node.size + node.right_node.size + 1
    return root


if __name__ == '__main__':
    node1 = Node(11)
    node1.color = g_black
    node2 = Node(2)
    node3 = Node(14)
    node3.color = g_black
    node1.left_node, node1.right_node = node2, node3
    node2.parent_node, node3.parent_node = node1, node1
    node4 = Node(1)
    node4.color = g_black
    node4_1 = Node(7)
    node4_1.color = g_black
    node2.left_node, node2.right_node = node4, node4_1
    node4.parent_node, node4_1.parent_node = node2, node2
    node5 = Node(15)
    node3.right_node = node5
    node5.parent_node = node3
    node6 = Node(5)
    node6_1 = Node(8)
    node4_1.left_node, node4_1.right_node = node6, node6_1
    node6.parent_node, node6_1.parent_node = node4_1, node4_1

    node4_1.size = 3
    node2.size = 5
    node3.size = 2
    node1.size = 8

    print(search_minth_node_under_one_node(node1, 4))
    print(compute_node_rank(node1, node5))
