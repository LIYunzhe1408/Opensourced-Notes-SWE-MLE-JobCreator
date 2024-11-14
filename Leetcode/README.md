# Part 1: October 30 - Nov 10
| Date   | Topics     | Status                              |
| :----: | :--------: | :---------------------------------: |
| Oct 30 | Array      | <span style="color:green">**Check** |
| Oct 31 | Array      | <span style="color:green">**Check** |
| Nov 1  | String     | <span style="color:red">**NA**      |
| Nov 2  | String     | <span style="color:red">**NA**      |
| Nov 3  | Hash Table | <span style="color:red">**NA**      |
| Nov 4  | Recursion  | <span style="color:red">**NA**      |
| Nov 5  | Recursion  | <span style="color:red">**NA**      |

## Array (Oct 30 - Nov 10)
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
Nov 10 - TBD
| Questions                                                     | Summary    |   Solved On                         |
| :-------------------------------------------                  | :--------  | :---------------------------------  |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/submissions/)| Sort is time consuming, hashmap is the best | Nov 11, 2024 |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/submissions/)|  Two pointers move inward and check alnum in the loop   | Nov 13, 2024 |

### Tricks
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

Many tips that apply to arrays also apply to strings

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