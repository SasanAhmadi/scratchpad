from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        visited = {}

        height = len(grid)
        width = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0 or i > height -1 or j > width - 1 or (i,j) in visited or grid[i][j] == "0":
                return
            visited[(i, j)] = 1
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(height):
            for j in range(width):
                if not (i,j) in visited and grid[i][j] == "1":
                    result +=1
                    dfs(i,j)


        return result


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
assert Solution().numIslands(grid) == 1


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
assert Solution().numIslands(grid) == 3


