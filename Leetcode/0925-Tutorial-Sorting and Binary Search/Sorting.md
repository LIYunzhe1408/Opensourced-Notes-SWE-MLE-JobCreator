# Sorting
## 1 Motivation
Sorting is a very classic problem of reordering items (that can be compared, e.g., integers, floating-point numbers, strings, etc) of an array (or a list) in a certain order (increasing, non-decreasing (increasing or flat), decreasing, non-increasing (decreasing or flat), lexicographical, etc).
* Comparison versus non-comparison based strategies
* Iterative versus Recursive implementation,
* Divide-and-Conquer paradigm
* Best/Worst/Average-case Time Complexity analysis,
* Randomized Algorithms, etc.

When an (integer) array A is sorted, many problems involving A become easier.

### 1-1 Category
* Bubble Sort (comparison)
* Selection Sort (comparison)
* Insertion Sort (comparison)
* Merge Sort (comparison, recursive)
* Quick Sort (comparison, recursive)
* Random Quick Sort (comparison, recursive)
* Counting Sort (non-comparison)
* Radix Sort (non-comparison)

## 2 Analysis of Algorithm
Analysis of Algorithm is a process to evaluate rigorously the resources (time and space) needed by an algorithm and represent the result of the evaluation with a (simple) formula.

We can measure the actual running time of a program by using wall clock time or by inserting timing-measurement code into our program. **However**, actual running time is not meaningful when comparing two algorithms as they are possibly coded in different languages, using different data sets, or running on different computers.

Instead of measuring the actual timing, we count the # of operations (arithmetic, assignment, comparison, etc). This is a way to assess its efficiency as an algorithm's execution time is correlated to the # of operations that it requires. Knowing the (precise) number of operations required by the algorithm, we can state something like this: Algorithm **$X$** takes **$2n^2 + 100n$** operations to solve problem of size **$n$**

### 2-1 Only consider the leading term
Asymptotic analysis is an analysis of algorithms that focuses on analyzing problems of large input size n, considers only the leading term of the formula, and ignores the coefficient of the leading term.

We choose the leading term because the lower order terms contribute lesser to the overall cost as the input grows larger, e.g., for $f(n) = 2n^2 + 100n$, we have:
$f(1000) = 2*1000^2 + 100*1000 = 2.1M$, vs
$f(100000) = 2*100000^2 + 100*100000 = 20010M$.

### 2-2 Ignoring coefficient of the leading term.
Suppose two algorithms have $2n^2$ and $30n^2$ as the leading terms, respectively. 

Although actual time will be different due to the different constants, the **growth rates** of the running time are the same. Compared with another algorithm with leading term of $n^3$, the difference in growth rate is a much more dominating factor.

Hence, we can drop the coefficient of leading term when studying algorithm complexity.

### 2-3 Big-O Notation
If algorithm $A$ requires time proportional to $f(n)$, we say that algorithm $A$ is of the order of $f(n)$.

We write that algorithm $A$ has time complexity of $O(f(n))$, where $f(n)$ is the growth rate function for algorithm $A$.

The most common growth terms can be ordered from fastest to slowest as follows:
$O(1)$/constant time < $O(log n)$/logarithmic time < $O(n)$/linear time <
$O(n log n)$/quasilinear time < $O(n2)$/quadratic time < $O(n3)$/cubic time <
$O(2n)$/exponential time < $O(n!)$/also-exponential time < $∞$
![](./Figures/growth_rates.png)

## 3 $O(N^{2})$ Comparison-based Sorting
Examples are based on ascending order. From small to large.

They compare pairs of elements of the array and decide whether to swap them or not.
### Bubble Sort
1. Assume array length is N. Compare adjacent pair of items
2. Swap the item if they are out of order
3. Repeat step 1 and 2 until comparing the last pair(i.e. array[N-2] and array[N-1]), then the last item will be the smallest/largest one
4. Reduce comparison length by 1(i.e. from 0 to N-2, then 0 to N-3) until reduced to 1.
```python
def bubbleSort(array):
    N = len(array) 
    for end in range(N - 1, 1, -1):
        for i in range(end - 1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i] # Swap if out of order
                swapped = True
        if swapped: # Optimization, terminate early if no pair was swapped, which means the array is sorted.
            break
    return array
```
### Selection Sort
Thoughts are similar to Bubble but w/ o/ several swaps.
1. Select the index of the minimal item.
2. Swap it with the **first** available index.
3. Repeat step 1 and 2 until the end
```python
def selectionSort(array):
    N = len(array)
    for i in range(N-1):
        smallest = i + A[i:].index(min(A[i:])) # This is O(N)
        array[smallest], array[i] = array[i], array[smallest]
    return array
```
### Insertion Sort
Imagine you now have one poker card and gonnna pick several cards one by one.
1. Pick next card and compare it with the sequence of the last pick.
2. Insert it into the proper order.
3. Repeat 1 and 2.
* Best Cases: Sorted list, no shifting of the inner loop will be needed. $O(N)$
* Worst Cases: Reversed list, every inner iteration will run the whole array. $O(N^2)$
```python
def insertSort(array):
    N = len(array) # how many cards I have
    
    for i in range(1, N - 1):
        picked_card = array[i]
        j = i - 1
        while picked_card < array[j] and j >= 0: # This replaces the for loop, because the loop should be break when the order is sorted. Using for loop will be too tedious using if statement.
            array[j+1] = array[j]
            j -= 1

        # for j in range(i-1, -1, -1):
        #     if picked_card < array[j]:
        #         array[j+1] = array[j]
        #     else:
        #         break
        array[j] = picked_card
    return array
```

## 4 $O(N\log{N})$ Comparison-based Sorting
* Merge Sort
* Quick Sort and its Randomized version.

These sorting algorithms are usually implemented recursively, use Divide and Conquer problem solving paradigm, and run in $O(N log N)$ time for Merge Sort and $O(N log N)$ time in expectation for Randomized Quick Sort.

https://visualgo.net/en/sorting?slide=11