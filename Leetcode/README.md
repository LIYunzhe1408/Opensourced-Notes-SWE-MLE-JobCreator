# Coding interview preparation
Author: Yunzhe Jonas Li  @ UC Berkeley\
Email: liyunzhe.jonas@berkeley.edu


## Syntax tips
1. Uppercase to lowercase for string: `s.lower()`. 
2. Keep only lowercase letters in string. `''.join(str.isalpha, s)` or 
    ```python
    sfiltered = ''

    for char in s:
        if (ord(char) >= 97 and ord(char) <= 122):
            sfiltered += char
    ```
3. Keep lowercase letters and numbers in string: `[val for val in s.lower() if val.isalpha() or val.isnumeric()]` or `val.isalnum()`
4. `list` to `string`: `''.join(list)`
5. Create a dict(hashmap) with default `value` value. `hashmap = defaultdict(int)`
6. Use `Counter(string)` to create a hashmap with appearance time count, replacing `for` loop.
7. Use `ord(character)` to convert a single character to integer.
8. The `OrderedDict` class from Python's `collections` module is a dictionary that remembers the order of key-value pairs in which items are inserted.
   1. `ordered_dict.move_to_end('c', last=True)`
   2. `ordered_dict.popitem(last=True)`: pop the most recently added element
   3. It's a `list` that combines the features of `dict` and order-preserving behavior of a `list`
   4. Why Not Just Use a List of Tuples?
      1. Efficient Lookups
      2. Easy Modification

## [New] Graph
A graph is a structure containing a set of objects (vertices or nodes) where there can be edges between nodes.
* Edges can be directed or undirected, optionally having values(a weighted graph)
* Trees are undirected graph in which any two vertices are connected by exactly one edge and there are no cycles.
* Used to build relationship between **unordered entities**
    * Friendship between people: nodes are people, edges represent having a relationship
    * Distance between locations: each node is a location, edges represent two locations are connected, values are distances

