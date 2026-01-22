# A median problem from LeetCode: https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75
# 1657. Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        def CountOccurence(word):
            occur_map = {}
            for letter in word:
                occur_map[letter] = occur_map.get(letter, 0) + 1
            return occur_map
        
        word1_map = CountOccurence(word1)
        word2_map = CountOccurence(word2)

        if set(word1_map.keys()) != set(word2_map.keys()):
            return False
        elif sorted(word1_map.values()) != sorted(word2_map.values()):
            return False
        else:
            return True
# Example usage:
test = Solution()
print(test.closeStrings("uau","ssx"))  



# improved version by using Counter from collections
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_map = Counter(word1)
        print( word1_map)
        word2_map = Counter(word2)

        if set(word1_map.keys()) != set(word2_map.keys()):
            return False
        return sorted(word1_map.values()) == sorted(word2_map.values())
        
        
# Example usage:
test = Solution()
print(test.closeStrings("uau","ssx"))