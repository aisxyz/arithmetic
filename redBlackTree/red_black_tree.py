# coding: utf8
'''
红黑树的性质：
1、每个节点非红即黑。
2、根节点是黑的。
3、每个叶节点（注意是 NIL）是黑的。
4、红色节点的儿子均是黑的。
5、每个节点到其子孙叶节点的所有路径上包含相同数目的黑节点，即黑高度相同。
'''
g_black = 'black'
g_red = 'red'

class NonNode:
    def __init__(self, parent_node):
        self.key = None
        self.color = g_black
        self.left_node = None
        self.right_node = None
        self.parent_node = parent_node
        
class Node:
    def __init__(self, key):
        # Note: node.left_node.key <= node.key < node.right_node.key
        self.key = key
        self.color = g_red
        self.left_node = NonNode(self)
        self.right_node = NonNode(self)
        self.parent_node = None

    def __repr__(self):
        return '<Node(key=%s, color=%s)>' % (self.key, self.color)


def preorder_tree_walk(node):
    if node.key is not None:
        print(node, end=' ')
        preorder_tree_walk(node.left_node)
        preorder_tree_walk(node.right_node)

        
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
    return root

def right_rotate(root, node):
    temp_node = node.left_node
    if temp_node.key is Node:
        print('No left node, forbid to make a right rotate!')
        return root
    temp_node.right_node.parent_node = node
    node.left_node = temp_node.right_node
    temp_node.parent_node = node.parent_node
    if node is root:
        root = temp_node
    elif node is node.parent_node.left_node:
        node.parent_node.left_node = temp_node
    else:
        node.parent_node.right_node = temp_node

    temp_node.right_node = node
    node.parent_node = temp_node
    return root

    
def rbtree_insert_fixup(root, node):
    if node is root:
        node.color = g_black
        return node
    while node.parent_node.color == g_red:
        if node.parent_node is node.parent_node.parent_node.left_node:
            uncle_node = node.parent_node.parent_node.right_node
            if uncle_node.color == g_red:
                node.parent_node.color = g_black
                uncle_node.color = g_black
                node.parent_node.parent_node.color = g_red
                node = node.parent_node.parent_node
            elif node is node.parent_node.right_node:
                node = node.parent_node
                root = left_rotate(root, node)
            #else:          # No else ???
            node.parent_node.color = g_black
            node.parent_node.parent_node.color = g_red
            root = right_rotate(root, node.parent_node.parent_node)
        else:
            uncle_node = node.parent_node.parent_node.left_node
            if uncle_node.color == g_red:
                node.parent_node.color = g_black
                uncle_node.color = g_black
                node.parent_node.parent_node.color = g_red
                node = node.parent_node.parent_node
            elif node is node.parent_node.left_node:
                node = node.parent_node
                root = right_rotate(root, node)
            #else:          # No else ???
            node.parent_node.color = g_black
            node.parent_node.parent_node.color = g_red
            root = left_rotate(root, node.parent_node.parent_node)
    root.color = g_black
    return root

def rbtree_insert(root, insert_node):
    temp_node = root
    pre_node = None
    while temp_node.key is not None:
        pre_node = temp_node
        if insert_node.key > temp_node.key:
            temp_node = temp_node.right_node
        else:
            temp_node = temp_node.left_node
    insert_node.parent_node = pre_node
    if pre_node is None:
        root = insert_node
    elif insert_node.key > pre_node.key:
        pre_node.right_node = insert_node
    else:
        pre_node.left_node = insert_node
    #insert_node.color = g_red
    root = rbtree_insert_fixup(root, insert_node)
    return root


def get_min_node(node):
    while node.left_node.key is not None:
        node = node.left_node
    return node

def find_successor_node(node):
    if node.right_node.key is not None:
        return get_min_node(node)
    pnode = node.parent_node
    while pnode and node is pnode.right_node:
        node = pnode
        pnode = pnode.parent_node
    return pnode

def rbtree_delete_fixup(root, node):
    while node is not root and node.color == g_black:
        if node is node.parent_node.left_node:
            brother_node = node.parent_node.right_node
            if brother_node.color == g_red:
                brother_node.color = g_black
                root = left_rotate(root, node.parent_node)
                brother_node = node.parent_node.right_node
            if brother_node.left_node.color == g_black and brother_node.right_node.color == g_black:
                brother_node.color = g_red
                node = node.parent_node
            elif brother_node.right_node.color == g_black:
                brother_node.left_node.color = g_black
                brother_node.color = g_red
                root = right_rotate(root, brother_node)
                brother_node = node.parent_node.color
            else:
                brother_node.color = node.parent_node.color
                node.parent_node.color = g_black
                node.right_node.color = g_black
                root = left_rotate(root, node.parent_node)
                node = root
        else:
            brother_node = node.parent_node.left_node
            if brother_node.color == g_red:
                brother_node.color = g_black
                root = right_rotate(root, node.parent_node)
                brother_node = node.parent_node.left_node
            if brother_node.left_node.color == g_black and brother_node.right_node.color == g_black:
                brother_node.color = g_red
                node = node.parent_node
            elif brother_node.left_node.color == g_black:
                brother_node.right_node.color = g_black
                brother_node.color = g_red
                root = left_rotate(root, brother_node)
                brother_node = node.parent_node.color
            else:
                brother_node.color = node.parent_node.color
                node.parent_node.color = g_black
                node.left_node.color = g_black
                root = right_rotate(root, node.parent_node)
                node = root
    node.color = g_black
    return root

def rbtree_delete(root, delete_node):
    if not delete_node.left_node.key or not delete_node.right_node.key:
        temp_node = delete_node
    else:
        temp_node = find_successor_node(delete_node)
    if temp_node.left_node.key is not None:
        child_node = temp_node.left_node
    else:
        child_node = temp_node.right_node
    child_node.parent_node = temp_node.parent_node
    if temp_node.parent_node is None:
        root = child_node
    elif temp_node is temp_node.parent_node.left_node:
        temp_node.parent_node.left_node = child_node
    else:
        temp_node.parent_node.right_node = child_node

    if temp_node is not delete_node:
        delete_node.key = temp_node.key

    if temp_node.color == g_black:
        root = rbtree_delete_fixup(root, child_node)
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

    preorder_tree_walk(node1)
    print('-'*50)
    insert_node = Node(4)
    node1 = rbtree_insert(node1, insert_node)
    preorder_tree_walk(node1)
    
