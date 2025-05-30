class Solution:
    def minDeletions(self,s):
        # code here 
        n = len(s)
        rev_s = s[::-1]
    
    # Create a DP table for LCS
        dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Length of Longest Palindromic Subsequence
        lps = dp[n][n]
    
        return n - lps