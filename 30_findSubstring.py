from typing import List
# my solution, not the best, time complexity is O(n^2)
# class Solution:

#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         n1 = len(s)
#         n2 = len(words[0])
       
#         temp = words.copy()
#         output = []
#         for i in range(n1):
            
#             for j in range(len(words)):
#                 start = i + j*n2
#                 end = start + n2
#                 cur_item = s[start:end]
                
#                 if cur_item not in temp:
#                     temp = words.copy()
#                     break
#                 else:
#                     temp.remove(cur_item)

#                 if not temp:
#                     output.append(i)
#                     temp = words.copy()       
            
#         return output


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n1 = len(s)
        n2 = len(words[0])
        n3 = len(words)
        
        if n1 < n2 * n3:
            return []
        
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        output = []
        
        for i in range(n2):
            print(f"Starting at index: {i}")
            left = i
            right = i
            count = 0
            temp_count = {}
            
            while right + n2 <= n1:
                word = s[right:right+n2]
                print(f"Checking word: {word} at position {right}")
                right += n2
                
                if word in word_count:
                    temp_count[word] = temp_count.get(word, 0) + 1
                    count += 1
                    
                    while temp_count[word] > word_count[word]:
                        left_word = s[left:left+n2]
                        temp_count[left_word] -= 1
                        count -= 1
                        left += n2
                        
                    
                    if count == n3:
                        output.append(left)
                else:
                    temp_count.clear()
                    count = 0
                    left = right
            
        return output
    
# Example usage:
sol = Solution()
# print(sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
# Example usage:
print(sol.findSubstring("barfofoobarthefoobarman",["foo", "bar"]))
