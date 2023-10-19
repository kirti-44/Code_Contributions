"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        j = len(nums)-1
        res = pow(2,31)-1
        sum = 0
        while i < len(nums) and sum < x :
            if sum + nums[i] > x :
                break
            sum += nums[i]
            i += 1
            if sum == x :
                res = min(res, i)
        while j >= 0 and j >= i:
            if sum + nums[j] > x :
                while i > 0 and sum + nums[j] > x :
                    sum -= nums[i-1]
                    i -= 1
            if sum + nums[j] > x :
                break
            else :
                sum += nums[j]
                if sum == x :
                    res = min(res, len(nums)-j+i)
                j -= 1
        if res == pow(2,31)-1 :
            return -1
        return res