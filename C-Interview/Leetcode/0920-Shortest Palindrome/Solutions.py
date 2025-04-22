"""
Time complexity: O(n^2)
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reversed_s = s[::-1]

        for i in range(len(reversed_s)):
            if s[:len(reversed_s)-i] == reversed_s[i:]:
                return reversed_s[:i] + s

        return ''

"""
O(n) Solution using KMP
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Reverse the original string
        reversed_string = s[::-1]

        # Combine the original and reversed strings with a separator
        combined_string = s + "#" + reversed_string

        # Build the prefix table for the combined string
        prefix_table = self._build_prefix_table(combined_string)

        # Get the length of the longest palindromic prefix
        palindrome_length = prefix_table[-1]

        # Construct the shortest palindrome by appending the reverse of the suffix
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s

    # Helper function to build the KMP prefix table
    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0

        # Build the table by comparing characters
        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table