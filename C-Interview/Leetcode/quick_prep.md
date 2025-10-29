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