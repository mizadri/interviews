from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxValue=0
        minValue=0
        right=0
        left=0
        longestWindow = 0
        while(left < len(nums) and right < len(nums)):
            
            while abs(maxValue - minValue) <= limit and right < len(nums):
                maxValue = max(maxValue, nums[right])                
                minValue = min(nums[left:right+1])
                longestWindow = max(longestWindow, right-left)
                right += 1

            while abs(maxValue - minValue) > limit and left < len(nums):
                left += 1
                maxValue = max(nums[left:right+1])
                minValue = min(nums[left:right+1])

        return max(longestWindow, right-left)
    
sol = Solution()
res = sol.longestSubarray([8,2,4,7], 4)
print(res) # 2