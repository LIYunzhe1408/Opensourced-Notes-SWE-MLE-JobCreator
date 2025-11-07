The purpose is to prepare for the coding interview in a short time when you already have a full-time job and seek a better one. Topics you need to review:
* High priority:
  * !!! Array P0
  * !!! String !!! P0
  * Sorting and searching [P1 Mid priority]
  * !!! Matrix !!! P0
  * Tree [P1 Mid priority]
  * Graph [P2 Low priority]
* Mid priority
  * Hash Table [P1 Mid priority]
  * Recursion [P1 Mid priority]
  * !!! Linked list !!! P0
  * queue [P2 Low priority]
  * stack [P2 Low priority] but trapping rain water is top!!!!
  * heap [P1 Mid priority]
  * tire [P2 Low priority]
  * interval [P1 Mid priority]
* Low priority
  * !!! DP P0
  * Binary [P1 Mid priority]
  * Math [P1 Mid priority]
  * Geometry [P2 Low priority]

## Syntax and python trick
1. Reverse the traverse is `for i in range(len(data), -1, -1)` where the interval `-1` should not be omitted.
2. Usage of `set()`. `set.add()` and `set.remove()`
3. Usage of `from collections import Counter`. If the key is not in counter, will return 0 rather than raising error.
4. Usage of `OrderedDict` for LRU. `move_to_end(key)` and `popitem(last=False)`

