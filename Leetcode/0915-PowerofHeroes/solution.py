class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, result ,mod = 0, 0, int(1e9+7)
        nums = sorted(nums)
        for n in nums:
            result = (((n * n) % mod) * ((prev + n) % mod) + result) % mod
            prev = ((prev * 2) % mod + n) % mod
        return result