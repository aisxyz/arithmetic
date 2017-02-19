# coding: utf8

class Node:
    def __init__(self, key):
        # Note: left_node.key <= current_node.key < right_node.key
        self.key = key
        self.left_node = None
        self.right_node = None
        self.parent_node = None

    def __str__(self):
        return 'Node(key=%s)' % self.key

    def __repr__(self):
        return '<Node(key=%s)>' % self.key


def inorder_tree_walk(node):
    if node is not None:
        inorder_tree_walk(node.left_node)
        print(node.key, end=' ')
        inorder_tree_walk(node.right_node)

def preorder_tree_walk(node):
    if node is not None:
        print(node.key, end=' ')
        preorder_tree_walk(node.left_node)
        preorder_tree_walk(node.right_node)

def posorder_tree_walk(node):
    if node is not None:
        posorder_tree_walk(node.left_node)
        posorder_tree_walk(node.right_node)
        print(node.key, end=' ')


def tree_search(node, search_key):
    if node is None or node.key == search_key:
        return node
    if search_key < node.key:
        return tree_search(node.left_node, search_key)
    else:
        return tree_search(node.right_node, search_key)


def iterative_tree_search(node, search_key):
    while node is not None and node.key != search_key:
        if search_key < node.key:
            node = node.left_node
        else:
            node = node.right_node
    return node


def get_min_node(node):
    while node.left_node is not None:
        node = node.left_node
    return node

def get_max_node(node):
    while node.right is not None:
        node = node.right_node
    return node


def find_successor_node(node):
    if node.right_node is not None:
        return get_min_node(node.right_node)
    pnode = node.parent_node
    while pnode is not None and node is pnode.right_node:
        node = pnode
        pnode = pnode.parent_node
    return pnode

def find_precursor_node(node):
    if node.left_node is not None:
        return get_max_node(node.leftt_node)
    pnode = node.parent_node
    while pnode is not None and node is pnode.left_node:
        node = pnode
        pnode = pnode.parent_node
    return pnode


def tree_insert(root, insert_node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if insert_node.key <= current_node.key:
            current_node = current_node.left_node
        else:
            current_node = current_node.right_node
    insert_node.parent_node = last_node
    if last_node is None:
        root = insert_node
    else:
        if insert_node.key > last_node.key:
            last_node.right_node = insert_node
        else:
            last_node.left_node = insert_node
    return root


def tree_delete(root, delete_node):
    if not delete_node.left_node or not delete_node.right_node:
        temp_node = delete_node
    else:
        # Note: it's successor node no left child if the delete_node has two children.
        temp_node = find_successor_node(delete_node)

    if temp_node.left_node is not None:     # Indicate it is the delete_node.
        child_node = temp_node.left_node
    else:
        child_node = temp_node.right_node

    if child_node is not None:
        child_node.parent_node = temp_node.parent_node

    if temp_node.parent_node is None:
        root = child_node
    elif temp_node is temp_node.parent_node.left_node:
        temp_node.parent_node.left_node = child_node
    else:
        temp_node.parent_node.right_node = child_node
        
    if temp_node != delete_node:
        delete_node.key = temp_node.key
    return root


if __name__ == '__main__':
    root = Node(5)
    node1 = Node(3)
    node2 = Node(7)
    node3 = Node(2)
    node4 = Node(4)
    node5 = Node(6)

    root.left_node, root.right_node = node1, node2
    node1.parent_node, node2.parent_node = root, root
    node1.left_node, node1.right_node = node3, node4
    node3.parent_node, node4.parent_node = node1, node1
    node2.left_node = node5
    node5.parent_node = node2

    node6 = Node(5)
    root = tree_insert(root, node6)
    #tree_delete(root, node1)
    inorder_tree_walk(root)

