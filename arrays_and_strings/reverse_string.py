"""
Reverse String
"""
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


"""
Reverse String
--------------
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""