
#User function Template for python3

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        s3=""
        s4=""
        common_chars = set(s1)&set(s2)
        for char in s1:
            if char not in common_chars:
                s3+=char
        for char in s2:
            if char not in common_chars:
                s4+=char
        result=s3+s4
        return result if result else "-1"
        
       
                    
        #code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        obj = Solution()
        print(obj.concatenatedString(s,p))
        print("~")
# } Driver Code Ends