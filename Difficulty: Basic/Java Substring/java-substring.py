#User function Template for python3
class Solution:
    def javaSub (ob, S, L, R):
        # code here 
        stri=""
        for i in range(L,R+1):
            stri+=S[i]
        return stri


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        L,R = input().split()
        L = int(L)
        R = int(R)
        
        ob = Solution()
        print(ob.javaSub(S,L,R))
# } Driver Code Ends