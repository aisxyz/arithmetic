# coding: utf8

'''
二项树：
    二项树Bk是一种递归的有序数。二项树B0只包含一个结点，二项树Bk由两棵二项树Bk_1连接
    而成，其中一棵的根是另一棵的根的最左孩子。
性质：
    1、高度为k。
    2、共有2^k个结点。
    3、在深度i处恰有组合数combinations(k, i)个结点，其中i=0, 1, 2, ..., k。
    4、根的度数为k，它大于任何结点的度数。并且，如果根的子女从左到右编号为k-1，k-2，……，
       0，则子女i是子树Bi的根。

二项堆：二项堆H是由满足以下二项堆性质的二项树组成：
    1、H中的每个二项树遵循最小堆性质，称这种树是最小堆有序的。
    2、对任意自然数k，在H中至多有一棵二项树的根具有度数k。因此在一棵含有N个结点的二项
       堆H中，包含至多**int(lgN)+1**棵二项树。因为N的二进制可表示为N=SUM(bi*2^i)，其
       中i=0, 1, 2, ..., int(lgN)。根据二项树的性质2可知，二项树Bi出现于H中，当且仅当
       位bi=1。例如包含13个结点的二项堆H，因13=(1101)b，所以H包含了最小堆有序二项树B3、
       B2和B1，它们分别有8、4和1个结点。
存储：二项堆中的各二项树的根被组织成一个称为**根表**的链表。
'''

class BHeapNode:
    def __init__(self, key=None):
        self.key = key
        self.degree = 0         # Progressive increase strictly.
        self.parent = None      # Every root has no parent.
        self.most_left_child = None
        self.right_brother = None   # Point to next root if current node is root.

    def __repr__(self):
        '''
        pk = self.parent and self.parent.key or None
        ck = self.most_left_child and self.most_left_child.key or None
        rk = self.right_brother and self.right_brother.key or None
        return '<BHeapNode(k={}, d={}, pk={}, ck={}, rk={})>'.format(
            self.key, self.degree, pk, ck, rk)
        '''
        return '<BHeapNode(key=%s)>' % self.key


def make_binominal_heap():
    return BHeapNode()


def binominal_heap_minimum(head):   # Time complexity: O(logN)
    min_tree = head
    min_value = head.key
    while min_tree.right_brother:
        min_tree = min_tree.right_brother
        if min_value > min_tree.key:
            min_value = min_tree.key
    return min_tree


def binominal_heap_link(tree1, tree2):
    '''Note: Both tree1 and tree2 must have the same degree.'''
    tree1.parent = tree2
    tree1.right_brother = tree2.most_left_child
    tree2.most_left_child = tree1
    tree2.degree += 1


def binominal_heap_merge(heap1, heap2):
    if heap1.key is None:
        return heap2
    elif heap2.key is None:
        return heap1
    
    head1 = heap1
    tail = heap1
    head2 = heap2
    pre_tree = None
    
    while head1 and head2:
        if head1.degree <= head2.degree:
            pre_tree = head1
            tail = head1
            head1 = head1.right_brother
        else:
            if pre_tree:
                insert_tree = head2
                head2 = head2.right_brother
                insert_tree.right_brother = pre_tree.right_brother
                pre_tree.right_brother = insert_tree
                pre_tree = insert_tree
            else:
                heap1 = heap2
                head1, head2 = head2, head1
    if not head1:
        tail.right_brother = head2
    return heap1


def binominal_heap_union(heap1, heap2):
    heap = binominal_heap_merge(heap1, heap2)
    prev_tree = None
    current_tree = heap
    next_tree = current_tree.right_brother
    while next_tree:
        if current_tree.degree != next_tree.degree or \
           next_tree.right_brother and \
           current_tree.degree == next_tree.right_brother.degree:
                prev_tree, current_tree = current_tree, next_tree
        elif current_tree.key <= next_tree.key:
            current_tree.right_brother = next_tree.right_brother
            binominal_heap_link(next_tree, current_tree)
        else:
            binominal_heap_link(current_tree, next_tree)
            current_tree = next_tree
            if prev_tree:
                prev_tree.right_brother = current_tree
            else:
                heap = current_tree
        next_tree = current_tree.right_brother
    return heap


