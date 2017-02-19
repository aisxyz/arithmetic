# coding: utf8
'''
B树的性质：
1、每个节点x有以下域：
 a) n[x]：当前存储在节点x中的关键字数。
 b) n[x]个关键字本身，以非降序存放，即 key1[x]<=key2[x]<=...<=keyn[x]。
 c) leaf[x]，表明节点x是否为叶子的布尔值。
2、每个内节点x还包含n[x]+1个指向其子女的指针c1[x], c2[x], ..., cn[x], cn1[x]，叶
 节点的ci域无定义。
3、各关键字keyi[x]对存储在各子树中的关键字范围加以分隔：如果ki为存储在以ci[x]为根的子树
 中的关键字，则： k1<=key1[x]<=k2<=key2[x]<=...<=keyn[x]<=kn1 。
4、每个叶节点具有相同的深度。
5、每个节点能包含的关键字数有上界和下界，它们共用一个称作B数的最小度数的固定整数t>=2来表示。
 a) 每个**非根**的节点必须至少有t-1个关键字，每个**非根**的内节点至少有t个子女。
 b) 每个节点可包含至多2t-1个关键字，所以一个内节点至多可有2t个子女。如果一个节点恰好有2t-1
 个关键字，就说它是满的。
 注：t=2时，树的每个内节点有2个、3个或4个子女，亦即一棵2-3-4树。

定理：一棵关键字个数为n>=1，最小度数为t>=2的B数的高度h满足： h <= log_t((n+1)/2)。
'''

from bisect import bisect_left

g_min_degree = 3

class Btree_node:
    def __init__(self, keys=None):
        # keys needs to be sorted.
        if keys is None:
            keys = []
        self.num_key = len(keys)
        self.keys = keys    #sorted(keys)
        self.is_leaf = True
        #self.parent = None
        self.children = [None] * (self.num_key+1)

    def __repr__(self):
        return '<BNode(%s)>' % str(self.keys)


def Btree_search(node, key):
    i = 0
    while i < node.num_key and key > node.keys[i]:
        i += 1
    if i < node.num_key and key == node.keys[i]:
        return node, i
    if node.is_leaf:
        return None, -1
    else:
        # DISK_READ(node.children[i])   # simulate reading disk.
        return Btree_search(node.children[i], key)


def Btree_create():
    root = Btree_node()
    # DISK_WRITE()
    return root


def is_full_node(node):
    return node.num_key == 2 * g_mid_degree - 1


def Btree_split_child(node, i, child_i):
    # child_i needs to be a full node.
    mid_key_i = child_i.num_key // 2   # get the tree's min-degree t.
    new_node = Btree_node(child_i.keys[mid_key_i+1:])
    new_node.is_leaf = child_i.is_leaf
    new_node.children = child_i.children[mid_key_i+1: ]
    node.keys.insert(i, child_i.keys[mid_key_i])
    node.children.insert(i+1, new_node)
    node.num_key += 1
    child_i.num_key = mid_key_i
    child_i.keys = child_i.keys[0: mid_key_i]
    child_i.children = child_i.children[: mid_key_i+1]
    # DISK_WRITE(child_i)
    # DISK_WRITE(new_node)
    # DIST_WRITE(node)

def Btree_insert_nonfull(node, key):
    tail_index = node.num_key - 1
    while tail_index >= 0 and key < node.keys[tail_index]:
        tail_index -= 1
    if node.is_leaf:
        node.keys.insert(tail_index+1, key)
        node.num_key += 1
        # DISK-WRITE(node)
    else:
        tail_index += 1
        # DISK-READ(node.children[tail_index])
        if is_full_node(node.children[tail_index]):
            Btree_split_child(node, tail_index, node.children[tail_index])
            if key > node.keys[tail_index]:
                tail_index += 1
        Btree_insert_nonfull(node.children[tail_index], key)
    
def Btree_insert(root, key):
    # This is the only way to increse the height of the B tree.
    if is_full_node(root):
        new_root = Btree_node()
        new_root.is_leaf = False
        new_root.chilren.append(root)
        Btree_split_child(new_root, 0, root)
        Btree_insert_nonfull(new_root, key)
        root = new_root
    else:
        Btree_insert_nonfull(root, key)
    return root
    

def pop_precursor_key(node):
    while not node.is_leaf:
        node = node.children[-1]
    node.num_key -= 1
    node.children.pop()
    return node.keys.pop()

