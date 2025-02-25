#User function Template for python3

class Solution:
    def modify(self, N):
        #code here
        N=str(N)
        result=N[0]
        for i in range(1,len(N)):
            if N[i]!=N[i-1]:
                result+=N[i]
        return int(result)
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        num = int(input())

        solObj = Solution()

        print(solObj.modify(num))
# } Driver Code Ends