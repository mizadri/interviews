# https://leetcode.com/problems/3sum/
"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

In my code it also recognizes [0,1,-1], since they have different indices
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if (i != j and i != k and j != k):
                        triplet = frozenset([i,j,k])

                        if sum([nums[ix] for ix in triplet]) == 0:
                            triplets.add(triplet)

        return [[nums[ix] for ix in triplet] for triplet in triplets]