Graph representations: you can be given a list of edges, and you should build your own graph from the edges so that you can perform a traversal on them.
* Adjacency matrix: Rare
* Adjacency list: Rare
* Hash table of hash tables: simplest approach during algorithm interviews
* In interview, graphs are commonly given in the input as 2D matrices where cells are the nodes and each cell can traverse to its adjacent cells(Up/down/left/right. Always ensure:
  * current position is within the boundary
  * current position has not been visited

Time complexity:
* DFS: $O(|V|+|E|)$
* BFS: $O(|V|+|E|)$
* Topological sort: $O(|V|+|E|)$

You need to be aware that
* In a graph that allows for cycles, handle cycles and keep a set of **visited** vertices when traversing
* Always keep track of visited nodes, otherwise your code could end up in an infinite loop
* Empty graph
* graph with one or two nodes
* disconnected graph
* graph with cycles

Algorithms for graph search:
* Common: BFS, DFS
* Uncommon: Topological Sort, Dijkstra's Algo
* Almost Never: Bellman-Ford algorithm, Floyd-Warshall algorithm, Prim's algorithm, Kruskal's algorithm. Your interviewer likely doesn't know them either.

Depth First Search: explores as far as possible along each branch before backtracking
```python
def dfs(matrix):
    if not matrix:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        if (i, j) in visited:
            return
        
        visited.add((i, j))
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i <= rows and 0 <= next_j <= cols:
                # Any conditions that expected by specific questions
                traverse(next_i, next_j)
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```

Breadth First Search: explores all directions at the present node
```python
from collections import deque

def bfs(matrix):
    if not matrix:
        return
    
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        queue = deque([(i, j)])
        while queue:
            curr_i, curr_j = queue.popleft()
            if (curr_i, curr_j) not in visited:
                visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i <= rows and 0 <= next_j <= cols:
                    # Any conditions that expected by specific questions
                    queue.append((next_i, next_j))
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```
Topological Sort:
* Initialize a `queue`, a nodes dictionary to store in/out degree/nodes' set for each node, and a result order list.
  * In degree is the condition to determine whether this node has no dependence and can be added into the queue
* Process every node to record their in degree and out nodes' set
* Append all nodes that have 0 in degree into the queue.
* When the queue is not empty
  * Pop out the front node, check if this node the dependence of other nodes
  * Decrement the in degree by one for the nodes that depends on this popped out node
  * Append all nodes that have 0 in degree right now in to the queue.
  * Append current popped out node into result list.
* Return the result list if the length of result list is equal to the number of nodes.

### Questions
1. [200 Accepted in 32'28''] Number of Islands: https://leetcode.com/problems/number-of-islands/submissions/
   * DFS or BFS
2. [733 Accepted in 9'23''] Flood Fill: https://leetcode.com/problems/flood-fill/submissions/
   * BFS

## Tree
A tree is an abstract data type that represents a hierarchical structure of a set of connected nodes. Each node can be connected to many children, but must be connected to exactly one parent, except for the root node that has no parent node.
* An undirected `graph` without cycles.
* Each node can be the root node of its own subtree, making recursion a useful for tree traversal
* Binary tree will be usually asked in interviews as opposed to ternary(3 children) or N-ary(N children) trees.
* Check out what is `Trie` in later sections which is an advanced tree used for efficiently sorting and searching strings.

Common terms in a tree:
* Neighbor: parent or child of a node
* Ancestor: a node reachable by traversing its parent chaining
* Descendent: a node in the node's subtree
* Degree: number of children of a node
* Degree of a tree: maximum degree of nodes in the tree
* Distance: Number of edges along the shortest path between 2 nodes
* Level/Depth: Number of edges along the unique path between a node and the root node
* Width: Number of nodes in a level

A binary tree is the tree where each node in it has a maximum of 2 children.
* Complete binary tree: every level, except the last, is completely filled, and all nodes in the last level are as far left as possible.
* Balanced binary tree: the left and the right subtrees of every node differ in height by no more than 1.
* Traversal:
  * In-order traversal: Left -> Root -> Right
  * Pre-order traversal: Root -> Left -> Right
  * Post-order traversal: Left -> Right -> Root

Binary Search Tree: The in-order traversal will give all the elements in order.
* Be very familiar with the properties of a BST and validating that a binary is a BST.
* When a question involves a BST, the interviewer is usually looking for a solution which runs faster than $O(n)$
* The Access, Search, Insert, and Remove of a BST is all $O(n)$

In interview, you should be very familiar with:
* pre-oder, in-order, post-order traversal recursively
* and iterative approach as an extension because the interviewer may ask the candidate for this one if you finish writing the recursive approach too quickly
* corner cases:
  * empty Tree
  * single node
  * tree with two nodes
  * very skewed tree (like a linked list)
  
Common routines that tree questions will make use of:
* Insert value
* Delete value
* Count number of nodes in the tree
* Whether a value is in the tree
* Calculate the height of the tree
* Binary Tree:
  * Determine if it is a binary search tree
  * Get Maximum value
  * Get Minimum value

Techniques that may be used to solve tree questions:
* Recursion: When you notice the subtree problem can be used to solve the entire problem, try using recursion
  * Always remember to check for the base case, usually where the node is `null`
* Traversal by level: Breadth-first search
* Summation of nodes: Be sure to check whether nodes can be negative.

### Questions
1. [104 Accepted in 16'28''] Maximum Depth of Binary Tree: https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
   * Three solutions: Recursive DFS, Iterative DFS(Stack), BFS(Queue)
2. [226 Accepted in 2'43''] Invert Binary Tree: https://leetcode.com/problems/invert-binary-tree/submissions/
3. [235 Accepted in 29'02''] Lowest Common Ancestor: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/
   * Solution 1: Record all ancestors and determine the lowest using recursive search in BST.
     * Routine for search in BST: 
    ```python
    def search(root, key):
  
    # Base Cases: root is null or key 
    # is present at root
    if root is None or root.key == key:
        return root
    
    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)
    
    # Key is smaller than root's key
    return search(root.left, key)
    ```
    
   * Solution 2: Process two target nodes together and identify the split node.


## Stack
The stack is an abstract data type that supports:
* `push`: insert a new element on the top of a stack
* `pop`: remove and return the most recently added element, which is at the top of the stack

As an abstract data type, it can be implemented using `array` or `singly linked list`

The behavior of pushing and popping is called LIFO(Last In First Out), it's an analogy to a set of physical items stacked on top of each other.

Stacks are an important way of supporting:
* nested or recursive function calls.
* used to implement `depth-first search`(remember `queue` is used for `breadth-first search`)
* `depth-first search` can be implemented using recursion or a manual stack.

The time complexity of 
* `top/peek`, `push`, `pop`, `isEmpty` are all $O(1)$
* `search` is $O(n)$

Corner cases need to be careful:
* Empty stack: popping from an empty stack
* stack with one item
* stack with two items

### Questions
1. [20 Accepted in 16'58''] Valid Parentheses: https://leetcode.com/problems/valid-parentheses/submissions/
2. [232 Accepted in 11'28''] Implement Queue using Stacks: https://leetcode.com/problems/implement-queue-using-stacks/submissions/



## Queue
Queue is a linear collection of elements, like array and linked list, that maintain elements in a sequence.
* Addition of elements at **one end** of the sequence(`enqueue` operation), called tail, rear, or back of the queue.
* Removal of elements from **the other end** (`dequeue` operation), called head or front of the queue.
* This is an abstract data type and can be implemented using `array` or `singly linked list`.
* The behavior is called `FIFO`(First In First Out). Analogy to people lining up in real life to wait for service or food.
* **Breadth-first** search is commonly implemented using queues.

Implementation in python is `queue`. And the time complexity of common operations are
* enqueue: $O(1)$
* dequeue: $O(1)$
* front:  $O(1)$
* back:  $O(1)$
* isEmpty: $O(1)$

You should be aware that
* Most languages do not have a built-in `queue` class. You need to implement it using an array or a list with which the dequeue operation(assuming the front of the queue is on the left) will be $O(n)$ because it requires shifting all elements left by one.
* In such case, you can flag this to the interviewer and say that you assume that there's a queue data structure to use which has an efficient dequeue operation.
* Corner cases:
  * empty queue
  * queue with one item
  * queue with two items

### Questions
1. [225 Exceed 15 min but accepted in 3'48'' after capture the idea] Implement stack using queues: https://leetcode.com/problems/implement-stack-using-queues/submissions/
   * The idea is to keep newly entered element at the front of ‘q1’ so that pop operation dequeues from ‘q1’. ‘q2’ is used to put every new element in front of ‘q1’.
  ```python
  import queue
  q = queue.Queue()
  q.put(1)
  q.get()
  q.empty()
  ```



## Linked List
Linked List is used to represent **sequential** data.
* A linear collection of `nodes` where data and a reference to next element are stored.
* Each contains an address of next element.
* Opposed to `Array`: Order is given by their physical placement in memory

Linked List features:
* $O(1)$ time complexity for insertion and deletion of a node.
* $O(n)$ time complexity for access. Traverse is mandatory.

There are 3 types of linked list:
* Singly linked list: each node points to the next node and the last node points to `null`
* Doubly linked list: each node has two pointers, `next` points to the next node and `prev` points to the previous node. The `prev` of the first node and the `next` of the last node points to `null`.
* Circular linked list: A singly linked list where the last node points back to the first node. A circular doubly linked list variant is that the `prev` of the first node points to the last node and the `next` of the last points back to the first node.

Corner cases need to pay attention:
* empty linked list where the head is `null`
* single node
* two nodes
* **linked list has cycles**: Clarify beforehand with the interviewer whether there can be a cycle in the list.
  
Techniques that are effective when coding and you should familiar with:
* Dummy nodes: Add a placeholder at the head helps to handle many edge cases. In this way, operations will never be done on the head. Be sure to remember to remove them at the end of the operation.
* Two pointers: 
  * Get the $k^{th}$ from last node. One pointer is k nodes ahead of the other, when the one ahead reaches the end, the other is k nodes behind.
  * Detect cycles. One pointer increments twice as much as the other, if two pointers meet, meaning that there is a cycle.
  * Get the middle node. One pointer increments twice as much as the other, if the faster pointer reaches the end, the slower pointer will be at the middle.
* Using space: Used for modifying the linked list in-place rather than creating a new linked list. Ideas can be borrowed from the `Reverse a linked list` question below.
* Elegant modification operations:
  * Truncate(Shorten/Cut off) a list - Set the `next` pointer to `null` at the last element
  * Swap values of nodes - just swap value of the nodes as array, there's no need to swap the `next` pointer.
  * Combine two lists - attach the head of the second list to the tail of the first list.

### Questions
1. [206 Accepted in 2 min after reviewing the idea] Reverse Linked List: https://leetcode.com/problems/reverse-linked-list/submissions/
   * Solve in both recursively and iteratively. Recursive way need to review often.
2. [141 Accepted in 4'42''] Linked List Cycle: https://leetcode.com/problems/linked-list-cycle/submissions/

## Matrix
A matrix is a 2-dimensional array.
* Corner Case:
  * Empty matrix: Check that none of the arrays are 0 length
  * $1\times{1}$ matrix
  * Matrix with only one row or column

Techniques that you should familiar with:
* Creating an empty $N\times{M}$ matrix to make a copy of the matrix with the same size/dimensions that is initialized to empty values to store the visited state or dynamic programming table.**For Traversal or DP**
  * `zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]`
  * Copying a matrix: `copied_matrix = [row[:] for row in matrix]`
* Transposing a matrix: interchanging its rows into columns or columns into rows.
  * For grid game that need to verify vertically and horizontally, one trick is to write code to verify the matrix for the horizontal cells, transpose the matrix, and reuse the logic for horizontal verification to verify originally vertical cells (which are now horizontal)
  * `transposed_matrix = zip(*matrix)`

### Questions
1. [73 Accepted in 8'34''']Set Matrix Zeros: https://leetcode.com/problems/set-matrix-zeroes/submissions/
2. [54 Exceed 15 min but correct idea]Spiral Matrix: https://leetcode.com/problems/spiral-matrix/submissions/
    * Boundary matters a lot.


## Sorting and searching
Sorting is the act of rearranging elements in a sequence in order, either in numerical or lexicographical order, either ascending or descending. It helps i) make a set of data more readable; ii) make it easy to search or retrieve.
* A number of sorting algos run in $O(n^2)$, they should not be used in interviews.
* The sorted lists are called **permutations**(Order in the sequence matters).
* Instead, sort the input using default sorting function so that **you can use binary searches on them**

Binary search compares the target value with the middle element of the array, which informs the algorithm whether the target value lies in the left half or the right half, and this comparison proceeds on the remaining half until the target is found or the remaining half is empty.
* On a sorted array of elements, searching can be done in faster than $O(n)$ time (typically in $O(\log{n})$) by using Binary Search.
* Learning Resource: https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search

### Sorting Classifications
Learning resource: https://medium.com/basecs/sorting-out-the-basics-behind-sorting-algorithms-b0a032873add
> Algorithm is not that intimidating, but a manual of your code -- Vaidehi Joshi published in basecs
* Time complexity
* Space complexity
* Recursive / Non-recursive
* Comparison / Non-Comparison
* Internal / External
* Stability

### Time complexity
You are unlikely to be asked to implement a sorting algo from scratch during an interview, it's good to know TC of different sorting algo.
* The built-in algorithm is almost definitely $O(n\log{(n)})$. In Python, it's Timsort.
* Quick, merge, heapsort takes $O(n\log{(n)})$ time complexity

Be aware of
* Empty sequence
* Sequence with one/two elements
* Sequence containing duplicate elements
* Binary Search should be the first thing that come to your mind when given a sorted order
* Counting sort to deal with known range of values

### Questions
1. [704 Runtime exceed]Binary Search: https://leetcode.com/problems/binary-search/submissions/
    * Be aware of correctly narrowing search range by assign `left=mid+1` and `right=mid-1`. Or will lead to infinite loop.
    * For sequence with just one element, be aware of `left<=right` rather that just `left<right`
2. [33 Accepted in 12'59''] Search in rotated sorted array: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
    * Conduct binary search for sorted part each.

## Recursion
Recursion is a method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. All recursive functions contains two parts:
* A base case (or cases) defined, which defines when the recursion is stopped - otherwise it will go on forever!
* Breaking down the problem into smaller subproblems and invoking the recursive call

Always remember to always define a base case so that your recursion will end.
* Like in fibonacci problem, `fib(0) = 0` and `fib(1) = 1` are base cases

Point out that 
* Recursion implicitly uses a stack. 
* Hence all recursive approaches can be rewritten iteratively using a stack. 
* Beware of cases where the recursion level goes too deep and causes a stack overflow.
* The default limit in Python is 1000.

Make sure you have enough base cases to cover all possible invocations of the recursive function
Techniques

### Questions
1. [22 Exceed 15 minutes]Generate Parentheses: https://leetcode.com/problems/generate-parentheses/submissions/
2. [77 Exceed 15 minutes]Combination: https://leetcode.com/problems/combinations/submissions/. 
   * > Reference of backtracking: https://www.geeksforgeeks.org/what-is-the-difference-between-backtracking-and-recursion/
3. [78 Exceed 15 minutes with trials] Subsets: https://leetcode.com/problems/subsets/
   * Backtracking is leveraged. Decide to include or not include a specific number.
   * Not a permutation, this is a subset

## Array
| Questions                                                     | Summary    |   Solved On                         |
| :-------------------------------------------                  | :--------  | :---------------------------------  |
| [Two sums](https://leetcode.com/problems/two-sum/description/)| Return indices of two numbers. Index as a hash key | Oct 31, 2024 |
| [Best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)          | Kadane's Algorithm: Find the maximum subarray sum in an array of numbers      | Oct 31, 2024 |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/submissions/)    | Loop the array twice     | Nov 3, 2024      |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/submissions/)                            | Kadane's Algorithm       | Nov 4, 2024      |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/submissions/)                        | Index as a hash key in set  | Nov 5, 2024      |
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/submissions/)            | Traverse inward from two ends  | Nov 5, 2024      |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/)| Recognize sorted part and then binary search  | Nov 6, 2024 |
| [3Sum](https://leetcode.com/problems/3sum/submissions/) | Sort+Two pointers, note that when to continue the loop is crucial. Add left or minus right is also vital for two pointers|Nov 6, 2024|
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/submissions/)| Two pointers, add left or minus right is also vital for two pointers  | Nov 10 ,2024|
| [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/submissions/)                | Dequeue for sliding windows  | Nov 11, 2024     |

### Overview
1. Arrays hold values of the same type at contiguous memory locations.
2. Two things to conern: index / position, element itself.
3. In Python, the array size is dynamic, dont need to define beforehand.
### Advantage:
1. Store multiple elements of the same type with one single variable name.
2. Accessing element is fast as long as you have the index, opposed to Linked Lists where you have to traverse from the head.
### Disadvantage:
1. Addition and Removal of elements into/from the array is slow because remaining elements need to be shifted to accommodate new/missing element. An exception is inserting/removing in/from the end of the array.
2. Array size is fixed in some language. We need to create a new array and copy the old one when we want to add one more elements, which takes $O(N)$ time.
### Terms
1. Subarray - `2, 3, 6]` is a subarray of `[2, 3, 6, 4, 5, 1]`, while `[3, 4, 5]` is not.
2. Subsequence - `3, 4, 5]` is a subarray of `[2, 3, 6, 4, 5, 1]`, while `[3, 5, 4]` is not.
### Time complexity
   * Access - $O(1)$
   * Search - $O(N)$
   * Search(Sorted Array) - $O(\log{N})$
   * Insert - $O(N)$
   * Insert(in the end) - $O(1)$
   * Remove - $O(N)$
   * Remove(from the end) - $O(1)$
### Things to look out for during the interviews
1. Clarify if there are ***duplicate values*** in the array. Would the presence of duplicate values ***affect*** the answer? Does it make the question ***simpler*** or ***harder***?
2. When using an ***index*** to iterate through array elements, do not go ***out of bounds***.
3. Be mindful about ***slicing*** or ***concatenating*** arrays in your code, which would take $O(N)$ time. Use start and end indices to demarcate a subarray/range where possible.
### Corner Cases:
1. empty sequence
2. sequence with 1 or 2 elements
3. sequence with repeated elements
4. duplicated values in sequence
### Techniques:
1. Sliding window \
    Apply to many ***sub***array/substring problems. ***Two pointers*** usually move in the ***same direction*** will never overtake each other. This ensures every element will at most be visited twice and the complexity will still be $O(N)$
2. Two pointers \
        General version of sliding windows where pointers can ***cross*** each other and can be on different arrays. When you're given two arrays to process, it's common to have ***one*** index(***pointer***) ***per array*** to traverse/compare the both of them, incrementing one of them when relevant.
3.  Traversing from the right
4.  Sorting the array
    * If the array is sorted or partially sorted, some forms of binary search should be possible. This means interviewer is looking for a solution that is ***faster than $O(N)$***. 
    * In some cases, sorting the array first can ***simplify*** the problem.
5.  Precomputation \
    For questions where ***summation*** or multiplication of a ***subarray*** is involved, precomputation using hashing or a prefix/suffix sum/product will be useful.
    > For `Product of itself`, we need to calculate from the left and right as prefix and suffix.
6.  Index as a hash key \
    When you're given a sequence and the interviewer asks for $O(1)$ space, it will be possible to use the array itself as a hash table.
    > For example, if the array only has values from 1 to N, where N is the length of the array, negate the value at that index (minus one) to indicate presence of that number.
7.  Traversing the array more than once \
        Keep $O(N)$ time complexity

## Reading:
* [Coding interview cheatsheet: Best practices before, during and after](https://www.techinterviewhandbook.org/coding-interview-cheatsheet/)
* [Top techniques to approach and solve coding interview questions](https://www.techinterviewhandbook.org/coding-interview-techniques/)
  1. Try going through all the common data structures and applying them to the problem. These are the data structures to keep in mind and try, in order of frequency they appear in coding interview questions:
     * Hash Maps: Useful for making lookup efficient.
     * Graphs: If the data is presented to you as associations between entities
     * Stack and Queue: Parse a string with nested properties (such as a mathematical equation)
     * Heap: Question involves scheduling/ordering based on some priority. Also useful for finding the max K/min K/median elements in a set.
     * Tree: Store strings in a space-efficient manner and look for the existence of strings
  2. routines
     * Sorting
     * Binary search: Useful if the input array is sorted and you need to do faster than O(n) searches
     * Sliding window
     * Two pointers
     * Union find
     * BFS/DFS
     * Traverse from the back
     * Topological Sorting
  3. Optimize:
     * Time complexity
     * Do even less work: two passes of the array -> single passes
     * Use less space

## String
| Questions                                                     | Summary    |   Solved On                         |
| :-------------------------------------------                  | :--------  | :---------------------------------  |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/submissions/)| Sort is time consuming, hashmap is the best | Nov 11, 2024 |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/submissions/)|  Two pointers move inward and check alnum in the loop   | Nov 13, 2024 |
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/)| Sliding window using 2 pointers to represent boundaries | Nov 17, 2024 |
| [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/submissions/) | longest substring. Two pointer + sliding window + hashmap to record frequency | Nov 22, 2024 |

Common data structures for looking up strings
- Trie/Prefix Tree
- Suffix Tree

Common Algorithms:
- Rabin Karp for efficient searching of substring using a rolling hash
- KMP for efficient searching of substring

### Time Complexity
* Access: $O(1)$
* Search: $O(N)$
* Insert: $O(N)$
* Remove: $O(N)$

### Operations involving another string
Here we assume the other string is of length m.
* Find Substring: $O(m{n})$
* Concatenating: $O(m+n)$
* Slice: $O(m)$
* Split by token: $O(n+m)$
* Strip (remove leading and trailing whitespaces): $O(N)$

### Things to look out for during interviews
Ask about input character set and case sensitivity. Usually the characters are limited to lowercase Latin characters, for example a to z.

### Corner cases
- Empty string
- String with 1 or 2 characters
- String with repeated characters
- Strings with only distinct characters

### Techniques
Many string questions fall into one of these buckets.

#### Counting characters
Use hash table. Space complexity is $O(1)$ as the upper bound of the range is fixed of 26.
#### String of unique characters
A neat trick to count the characters in a string of unique characters is to use a 26-bit bitmask to indicate which lower case latin characters are inside the string.
```python
mask = 0
for c in word:
    mask |= (1 << (ord(c) - ord('a')))
```
> Bit manipulation:
> 
> Save space and efficient but challenging to understand. (Quality of cell phone manufacturing.)
> ![alt text](bit%20manipulation.png)
> 1. Whether position n of x is 1: `x & 1<<n`
> 2. Set position n of x to 1: `x | 1 << n`
> 3. Set position n of x to 0: `x & ~(1<<n)`
> 4. Switch on/off position n of x: `x ^ (1<<n)` 

To determine if two strings have common characters, perform & on the two bitmasks. If the result is non-zero, ie. `mask_a & mask_b > 0`, then the two strings have common characters.


#### Anagram
It is the result of **rearranging** the letters of a word or phrase to produce a new word or phrase, while using all the original letters only once. 

To determine if two strings are anagrams, there are a few approaches:
1. Sorting both strings should produce the same resulting string. This takes $O(n.log(n))$ time and $O(log(n))$ space.
2. If we map each character to a ***prime number*** and we multiply each mapped number together, anagrams should have the same multiple (prime factor decomposition). This takes $O(n)$ time and $O(1)$ space.
3. Frequency counting of characters will help to determine if two strings are anagrams. This also takes $O(n)$ time and $O(1)$ space.


#### Palindrome
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as `madam` or `racecar`.

Ways to determine if a string is a palindrome:
1. Reverse the string and it should be equal to itself.
2. Have **two pointers** at the start and end of the string. Move the pointers **inward** till they meet. At every point in time, the characters at both pointers should match.

When a question is about counting the number of palindromes, a common trick is to have two pointers that move **outward**, **away from the middle**. Note that palindromes can be even or odd length. For each middle pivot position, you need to check it twice - once that includes the character and once without the character.
* For substrings, you can terminate early once there is no match
* For subsequences, use dynamic programming as there are overlapping subproblems.


## Hash Table
| Questions                                                     | Summary    |   Solved On                         |
| :-------------------------------------------                  | :--------  | :---------------------------------  |
| [Ransom Note](https://leetcode.com/problems/ransom-note/submissions/)| Hashmap to count appearance times./ Sort the string may help but waste time | Nov 25, 2024 |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/submissions/)| Hashmap + sort. | Nov 26, 2024 |
| [LRU Cache](https://leetcode.com/problems/lru-cache/submissions/)| Usage of OrderedDict | Dec 1, 2024 |
| [Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/submissions/)| list+map = set | Dec 15, 2024 |
| [First Missing Positive](https://leetcode.com/problems/first-missing-positive/submissions/)| Search for number existence with constraints of `len(nums)` | Dec 18, 2024 |
| [All O`one Data Structure](https://leetcode.com/problems/all-oone-data-structure/submissions/)| Hashmap + doubly linked list works best | Jan 4, 2025 |

A hash table uses a hash function on an element to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored.

Hashing is the most common example of a space-time tradeoff.

### Resolve hash collision
* Separate chaining - A linked list is used for each value
* Open addressing

### Time complexity
* Search: $O(1)$
* Insert: $O(1)$
* Remove: $O(1)$