def merge(array, left, right):
    """
    :param: array[list]: initial array of [left + right]
    :param: left[list]: left part of array
    :param: right[list]: right part of array

    :return array[list]: sorted array of initial array
    """
    pt_left, pt_right, pt_array = 0, 0, 0
    while pt_left < len(left) and pt_right < len(right):
        if left[pt_left] < right[pt_right]:
            array[pt_array] = left[pt_left]
            pt_left += 1
        else:
            array[pt_array] = right[pt_right]
            pt_right += 1
        pt_array += 1

    # Append all un-visited elements in the left, if it is activated, the right part will not be activated
    while pt_left < len(left):
        array[pt_array] = left[pt_left]
        pt_left += 1
        pt_array += 1

    # Append all un-visited elements in the right, if it is activated, the left part will not be activated
    while pt_right < len(right):
        array[pt_array] = right[pt_right]
        pt_right += 1
        pt_array += 1

    return array


def mergeSort(array):
    N = len(array)

    # Stop condition
    if N == 1:
        return array

    # Divide
    mid = N // 2
    left, right = array[:mid], array[mid:]

    # Conquer
    left = mergeSort(left)
    right = mergeSort(right)

    # Merge
    array = merge(array, left, right)

    return array
