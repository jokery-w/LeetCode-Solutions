class Solution(object):
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j] <= -1:
                    count += 1
                if grid[i][j] >= 0:
                    break
        return  count