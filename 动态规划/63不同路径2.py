class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]==1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i==0 and j==0: #初始化为1了，如果不跳过又会变回0
                    continue
                if obstacleGrid[i][j]==0: 
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] if i>0 else 0)+(obstacleGrid[i][j-1] if j>0 else 0)
                elif obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
        return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
