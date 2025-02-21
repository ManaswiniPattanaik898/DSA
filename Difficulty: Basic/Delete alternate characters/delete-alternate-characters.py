#User function Template for python3
class Solution:
    def delAlternate (ob, S):
        stri=""
        n=len(S)
        for i in range(0,n,2):
            stri+=S[i]
        return stri
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        
        ob = Solution()
        print(ob.delAlternate(S))
# } Driver Code Ends