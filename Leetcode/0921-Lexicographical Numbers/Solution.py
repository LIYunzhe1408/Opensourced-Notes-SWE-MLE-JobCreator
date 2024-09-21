class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        limit = n
        for start in range(1, 10):
            self._generate_lexical_numbers(start, limit, res)
        return res

    def _generate_lexical_numbers(self, current_num, limit, res):
        if current_num > limit:
            return
        
        res.append(current_num)

        for digit in range(10):
            next_num = current_num * 10 + digit
            if next_num <= limit:
                self._generate_lexical_numbers(next_num, limit, res)
            else:
                break