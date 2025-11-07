"""
Check if the Sentence Is Pangram
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # One way
        # return len(set(sentence)) == 26
        
        # Dictionary to maintain English alphabets and its count
        alphabet_and_found = {chr(ord('a') + i): False for i in range(26)}
        output = True
        
        for char in set(sentence):
            alphabet_and_found[char] = True
            
        for _, found in alphabet_and_found.items():
            if found == False:
                output = False
                break
        
        return output
        
s = Solution()
s.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
s.checkIfPangram("leetcode")

"""
Check if the Sentence Is Pangram
--------------------------------
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""