#User function Template for python3
from collections import Counter
class Solution:

    def isPossible(self, S):
        freq=Counter(S)
        odd_count=sum(1 for  count in freq.values() if count%2!=0)
        return 1 if odd_count<=1 else 0

        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        if solObj.isPossible(S):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends