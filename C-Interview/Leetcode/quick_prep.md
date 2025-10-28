The purpose is to prepare for the coding interview in a short time when you already have a full-time job and seek a better one. Topics you need to review:
* High priority:
  * Array
  * String
  * Sorting and searching
  * Matrix
  * Tree
  * Graph
* Mid priority
  * Hash Table
  * Recursion
  * Linked list
  * queue
  * stack
  * heap
  * tire
  * interval
* Low priority
  * DP
  * Binary
  * Math
  * Geometry

## Syntax and python trick
1. Reverse the traverse is `for i in range(len(data), -1, -1)` where the interval `-1` should not be omitted.

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