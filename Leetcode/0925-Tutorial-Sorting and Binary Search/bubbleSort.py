def bubbleSort(array):
    N = len(array)
    swapped = False
    for end in range(N - 1, 1, -1):
        for i in range(end):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i] # Swap if out of order
                swapped = True
        if not swapped: # Optimization, terminate early if no pair was swapped, which means the array is sorted.
            break
    return array
