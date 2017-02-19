#coding: utf8

def insert_sort(array):
    # Time complexity: O(n^2)
    length = len(array)
    for cur_i in range(1, length):
        value = array[cur_i]
        pre_i = cur_i - 1
        while pre_i>=0 and array[pre_i]>value:
            array[pre_i+1] = array[pre_i]   # or use list.insert() method.
            pre_i -= 1
        array[pre_i+1] = value


def merge_sort(array, start_i, end_i):
    def merge(arr, left_i, turn_i, right_i):
        sentry_value = max(arr) + 1
        sorted_arr1 = arr[left_i: turn_i+1]
        sorted_arr2 = arr[turn_i+1: right_i+1]
        sorted_arr1.append(sentry_value)
        sorted_arr2.append(sentry_value)
        a1_counter = a2_counter = 0
        for i in range(left_i, right_i+1):
            if sorted_arr1[a1_counter] < sorted_arr2[a2_counter]:
                arr[i] = sorted_arr1[a1_counter]
                a1_counter += 1
            else:
                arr[i] = sorted_arr2[a2_counter]
                a2_counter += 1

    if start_i < end_i:
        mid_i = (start_i + end_i) // 2
        merge_sort(array, start_i, mid_i)
        merge_sort(array, mid_i+1, end_i)
        merge(array, start_i, mid_i, end_i)


def quick_sort(array, start_index, end_index):
    if start_index < end_index:
        flag_value = array[end_index]
        last_lower_index = start_index
        count_index = start_index
        while count_index < end_index:
            if array[count_index] < flag_value:
                array[count_index], array[last_lower_index] = array[last_lower_index], array[count_index]
                last_lower_index += 1
            count_index += 1
        array[last_lower_index], array[end_index] = flag_value, array[last_lower_index]
        quick_sort(array, start_index, last_lower_index-1)
        # Or use tail-recursion instead:
        # start_index = last_lower_index + 1
        quick_sort(array, last_lower_index+1, end_index)


def quick_sort2(array, start_index, end_index):
    while start_index < end_index:
        flag_value = array[end_index]
        last_lower_index = start_index
        count_index = start_index
        while count_index < end_index:
            if array[count_index] < flag_value:
                array[count_index], array[last_lower_index] = array[last_lower_index], array[count_index]
                last_lower_index += 1
            count_index += 1
        array[last_lower_index], array[end_index] = flag_value, array[last_lower_index]
        quick_sort(array, start_index, last_lower_index-1)
        # Use tail-recursion instead:
        start_index = last_lower_index + 1


def stooge_sort(array, start_index, end_index):
    if array[start_index] > array[end_index]:
        array[start_index], array[end_index] = array[end_index], array[start_index]
    if start_index+1 >= end_index:
        return
    one_third_index = (end_index - start_index + 1) // 3
    stooge_sort(array, start_index, end_index-one_third_index)  # First two-thirds.
    stooge_sort(array, start_index+one_third_index, end_index)  # Last two-thirds.
    stooge_sort(array, start_index, end_index-one_third_index)  # First two-thirds again.


if __name__ == '__main__':
    array = [2, 8.2, 2, 3, 1.1, -2, 1, 4, 2, 3.0, 5, 7]
    quick_sort2(array, 0, len(array)-1)
    print(array)
