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
2. Usage of `set()`. `set.add()` and `set.remove()`
3. Usage of `from collections import Counter`. If the key is not in counter, will return 0 rather than raising error.
4. Usage of `OrderedDict` for LRU. `move_to_end(key)` and `popitem(last=False)`

## Questions to be reviewed
* !!! [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/description/)
* !!! [Maximum subarray](https://leetcode.com/problems/maximum-subarray/): 看之前累加的stuff whether larger than current value
* !!! [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/). Shrinking window using `set()`
* !!! KMP. The pointer pointing to the main string will never back trace. The characters we skip in the pattern string are the prefix/suffix shared in one substring. And the LPS should not be the entire pattern string.
* !!! [First Missing Positive](https://leetcode.com/problems/first-missing-positive/description/)
  * In-place solution: indexing sort
  * Quick solution: set() + linear search based on nums length
* !!! [LRU Cache](https://leetcode.com/problems/lru-cache/description/)
  * `OrderedDict`
  * More detailed: `Hashmap` + `doubly linked list`

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