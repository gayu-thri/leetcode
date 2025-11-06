from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Example - Odd length
        # Input: ["h","e", "l", "l", "o"]
        # Index: [ 0 , 1 ,  2 ,  3 ,  4 ]
        # len_s = 5; mid_index = 2
        
        # Example - Even length
        # Input: ["h","e", "l", "l", "o", "o"]
        # Index: [ 0 , 1 ,  2 ,  3 ,  4 ,  5 ]
        # len_s = 6; mid_index = 3
        
        last_index = len(s) - 1
        mid_index = (len(s) // 2)
            
        for i in range(mid_index):
            temp = s[i]
            s[i] = s[last_index - i]
            s[last_index - i] = temp
            
        return s

s = Solution()
print(s.reverseString(["h","e", "l", "l", "o"]))
print(s.reverseString(["h","e", "l", "l", "o", "o"]))