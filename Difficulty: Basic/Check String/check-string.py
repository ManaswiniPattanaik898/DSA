#User function Template for python3

class Solution:
    def check (self,s):
        n=len(s)
        for i in range(n-1):
            if s[i]!=s[i+1]:
                return False
        return True
        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    if ob.check (s):
        print ("YES")
    else:
        print ("NO")
        
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends