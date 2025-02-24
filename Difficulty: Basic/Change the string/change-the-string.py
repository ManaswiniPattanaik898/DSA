#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        for i in s:
            if i.isupper():
                return s.upper()
            else:
                return s.lower()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
# } Driver Code Ends