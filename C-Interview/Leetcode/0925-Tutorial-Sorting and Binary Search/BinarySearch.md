## Binary Search
* Background: Think of the case that a teacher searches a sheet for a specific student in 300 sheets.
* Attention: Binary Search must be always operated on **sorted things**.
* Time Complexity: $O(\log_{2}{N})$

### Recursive Solution
```python
"""
array[any datatype]: sorted array
x[datatype same as array]: to be searched
left[int]: left index of array
right[int]: right index of array
"""
bool binarySearchRecursive(array, x, left, right):
    if  left > right:
        return False
    
    mid = (left + right) / 2
    if array(mid) == x:
        return True
    else if x < array[mid]:
        binarySearchRecursive(array, x, left, mid - 1)
    else:
        binarySearchRecursive(array, x, mid + 1, right)
```
### Iterative Solution
```python
"""
array[any datatype]: sorted array
x[datatype same as array]: to be searched
left[int]: left index of array
right[int]: right index of array
"""
bool binarySearchRecursive(array, x):    
    left, right = 0, len(array) - 1    
    while left <= right:
            mid = (right - left) / 2
            if  x == array[mid]:
                return True
            else if x < array[mid]:
                right = mid -1
            else:
                left = mid + 1
        return False
```