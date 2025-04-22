def selectionSort(array):
    N = len(array)
    for i in range(N-1):
        smallest = i + array[i:].index(min(array[i:])) # This is O(N)
        array[smallest], array[i] = array[i], array[smallest]
    return array
