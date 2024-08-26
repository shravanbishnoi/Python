"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        mergedStr = ''
        if len(word1)<=len(word2):
            for i in range(len(word1)):
                mergedStr += word1[i]
                mergedStr += word2[i]
            mergedStr += word2[i+1:]
        else:
            for i in range(len(word2)):
                mergedStr += word1[i]
                mergedStr += word2[i]
            mergedStr += word1[i+1:]
        return mergedStr

if __name__ == '__main__':
    obj = Solution()
    result = obj.mergeAlternately('ABCDE', 'PQR')
    print(result)
    