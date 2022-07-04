import math

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        
        launch a binary search for target - numbers[i]
        """
        size=len(numbers)
        
        for i in range(size):
            # Binary search for x = target - numbers[i]
            x = target - numbers[i]        
            
            low = i
            high = size - 1
            mid = 0

            while low <= high:
                mid = math.ceil((high + low) / 2)
                # If x is greater, ignore left half
                if numbers[mid] < x:
                    low = mid + 1
                # If x is smaller, ignore right half
                elif numbers[mid] > x:
                    high = mid - 1
                # means x is present at mid
                else:
                    return [i+1, mid+1]

s = Solution()
print(s.twoSum([1,2,3,4,4,9,56,90] ,8))                  
                                            