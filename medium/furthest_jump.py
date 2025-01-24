class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0 

        for i in range(len(nums)):
            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])
            
            # If we can reach or exceed the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        return False