def pop_succeed_key(node):
    while not node.is_leaf:
        node = node.children[0]
    node.num_key -= 1
    node.children.pop(0)
    return node.keys.pop(0)


def Btree_delete(node, key):
    #print('[+] Tracing node:', node)
    if key in node.keys and node.is_leaf:
        node.num_key -= 1
        node.children.pop()     # Any child of leaf-node is none.
        node.keys.remove(key)
        return node
    elif key in node.keys:
        i = node.keys.index(key)
        left_child = node.children[i]
        right_child = node.children[i+1]
        if left_child.num_key >= g_min_degree:
            pre_key = pop_precursor_key(left_child)
            node.keys[i] = pre_key
        elif right_child.num_key >= g_min_degree:
            suc_key = pop_succeed_key(right_child)
            node.keys[i] = suc_key
        else:
            left_child.num_key = 2*g_min_degree - 1
            left_child.keys.extend( [key] + right_child.keys )
            left_child.children.extend( right_child.children )
            node.num_key -= 1
            node.keys.remove(key)
            node.children.remove(right_child)
            node.children[i] = Btree_delete(left_child, key)
            if node.num_key == 0:
                node = node.children[0]
    else:
        if node.is_leaf:
            return node
        i = bisect_left(node.keys, key)
        child = node.children[i]
        if child.num_key == g_min_degree-1:
            left_brother = node.children[i-1] if i>0 else None
            right_brother = node.children[i+1] if i<node.num_key else None
            #print('left_brother:', left_brother)
            #print('right_brother:', right_brother)
            if right_brother and right_brother.num_key >= g_min_degree:
                child.keys.append(node.keys[i])
                child.num_key += 1
                child.children.append(right_brother.children[0])
                node.keys[i] = right_brother.keys[0]
                right_brother.num_key -= 1
                right_brother.keys = right_brother.keys[1: ]
                right_brother.children = right_brother.children[1: ]
            elif left_brother and left_brother.num_key >= g_min_degree:
                child.keys.insert(0, node.keys[i])
                child.num_key += 1
                child.children.insert(0, left_brother.children[-1])
                node.keys[i] = left_brother.keys[-1]
                left_brother.num_key -= 1
                left_brother.keys.pop()
                left_brother.children.pop()
            else:
                if right_brother:
                    child.num_key = 2*g_min_degree - 1
                    child.keys += [node.keys[i]] + right_brother.keys
                    child.children.extend(right_brother.children)
                    node.num_key -= 1
                    node.keys.pop(i)
                    node.children.remove(right_brother)
                else:       # left_brother is not none
                    child.num_key = 2*g_min_degree - 1
                    child.keys = left_brother.keys + [node.keys[i-1]] + child.keys
                    child.children = left_brother.children + child.children
                    node.num_key -= 1
                    node.keys.pop(i-1)
                    node.children.remove(left_brother)
                    i -= 1             
                    
        node.children[i] = Btree_delete(child, key)
        if node.num_key == 0:
            node = node.children[0]
        
    return node
    

def Btree_walk(node, level=0):
    if node is None:
        return
    print('  '*level + '---', node)
    for child in node.children:
        Btree_walk(child, level+1)
        
        
if __name__ == '__main__':
    root = Btree_node(['p'])
    root.is_leaf = False
    node1 = Btree_node(['c', 'g', 'm'])
    node1.is_leaf = False
    node2 = Btree_node(['t', 'x'])
    node2.is_leaf = False
    node3 = Btree_node(['a', 'b'])
    node4 = Btree_node(['d', 'e', 'f'])
    node5 = Btree_node(['j', 'k', 'l'])
    node6 = Btree_node(['n', 'o'])
    node7 = Btree_node(['q', 'r', 's'])
    node8 = Btree_node(['u', 'v'])
    node9 = Btree_node(['y', 'z'])
    root.children = [node1, node2]
    node1.children = [node3, node4, node5, node6]
    node2.children = [node7, node8, node9]
    #print('search key 18:', Btree_search(root, 18))
    root = Btree_delete(root, 'f')
    root = Btree_delete(root, 'm')
    root = Btree_delete(root, 'g')
    root = Btree_delete(root, 'd')
    root = Btree_delete(root, 'b')
    root = Btree_delete(root, 'c')
    root = Btree_delete(root, 'p')
    root = Btree_delete(root, 'v')
    Btree_walk(root)
