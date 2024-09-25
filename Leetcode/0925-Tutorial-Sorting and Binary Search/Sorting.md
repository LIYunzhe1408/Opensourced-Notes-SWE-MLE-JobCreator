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
* Bubble Sort
* Selection Sort
* Insertion Sort

They compare pairs of elements of the array and decide whether to swap them or not.
