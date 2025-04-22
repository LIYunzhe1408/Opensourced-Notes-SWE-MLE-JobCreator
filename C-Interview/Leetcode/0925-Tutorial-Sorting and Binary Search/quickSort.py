def partition(array, start, end):
    pivot = array[start]
    mid_index = start

    for it in range(start + 1, len(array)):
        if array[it] <= pivot:
            mid_index += 1
            array[mid_index], array[it] = array[it], array[mid_index]
    array[start], array[mid_index] = array[mid_index], array[start]

    return mid_index


def quickSort(array, start, end):
    # When there are only two elements, it's the stop condition.
    # Case 1: If it's in correct order, say 1 2. mid_index will be 1, i.e. mid == start, mid+1 = end
    # Case 2: If it's in reverse order, say 2 1. mid_index will be 2, i.e. mid+1 > end, and left side will be case 1.
    if start < end:
        mid = partition(array, start, end)

        array = quickSort(array, start, mid)
        array = quickSort(array, mid+1, end)

    return array
