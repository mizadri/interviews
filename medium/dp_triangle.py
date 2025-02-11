from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-to-last row and move upward
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update current cell with the minimum sum from below
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        
        # The top element contains the minimum path sum
        return triangle[0][0]
