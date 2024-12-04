from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        nIslands = 0
        next_moves = [[1,0],[-1,0],[0,1],[0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and (i,j) not in visited:
                    nIslands += 1
                    queue = deque()
                    queue.append((i,j))

                    while(queue):
                        curr_cell = queue.pop()
                        visited.add(curr_cell)

                        for move in next_moves:
                            next_cell = (curr_cell[0]+move[0], curr_cell[1]+move[1])
                            if next_cell[0] >= 0 and next_cell[0] < len(grid) and \
                                 next_cell[1] >= 0 and next_cell[1] < len(grid[0]) and \
                                 grid[next_cell[0]][next_cell[1]] == "1" and next_cell not in visited:

                                queue.append(next_cell)

        return nIslands

                        