#User function Template for python3
class Solution:
    def conRevstr (ob, S1, S2):
        # code here 
        s3=S1+S2
        return s3[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1 = input()
        S2 = input()
        ob = Solution()
        print(ob.conRevstr(S1,S2))
# } Driver Code Ends