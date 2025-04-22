import collections

'''
Passed, but not time efficient, not space efficient
'''
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Choose a data structure to contain data. List is okay, but search will be O(n)
        appeared = {}

        # this, apple, is, sweet
        s1_split, s2_split = s1.split(' '), s2.split(' ')

        result = []
        # Traverse one sentence s1
        for word in s1_split:
            if word in appeared:
                appeared[word] = appeared[word] + 1
                continue
            appeared[word] = 1
        
        # Traverse another, while not search in the other sentence
        for word in s2_split:
            if word in appeared:
                appeared[word] = appeared[word] + 1
                continue
            appeared[word] = 1
        
        for key in appeared.keys():
            if appeared[key] == 1:
                result.append(key)
        return result


'''
Passed, but not time efficient
'''
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Choose a data structure to contain data. List is okay, but search will be O(n)
        appeared = {}
        result = []

        # this, apple, is, sweet
        sentence = s1.split(' ') + s2.split(' ')

        # Traverse one sentence s1
        for word in sentence:
            if word in appeared:
                appeared[word] = appeared[word] + 1
                continue
            appeared[word] = 1

        for key in appeared.keys():
            if appeared[key] == 1:
                result.append(key)
        return result

# Time Efficient, not space efficient
class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        c = collections.Counter((s1 + " " + s2).split())
        return [w for w in c if c[w] == 1]