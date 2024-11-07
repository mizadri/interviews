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
                        triplet = frozenset([nums[i],nums[j],nums[k]])

                        if sum([nums[ix] for ix in triplet]) == 0:
                            triplets.add(triplet)

        return [[nums[ix] for ix in triplet] for triplet in triplets]
    


    """
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        target_elements_ixs = {}
        results = set()
        for i in range(len(nums)):
            fixed_element = nums[i]
            # Do two sum after fixing i
            for j in range(len(nums)):
                if i != j:
                    target_elements_ixs[-fixed_element-nums[j]] = j
            for k in range(len(nums)):
                if i != k:
                    cur_el = nums[k]
                    if cur_el in target_elements_ixs:
                        jj = target_elements_ixs[cur_el]
                        if jj != k:
                            triplet = [fixed_element,nums[jj],cur_el]
                            if sum(triplet) == 0:
                                results.add(tuple(sorted(triplet)))
        return [list(triples) for triples in results]
    
    """