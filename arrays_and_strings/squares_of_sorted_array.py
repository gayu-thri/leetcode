"""
Squares of a Sorted Array
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sorted_squares = [0 for i in nums]
     
        # Use two pointers approach
        # Note: Absolute value of left most should be considered
        left = 0
        right = len(nums) - 1
        """
        Note
        ----
        Range used here
        `start`:  This should be the index of the last element
        `stop`:   This should be the index before the first element you want to reach
                  Since range() is exclusive of stop value, to include index 0, stop value must be -1
        `step`:   This should be -1 to indicate a backward iteration
        """
        # Input: [-4,-1,0,3,10]
        #             L R   
        for output_index in range(len(nums)-1, -1, -1):
            # Equals case can be used in any of the below blocks, doesn't require a separate block
            if abs(nums[left]) >= abs(nums[right]):
                # Left is greater
                number = abs(nums[left])
                left += 1
            elif abs(nums[right]) > abs(nums[left]):
                # Right is greater
                number = abs(nums[right])
                right -= 1
                
            sorted_squares[output_index] = number**2
                
        return sorted_squares
            
s = Solution()
print(s.sortedSquares([-4,-1,0,3,10]))
print(s.sortedSquares([-7,-3,2,3,11]))
               

"""
Squares of a Sorted Array
-------------------------
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""