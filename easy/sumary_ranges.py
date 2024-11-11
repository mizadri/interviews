class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        # Find consecutive ranges
        result = []
        start = nums[0]

        # Go through nums and check the previous
        for n in range(1,len(nums)):
            if nums[n] != nums[n-1] + 1:
                if start == nums[n-1]:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{nums[n-1]}")
                start = nums[n]

        if start == nums[-1]:
            result.append(f"{start}")
        else:
            result.append(f"{start}->{nums[-1]}")
                    
        return result

        