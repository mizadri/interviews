from typing import List
from collections import defaultdict


# Initialize the defaultdict with a default count of 1
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxValue=0
        minValue=999999999999999
        right=0
        left=0
        longestWindow = 0
        count_dict = defaultdict(lambda: 1)
        def decrement_count(key):
            if key in count_dict:
                count_dict[key] -= 1
                if count_dict[key] == 0:
                    del count_dict[key]
                    return True
            return False
        maxValue = max(maxValue, nums[right])                
        minValue = min(minValue, nums[right])

        while(left < len(nums) and right < len(nums)):
            
            while abs(maxValue - minValue) <= limit and right < len(nums):
                maxValue = max(maxValue, nums[right])                
                minValue = min(minValue, nums[right])
                count_dict[nums[right]] 
                longestWindow = max(longestWindow, right-left)
                right += 1

            while abs(maxValue - minValue) > limit and left < len(nums):
                if decrement_count(nums[left]): 
                    if nums[left] == maxValue:
                        maxValue = max(nums[left:right+1])

                    if nums[left] == minValue:
                        minValue = min(nums[left:right+1])

                left += 1
                if left == right:
                    right += 1
                
                # for num in range(maxValue, minValue, -1):
                #     if num in count_dict:
                #         maxValue = num
                #         break


        return max(longestWindow, right-left)
    
sol = Solution()
res = sol.longestSubarray([2,5,2], 9)
print(res) # 2