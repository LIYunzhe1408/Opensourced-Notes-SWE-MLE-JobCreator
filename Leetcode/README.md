# Week 1: October 30 - Nov 6
| Date   | Topics     | Status                              |
| :----: | :--------: | :---------------------------------: |
| Oct 30 | Array      | <span style="color:green">**Check** |
| Oct 31 | Array      | <span style="color:red">**NA**      |
| Nov 1  | String     | <span style="color:red">**NA**      |
| Nov 2  | String     | <span style="color:red">**NA**      |
| Nov 3  | Hash Table | <span style="color:red">**NA**      |
| Nov 4  | Recursion  | <span style="color:red">**NA**      |
| Nov 5  | Recursion  | <span style="color:red">**NA**      |

## Array 
Oct 30 - Nov 6
1. Overview
   1. Arrays hold values of the same type at contiguous memory locations.
   2. Two things to conern: index / position, element itself.
   3. In Python, the array size is dynamic, dont need to define beforehand.
2. Advantage:
   1. Store multiple elements of the same type with one single variable name.
   2. Accessing element is fast as long as you have the index, opposed to Linked Lists where you have to traverse from the head.
3. Disadvantage:
   1. Addition and Removal of elements into/from the array is slow because remaining elements need to be shifted to accommodate new/missing element. An exception is inserting/removing in/from the end of the array.
   2. Array size is fixed in some language. We need to create a new array and copy the old one when we want to add one more elements, which takes $O(N)$ time.
4. Terms
   1. Subarray - `2, 3, 6]` is a subarray of `[2, 3, 6, 4, 5, 1]`, while `[3, 4, 5]` is not.
   2. Subsequence - `3, 4, 5]` is a subarray of `[2, 3, 6, 4, 5, 1]`, while `[3, 5, 4]` is not.
5. Time complexity
   * Access - $O(1)$
   * Search - $O(N)$
   * Search(Sorted Array) - $O(\log{N})$
   * Insert - $O(N)$
   * Insert(in the end) - $O(1)$
   * Remove - $O(N)$
   * Remove(from the end) - $O(1)$
6. Things to look out for during the interviews
   1. Clarify if there are ***duplicate values*** in the array. Would the presence of duplicate values ***affect*** the answer? Does it make the question ***simpler*** or ***harder***?
   2. When using an ***index*** to iterate through array elements, do not go ***out of bounds***.
   3. Be mindful about ***slicing*** or ***concatenating*** arrays in your code, which would take $O(N)$ time. Use start and end indices to demarcate a subarray/range where possible.
7. Corner Cases:
   1. empty sequence
   2. sequence with 1 or 2 elements
   3. sequence with repeated elements
   4. duplicated values in sequence
8. Techniques:
   1. Sliding window
        
        Apply to many ***sub***array/substring problems. ***Two pointers*** usually move in the ***same direction*** will never overtake each other. This ensures every element will at most be visited twice and the complexity will still be $O(N)$

    2. Two pointers
        
        General version of sliding windows where pointers can ***cross*** each other and can be on different arrays. When you're given two arrays to process, it's common to have ***one*** index(***pointer***) ***per array*** to traverse/compare the both of them, incrementing one of them when relevant.

    3. Traversing from the right
    4. Sorting the array
        
        * If the array is sorted or partially sorted, some forms of binary search should be possible. This means interviewer is looking for a solution that is ***faster than $O(N)$***. 
         * In some cases, sorting the array first can ***simplify*** the problem.
  
    5. [NOT SURE] Precomputation

        For questions where ***summation*** or multiplication of a ***subarray*** is involved, precomputation using hashing or a prefix/suffix sum/product will be useful

    6. Index as a hash key
        
        When you're given a sequence and the interviewer asks for $O(1)$ space, it will be possible to use the array itself as a hash table.
        > For example, if the array only has values from 1 to N, where N is the length of the array, negate the value at that index (minus one) to indicate presence of that number.

    7. Traversing the array more than once
        
        Keep $O(N)$ time complexity

Questions
1. [Two sums](https://leetcode.com/problems/two-sum/description/)
2. [Best time to buy and sell stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
3. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/submissions/)
4. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/submissions/)
5. [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/submissions/)
6. [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/submissions/)
7. [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/)

### Oct 31
Reading:
* [Coding interview cheatsheet: Best practices before, during and after](https://www.techinterviewhandbook.org/coding-interview-cheatsheet/)
* [Top techniques to approach and solve coding interview questions](https://www.techinterviewhandbook.org/coding-interview-techniques/)