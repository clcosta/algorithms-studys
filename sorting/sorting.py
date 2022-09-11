from random import choice

def insert_sort(array):
    for idx in range(1, len(array)):
        current = array[idx]
        pos_current = idx - 1
        while pos_current >= 0 and array[pos_current] > current:
            array[pos_current+1] = array[pos_current]
            pos_current -= 1
        array[pos_current + 1] = current
    return array

def quick_sort(array):
    if len(array) < 2:
        return array
    
    smaller, equals, greater = [],[],[]

    element_to_compare = choice(array)

    for element in array:
        if element < element_to_compare:
            smaller.append(element)
        elif element == element_to_compare:
            equals.append(element)
        else:
            greater.append(element)
    return quick_sort(smaller) + equals + quick_sort(greater)

def bubble_sort(array):
    size = len(array) - 1
    for _ in range(size):
        for idx in range(size):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
    return array

def selection_sort(array):
    size = len(array) - 1
    for current_idx in range(size):
        min_idx = current_idx
        for idx in range(current_idx, size):
            if array[idx] < array[min_idx]:
                min_idx = idx
        if array[current_idx] > array[min_idx]:
            array[min_idx], array[current_idx] = array[current_idx], array[min_idx]
    return array

def merge_sort(array):

    def _merge(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left

        array_merged = []
        top_left = top_right = 0

        while len(array_merged) < len(left) + len(right):
            if left[top_left] <= right[top_right]:
                array_merged.append(left[top_left])
                top_left += 1
            else:
                array_merged.append(right[top_right])
                top_right += 1
            if top_right == len(right):
                array_merged += left[top_left:]
                break
            if top_left == len(left):
                array_merged += right[top_right:]
                break
        return array_merged
    
    if len(array) < 2:
        return array
    middle = len(array) // 2
    return _merge(left=merge_sort(array[:middle]),right=merge_sort(array[middle:]))