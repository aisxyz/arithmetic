#codign: utf8

def counting_sort(array):
    '''
    Note: all elements are required to be integers.
    '''
    min_value = min(array)
    if min_value < 0:
        # Convert negative number to nonnegative number.
        array = [x-min_value for x in array]
    max_value = max(array)
    temp_array = []
    for i in range(max_value+1):
        temp_array.append(0)
    for x in array:
        temp_array[x] += 1
    count = 0
    for i in range(max_value+1):
        num_ele = temp_array[i]
        while num_ele > 0:
            array[count] = i
            count += 1
            num_ele -= 1
    if min_value < 0:
        # Recover to original number.
        array = [x+min_value for x in array]
    return array


def bucket_sort(array):
    # Note: bucket-sort needs every element is in range [0, 1).
    min_value = min(array)
    if min_value < 0:
        array = [x-min_value for x in array]
    max_value = max(array)
    temp_array = []
    array_len = len(array)
    for _ in range(array_len):
        temp_array.append([])
    minification = max_value + 1
    array = [ x/minification for x in array ]
    
    for i in range(array_len):
        bucket_index = int(array_len*array[i])
        temp_array[bucket_index].append(array[i])
    array = []
    for i in range(array_len):
        temp_array[i].sort()
        array += temp_array[i]
        
    # Recover to original number, pay attention to the order.
    array = [ x*minification for x in array ]
    if min_value < 0:
        array = [ x+min_value for x in array ]
    return array


if __name__ == '__main__':
    array = [2.5, 5, 3, 0, -2, -1, 2, 3.5, 0, 3, 7]
    array = bucket_sort(array)
    print('array sorted:', array)
