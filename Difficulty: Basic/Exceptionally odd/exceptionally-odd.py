#User function Template for python3
from collections import Counter
class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        freq=Counter(arr)
        for i in range(len(arr)):
            if freq[arr[i]]%2!=0:
                return arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

        print("~")
# } Driver Code Ends