"""
Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in 
𝑂
(
𝑙
𝑜
𝑔
𝑛
)
O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3
Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1
Constraints:

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
123
  


"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ix = 0

        left = 0, right = len(nums)

        while(left < right):
            ix = ((left+right)//2)
            if (nums[ix] > target):
                right = right - 1
            elif (nums[ix] == target):
                return ix
            else:
                left = left + 1
        return -1

sol = Solution()
nums = [-1,0,2,4,6,8], target = 4
sol.search(nums, target)