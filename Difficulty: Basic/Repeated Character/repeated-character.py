#User function Template for python3
from collections import Counter
class Solution:
    def firstRep(self, s):
        # code here
        freq=Counter(s)
        for ch in s:
            if freq[ch]>1:
                return ch
        return "#"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.firstRep(s)
        if ans is '#':
            print(-1)
        else:
            print(ans)
        
        print("~")
# } Driver Code Ends