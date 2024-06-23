class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # generate subarrays, check if all fullfil the condition
        longest_sub = 0
        for i,xi in enumerate(nums):
            subarray = [xi]
            for j in range(i+1,len(nums)): #if abs(xi-nums[j]) :
                if all( abs(xxi-nums[j]) <= limit for xxi in subarray):
                    subarray.append(nums[j])
                else:
                    break