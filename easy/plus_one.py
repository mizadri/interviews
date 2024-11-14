from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 1  # We start with a carry of 1, as we're adding 1 to the number
        for ix in range(len(digits) - 1, -1, -1):
            digits[ix] += carryover
            if digits[ix] == 10:
                digits[ix] = 0
                carryover = 1
            else:
                carryover = 0
                break
        
        # If there's still a carryover left, we need to add a 1 at the beginning
        if carryover:
            digits.insert(0, 1)
        
        return digits
