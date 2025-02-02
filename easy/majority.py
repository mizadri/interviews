class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_count = {}

        for n in nums:
            if n not in elem_count:
                elem_count[n] = 1
            else:
                elem_count[n] += 1

        max_item = max(elem_count.items(), key=lambda x: x[1]) 

        return max_item[0]
