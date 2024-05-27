from typing import Optional, Union, List


def bubble_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:    
    sorting = True
    
    while sorting:
        sorting = False
        
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                sorting = True
                array[i], array[i+1] = array[i+1], array[i]
                
    return array

def insertion_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_value
                
    return array

def selection_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    n = len(array)
    for i in range(n-1):
        min_value_index = i
        
        for j in range(i+1, n):
            if array[min_value_index] > array[j]:
                min_value_index = j
                
        array[min_value_index], array[i] = array[i], array[min_value_index]
        
    return array

def merge_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    
    return _merge(left_array, right_array)

def _merge(left: List[Union[int, float, complex]], right: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    res_array = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            res_array.append(left[left_index])
            left_index += 1
        else:
            res_array.append(right[right_index])
            right_index += 1
            
    res_array.extend(left[left_index:])
    res_array.extend(right[right_index:])
    
    return res_array
        
def quick_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    if len(array) <= 1:
        return array
    
    pivot = array[len(array) // 2]
    left_array = [x for x in array if x < pivot]
    middle_array = [x for x in array if x == pivot]
    right_array = [x for x in array if x > pivot]
    
    return quick_sort(left_array) + middle_array + quick_sort(right_array)

def heap_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    n = len(array)

    for i in range(n // 2 - 1, -1, -1):
        _heap(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        _heap(array, i, 0)

    return array

def _heap(array: List[Union[int, float, complex]], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        _heap(array, n, largest)
        
def radix_sort(array: List[Union[int, float]]) -> List[Union[int, float]]:
    max_val = max(array)
    
    max_radix = 0
    while True:
        max_radix += 1
        if max_val / 10**(max_radix) < 1:
            break
        
    for i in range(max_radix):
        bins: List[List[int]] = [[] for _ in range(10)]
        
        for value in array:
            radix_value = (value // 10**i) % 10
            bins[radix_value].append(value)
            
        array.clear()
        for bin_ in bins:
            array.extend(bin_)
    
    return array

def custom_sort(array: List[Union[int, float, complex]]) -> List[Union[int, float, complex]]:
    root_index = 0
    root_value = array[root_index]
    tree = [root_value]
    
    for i in range(1, len(array)):
        index = root_index
        
        while True:
            if array[i] < tree[index]:
                if index > 0:
                    if array[i] < tree[index-1]:
                        index -= 1
                    else:
                        tree.insert(index, array[i])
                        root_index += 1
                        break
                else:
                    tree.insert(0, array[i])
                    root_index += 1
                    break
                
            else:
                if index < len(tree)-1:
                    if array[i] > tree[index+1]:
                        index += 1
                    else:
                        tree.insert(index+1, array[i])
                        break
                else:
                    tree.append(array[i])
                    break
    
    return tree