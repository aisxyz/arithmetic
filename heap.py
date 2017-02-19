#coding: utf8

def get_child_index(node_index):
    return(2*node_index+1, 2*node_index+2)


def get_parent_index(node_index):
    parent_index = (node_index-1)>>1 if node_index%2==1 else (node_index-2)>>1
    return parent_index


def max_heapify(heap_array, node_index):
    max_index = len(heap_array) - 1
    left_child_index, right_child_index = get_child_index(node_index)
    if left_child_index<=max_index and heap_array[left_child_index]>heap_array[node_index]:
        larger_index = left_child_index
    else:
        larger_index = node_index

    if right_child_index<=max_index and heap_array[right_child_index]>heap_array[larger_index]:
        larger_index = right_child_index

    if larger_index != node_index:
        heap_array[node_index], heap_array[larger_index] = heap_array[larger_index], heap_array[node_index]
        max_heapify(heap_array, larger_index)


def build_maxheap(heap_array):
    last_nonleaf_node_index = len(heap_array) // 2 - 1
    for i in range(last_nonleaf_node_index, -1, -1):
        max_heapify(heap_array, i)


def heap_sort(heap_array):
    build_maxheap(heap_array)
    for i in range(len(heap_array)-1, 0, -1):
        heap_array[0], heap_array[i] = heap_array[i], heap_array[0]
        part_array = heap_array[0:i]
        max_heapify(part_array, 0)
        heap_array[0:i] = part_array


def out_maxheap(heap_array):
    for i in range(len(heap_array)):
        print('Node {0}: {1}'.format(i, heap_array[i]))


# -----------------------------------------------------------------

# The creation process of max_priority_queue.

def get_max_value(maxheap_array):
    return maxheap_array[0]


def pop_max_value(maxheap_array):
    maxheap_array[0], maxheap_array[-1] = maxheap_array[-1], maxheap_array[0]
    max_value = maxheap_array.pop()
    max_heapify(maxheap_array, 0)
    return max_value


def modify_element(maxheap_array, index, new_value):
    assert 0 <= index < len(maxheap_array), "IndexError: index out of range!"
    if new_value < maxheap_array[index]:
        maxheap_array[index] = new_value
        max_heapify(maxheap_array, index)
        return
    maxheap_array[index] = new_value
    parent_index = get_parent_index(index)
    while index>0 and maxheap_array[parent_index]<new_value:
        maxheap_array[parent_index], maxheap_array[index] = new_value, maxheap_array[parent_index]
        index = parent_index
        parent_index = get_parent_index(index)


def insert(maxheap_array, value):
    maxheap_array.append(min(maxheap_array)-1)
    modify_element(maxheap_array, len(maxheap_array)-1, value)


def delete(maxheap_array, index):   # This is my idea.
    negative_infinity = min(maxheap_array) - 1
    modify_element(maxheap_array, index, negative_infinity)
    maxheap_array.remove(negative_infinity)


if __name__ == '__main__':
    heap_array = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    build_maxheap(heap_array)
    print('max_heap:', heap_array)
    delete(heap_array, 1)
    print('new_heap:', heap_array)
    #out_maxheap(heap_array)