## Questions to be reviewed
* !!! [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
* !!! [Maximum subarray](https://leetcode.com/problems/maximum-subarray/): 看之前累加的stuff whether larger than current value
* !!! [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/). Shrinking window using `set()`
* !!! KMP. The pointer pointing to the main string will never back trace. The characters we skip in the pattern string are the prefix/suffix shared in one substring. And the LPS should not be the entire pattern string.
* [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)
  * In-place solution: indexing sort
  * Quick solution: set() + linear search based on nums length
* !!! [LRU Cache](https://leetcode.com/problems/lru-cache/description/)
  * `OrderedDict`
  * More detailed: `Hashmap` + `doubly linked list`
* [Search in rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
  * Identify the rotated part and binary search respectively
  * Identify which part is sorted and determine the next target half.
* [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)
  * Decision Tree: DFS or backtrack
* [Combination](https://leetcode.com/problems/combinations/description/)
  * Decision tree with limit
* [Subset](https://leetcode.com/problems/subsets/description/)
  * Backtrack or DFS(include or not include)
* [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/): dfs(stack, recursion), bfs
* BST: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
  * Iterative
  * Recursive
* !!! [01 Matrix](https://leetcode.com/problems/01-matrix/description/)
  * Multi-source BFS: faster than running multiple single BFS
  * Use single-source BFS when the problem focuses on one starting point: Shortest path in a maze, exploring a graph from one node
  * Use multi-source BFS when multiple starting points are given, and results depend on finding the nearest or shortest distance to any of those starting points: Nearest distance from multiple 0 cells to all other cells, finding the closest fire station to all houses in a city grid.
  * Difference: 
    * Start queue with one node
    * Start queue with all source nodes
* !! [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)
  * $O(m\times{n})$ space complexity to record every 0 position
  * $O(m+n)$ space complexity to record the row/col index
  * $O(1)$ to record 0 row/col in-place.
* !!! [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)
* !!! [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
  * Iterative and recursive(!!!!)
* !!! [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
  * Easy but watch out the condition to stop.
* !!! [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)
* !!! [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
  * Easy but need to consider all corner cases like 1 single close bracket, only open brackets...
* !!! [implement queue using stacks]()
  * Easy and succeeded, but for efficient TC, `push` should not frequently pop and append.
* !!! [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)
  * High frequency problem

## Array
* Values of same type in contiguous memory locations
* index(position), element
* Access: $O(1)$ with index. Linked list should traverse from the head.
* Search: $O(N)$, Search sorted: $O(\log{(N)})$
* Insert & Remove: as remaining elements need to be shifted to accommodate new/missing element.

Heads-up:
* Duplicate values in the array
* index out of bound
* Slice and concatenating will take $O(N)$
* empty sequence
* sequence with 1 or 2 elements
* sequence with repeated elements

Technique:
1. Sliding window with two pointers moving in the same direction that will never overtake each other. Every elements at most will be visited twice.
2. Two pointers that can cross each other and can be on different arrays. One pointer per array pointing to the index, incrementing one of them when condition is valid.
3. Traverse from the right
4. Sorting the array by using Binary Search
5. Precomputation for prefix/suffix, sum/product.

Questions:
* Two Sum
* Best Time to Buy and Sell Stock
* !!! Product of Array Except Self
* !!! Maximum subarray: 看之前累加的stuff whether larger than current value

## String
TODO: KMP, bit manipulation

* String is an array of characters.
* Time complexity of accessing, inserting, and searching is the same as array. 
* Search substring: $O(n\times{m})$
* Concatenating: $O(n+m)$. Strings are immutable, a new one will be created.
* Slicing: $O(m)$
* Split by token:$O(m+n)$. Traverse the entire input string $n$. KMP avoid rescanning and build a LSP array using $O(n)$. 
* Striping: $O(n)$. The string is entirely spaces.

Heads-up:
* Ask input character set and case sensitivity
* Empty string
* string with 1 or 2 characters
* string with repeated characters
* string with only distinct characters

Technique:
* counting characters: Use hash table, space complexity $O(1)$
* string of unique characters: 26-bit mask.
* Anagram: rearranging producing the same.
  * sorting and see if the same. TC: $O(n\log{n})$
  * Map character to a prime number and multiply them together too see if the same multiple.
  * Frequency counting.
* Palindrome: Read the same backward or forward
  * Reverse the string and should be equal.
  * two pointers at the start and the end. Move pointers inward till they meet. Every position, they should match
  * Counting the number of palindromes
    * Move two pointers outward away from the middle. Palindromes can be even or odd length. So for each middle position, you need to check it twice.

Questions:
* Valid Anagram
* Valid Palindrome. Can compare characters at each position in-place.
* !!! Longest Substring Without Repeating Characters. Shrinking window using `set()`
* !!! KMP. The pointer pointing to the main string will never back trace. The characters we skip in the pattern string are the prefix/suffix shared in one substring. And the LPS should not be the entire pattern string.


## Hash Table
* A hash table uses a hash function on an element to compute an index into an array of buckets, from which the desired value can be found. 
* Hashing is the most common example of a space-time tradeoff.
* Resolve hash collision: 
  * separate chaining: A linked list for each value
  * open addressing
* Search, insert, remove: $O(1)$
* Hash function for string
  ```python
  unsigned long long stringHash(const string& s) {
      const unsigned long long P = 131;     // prime base
      const unsigned long long MOD = 1e9+9;
      unsigned long long hash = 0;
      for (char c : s)
          hash = (hash * P + c) % MOD;
      return hash;
  }
  ```

Questions:
* Ransom Note
* !!! [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)
  * In-place solution: indexing sort
  * Quick solution: set() + linear search based on nums length
* !!! [LRU Cache](https://leetcode.com/problems/lru-cache/description/)
  * `OrderedDict`
  * More detailed: `Hashmap` + `doubly linked list`

## Sorting and Searching
* Rearrange elements in a sequence in order, either numerical or lexicographical.
* Binary search compares the target value with the middle element of the array, which informs the algorithm whether the target value lies in the left half or the right half, and this comparison proceeds on the remaining half until the target is found or the remaining half is empty.
* On a sorted array of elements, searching can be done in $O(\log{n})$ by using binary search
* Time complexity
  * Python built-in sorting: $O(n\log{n})$. Timsort
  * quick, merge, heapsort takes $O(n\log{n})$
* sorting classification:(Bubble sort, selection sort, merge sort, quick sort, insertion sort, heap sort, counting sort)
  * TC
  * SC(in-place or not)
  * recursive/Non-recursive (split a large dataset into a smaller or not)
  * comparison/non-comparison
  * internal/external (all on RAM or not)
  * stability

Heads-up:
* Empty sequence
* sequence with one/two elements
* sequence with duplicate elements
* Binary search should be the 1st thing that come to mind when given a sorted order.
* Counting sort to deal to deal with known range of values.

Questions:
* Binary Search
* !!! [Search in rotated sorted array](https://leetcode.com/problems/search-in-rotated-sorted-array/description/)
  * Identify the rotated part and binary search respectively
  * Identify which part is sorted and determine the next target half.

## Recursion
* The solution depends on solutions to smaller instances of the same problem
* All recursive function contains:
  * A base case defined, which defines when the recursion is stopped - otherwise it will go on forever!
  * Breaking down the problem into smaller subproblems and invoking the recursive call

Heads-up:
* Recursion implicitly uses a stack.
* all recursive approaches can be rewritten iteratively using a stack.
* Beware of cases where the recursion level goes too deep and causes a stack overflow.
* The default limit in Python is 1000.

Questions:
* !!! [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/description/)
* !!! [Combination](https://leetcode.com/problems/combinations/description/)
* !!! [Subset](https://leetcode.com/problems/subsets/description/)

## Tree
* Represent a hierarchical structure of a set of connected nodes.
* Each node can be connected to many children, but must be connected to exactly one parent. Except for the root node that has no parent.
* An undirected graph without cycles
* Each node can be the root node of its subtree, so use recursion for tree traversal
* Binary tree is often asked; Trie is more efficient for sorting and searching string.
* Degree: Number of children of a node
  * Level: Number of edges along the unique path between a node and the root.
  * Distance: Number of edges along the shortest path between 2 nodes
* Binary Tree
  * Each node has a maximum of 2 children
  * Complete binary tree: every level, except the last, is completely filled, and all nodes in the last level are as far left as possible
  * Balanced binary tree: the left and the right subtrees of every node differ in height by no more than 1
  * Traversal:
    * In-order: left, root, right
    * Pre-order: root, left, right
    * Post-order: left, right, root
* binary search tree
  * Each node can have at most 2 children
  * All values in its left subtree must be less than the value of the node
  * All values in its right subtree must be greater than the value of the node
  * Access, search, insert, remove: $O(\log{n})$
  * In-order traversal gives all elements in order

Heads-up:
* Empty tree
* single node
* tree with two nodes
* very skewed tree (like a linked list)

Techniques:
* recursion: when the subtree problem can be used to solve the entire problem. Check the base case where the node is null
* Traversal by level: breadth-first search
* summation of nodes: check whether nodes can be negative
* routines:
  * insert value
  * delete value
  * count number of nodes
  * whether a value is in the tree
  * calculate depth/height => in-order, dfs, bfs
  * binary search tree
    * determine if it's a valid BST
    * get maximum value
    * get minimum value

Questions:
* [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/): dfs(stack, recursion), bfs
* Invert/Flip Binary Tree
* BST: [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)
  * Iterative
  * Recursive

## Graph
* Contain a set of nodes(vertices) where there can be edges between nodes.
  * Edges can be directed or undirected, optionally having values as weight
  * Trees are undirected graph which any nodes are connected by exactly one edge and there are no cycles.
* Used to build relationship between unordered entities
  * Friendship
  * Distance between locations
* Build graphs:
  * Given a list of edges, build your own graph
  * Adjacency matrix and list are rare to use
  * During interview: Hashtable(simplest), 2D matrices
  * In 2D matrices graph:
    * Traverse up down left right
    * always check current position within boundary
    * always check current position is unvisited
* TC: DFS, BFS, topological sort: $O(|V|+|E|)$

Heads-up:
* In a graph that allows for cycles, handle cycles and keep a set of visited vertices when traversing
* Always keep track of visited nodes, otherwise the code could en up in an infinite loop
* Empty graph
* graph with one or two nodes
* disconnected graph
* graph with cycles

Techniques:
* Common: BFS, DFS
* Uncommon: Topological sort, Dijkstra's Algo
* Almost never: Bellman-Ford Algo, Floyd-Warshall Algo, Prim's Algo... ...

DFS: recursive
```python
def dfs(matrix):
    if not matrix:
        return
    
    visited = set()
    directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
    rows, cols = len(matrix), len(matrix[0])
    
    def traverse(i, j):
        if (i, j) in visited:
            return
        # Previously (i, j) was added as next_i, next_j before traverse in the loop
        visited.add((i, j))
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i <= rows and 0 <= next_j <= cols and CONDITION:
                
                traverse(next_i, next_j)

    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```

BFS
```python
def bfs(matrix):
    if not matrix:
        return
    
    visited = set()
    directions = ((1, 0), (-1, 0), (0, -1), (0, 1))
    rows, cols = len(matrix), len(matrix[0])
    
    
    def traverse(i, j):       
        q = deque([(i, j)])
        while q: 
            i, j = q.popleft()
            if (i, j) not in visited:
                visited.add((i, j))
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i <= rows and 0 <= next_j <= cols and CONDITION:
                    q.append((next_i, next_j))
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)
```

Topological sort
* A topological sort is a graph traversal in which each node v is visited only after all its dependencies are visited.
* Topological sorting is most commonly used for scheduling a sequence of jobs or tasks which has dependencies on other jobs/tasks. The jobs are represented by vertices, and there is an edge from x to y if job x must be completed before job y can be started.

* Initialize a queue, a nodes dictionary to store in/out degree/nodes' set for each node, and a result order list.
  * In degree is the condition to determine whether this node has no dependence and can be added into the queue
* Process every node to record their in degree and out nodes' set
* Append all nodes that have 0 in degree into the queue.
* When the queue is not empty
  * Pop out the front node, check if this node the dependence of other nodes
  * Decrement the in degree by one for the nodes that depends on this popped out node
  * Append all nodes that have 0 in degree right now in to the queue.
  * Append current popped out node into result list.
* Return the result list if the length of result list is equal to the number of nodes.

Questions:
* Number of Islands.
  * The elements in the grid is not integer 0 and 1, but string '0' and '1'
* Flood Fill: Watch out for the color == original_color
* !!! [01 Matrix](https://leetcode.com/problems/01-matrix/description/)


## Matrix
* A matrix is a 2-dimensional array.

Heads-up:
* Empty matrix: Check that none of the arrays are 0 length
* $1\times{1}$ Matrix
* Matrix with only one row or column

Techniques:
* Create an initialized matrix: 
  * column first then row outer
  * `zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]`
* Copy a matrix
  * `copied_matrix = [row[:] for row in matrix]`
* Transpose a matrix:
  * For grid game that need to verify vertically and horizontally, one trick is to write code to verify the matrix for the horizontal cells.
  * Transpose the matrix and reuse the logic.
  * `transposed_matrix = zip(*matrix)`

Questions:
* !! [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/description/)
  * $O(m\times{n})$ space complexity to record every 0 position
  * $O(m+n)$ space complexity to record the row/col index
  * $O(1)$ to record 0 row/col in-place.
* !!! [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/description/)

## Linked List
* A linear collection of nodes where data and a reference to next element (address) are stored
* Used to represent sequential data that stored in discrete physical placement in memory(Array is in continuous memory)
* Access: $O(n)$
* Insert/Delete: $O(1)$
* Singly linked list, Doubly linked list, Circular linked list.

Heads-up:
* Empty linked list where the head points to null
* single node linked list
* two nodes linked list
* linked list has cycles: Clarify beforehand whether there can be a cycle in the list.

Techniques:
* Dummy head
* Two pointers:
  * Get the $k^{th}$ from the last node. One pointer is k nodes ahead of the other, when it reaches the end, the other pointer is K nodes behind
  * Detect cycles. One pointer increments twice as much as the other, if two pointers meet, meaning there's a cycle.
  * Get the middle node. One pointer increments twice as much as the other, if the faster pointer reaches the end, the other slower pointer will be at the middle.
* Using space: used for modifying the linked list in-place rather than creating a new linked list. `Reverse a linked list`
* Shorten/Cut-off a list: Set the `next` to `null` at the last element.
* Swap values of node: just swap value of the nodes as array, no need to swap the `next` pointer.
* Combine two lists: attach the head of the second list to the tail of the first list.

Questions:
* !!! [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)
  * Iterative and recursive(!!!!)
* !!! [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)
  * Easy but watch out the condition to stop.

## Queue
* A linear collection of elements, like array and linked list, that maintain elements in a sequence.
* Addition of elements at one end of the sequence(enqueue operation), called tail, rear, or back of the queue.
* Removal of elements from the other end (dequeue operation), called head or front of the queue.
* This is an abstract data type and can be implemented using array or singly linked list.
* The behavior is called FIFO(First In First Out). Analogy to people lining up in real life to wait for service or food.
* Breadth-first search is commonly implemented using queues.
* enqueue, dequeue, front, back, isEmpty are all $O(1)$
* [Flag this to interviewer] If using array or list to implement queue, dequeueing will take $O(n)$ as it requires shifting all elements left by one

Heads-up:
* empty queue
* queue with 1 / 2 items


Questions:
* !!! [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/)

## Stack
* An abstract data type:
  * push: insert a new element on the top of the stack
  * pop: remove and return the most recently added element, which is the top of the stack
* Can be implemented using array or singly linked list
* The behavior is LIFO(Last In First Out)
* It's important because it supports:
  * nested or recursive function calls
  * used to implement depth-first search
  * DFS can be implemented using either recursion(implicit stack) or a manual stack
* TC: top, push, pop, isEmpty are all $O(1)$; Search is $O(n)$

Heads-up:
* Empty stack: popping from an empty stack
* stack with 1/2 item(s)

Questions:
* !!! [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/)
  * Easy but need to consider all corner cases like 1 single close bracket, only open brackets...
* !!! [implement queue using stacks]()
  * Easy and succeeded, but for efficient TC, `push` should not frequently pop and append.
* !!! [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)
  * High frequency problem