def binominal_heap_insert(heap, insert_tree):
    return binominal_heap_union(heap, insert_tree)


def find_tree_has_min_key(heap):
    tail = heap
    min_key = heap.key
    min_tree = heap
    prev_tree = None
    while tail:         # search the binominal tree with the min key.
        next_tree = tail.right_brother
        if next_tree and next_tree.key < min_key:
            min_key = next_tree.key
            prev_tree = tail
            min_tree = next_tree
        tail = next_tree     
    return min_tree, prev_tree


def extract_min_key(heap):
    min_tree, prev_tree = find_tree_has_min_key(heap)
    if prev_tree:
        prev_tree.right_brother = min_tree.right_brother
    min_tree.right_brother = None
    
    head = min_tree.most_left_child
    current_tree = head.right_brother
    head.right_brother = None
    head.parent = None
    while current_tree:         # reverse the min tree
        next_tree = current_tree.right_brother
        current_tree.right_brother = head
        current_tree.parent = None
        head = current_tree
        current_tree = next_tree

    if not prev_tree:       # if the first tree has the min key.
        return head
    return binominal_heap_union(heap, head)


def decrease_key(heap, node, new_key):
    if new_key > node.key:
        raise ValueError("new key %s is greater than current key!" %(new_key, node.key))
    node.key = new_key
    temp_node = node
    temp_parent = temp_node.parent
    while temp_parent and temp_node.key < temp_parent.key:
        temp_node.key, temp_parent.key = temp_parent.key, temp_node.key
        temp_node = temp_parent
        temp_parent = temp_node.parent
        
def delete_node(heap, node):
    infinitesimal = find_tree_has_min_key(heap)[0].key - 1
    decrease_key(heap, node, infinitesimal)
    return extract_min_key(heap)

    
def binominal_heap_walk(heap, level=0):
    tail = heap
    while tail:
        print('---'*level, tail)
        if tail.most_left_child:
            binominal_heap_walk(tail.most_left_child, level+1)
        tail = tail.right_brother

        
if __name__ == "__main__":
    # Ignore all nodes under grandson.
    
    heap1 = BHeapNode(12)
    tree1 = BHeapNode(7)
    tree1.degree = 1
    t1_node1 = BHeapNode(25)
    t1_node1.parent = tree1
    tree1.most_left_child = t1_node1
    heap1.right_brother = tree1
    tree2 = BHeapNode(15)
    tree2.degree = 2
    t2_node1 = BHeapNode(28)
    t2_node2 = BHeapNode(33)
    t2_node1.right_brother = t2_node2
    t2_node1.parent = t2_node2.parent = tree2
    tree1.right_brother = tree2
    tree2.most_left_child = t2_node1

    heap2 = BHeapNode(18)
    tree2_1 = BHeapNode(3)
    tree2_1.degree = 1
    t21_node1 = BHeapNode(37)
    t21_node1.parent = tree2_1
    tree2_1.most_left_child = t21_node1
    heap2.right_brother = tree2_1
    tree2_2 = BHeapNode(6)
    tree2_2.degree = 4
    t22_node1 = BHeapNode(8)
    t22_node2 = BHeapNode(29)
    t22_node3 = BHeapNode(10)
    t22_node4 = BHeapNode(44)
    t22_node1.right_brother = t22_node2
    t22_node2.right_brother = t22_node3
    t22_node3.right_brother = t22_node4
    t22_node1.parent = t22_node2.parent = tree2_2
    t22_node3.parent = t22_node4.parent = tree2_2
    tree2_1.right_brother = tree2_2
    tree2_2.most_left_child = t22_node1

    heap = binominal_heap_union(heap1, heap2)
    heap = extract_min_key(heap)
    #decrease_key(heap, t2_node2, 0)
    heap = delete_node(heap, t2_node2)
    binominal_heap_walk(heap)
    
    
