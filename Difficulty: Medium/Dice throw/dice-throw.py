class Solution:
    def noOfWays(self, m,n,x):
        # code here
        dp = [[0] * (x + 1) for _ in range(n + 1)]
    
    # Base case
        dp[0][0] = 1
    
    # Fill the table
        for i in range(1, n + 1):  # For each dice
            for j in range(1, x + 1):  # For each target sum
                for f in range(1, m + 1):  # For each face value
                    if j - f >= 0:
                        dp[i][j] += dp[i - 1][j - f]
    
        return dp[n][x]