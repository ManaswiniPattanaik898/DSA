
#User function Template for python3
from collections import Counter
class Solution:
    
    #Function to find repeated character whose first appearance is leftmost.
    def repeatingCharacter(self,s):
        #code here
        freq=Counter(s)
        n=len(s)
        for i in range(0,n):
            if freq[s[i]]>1:
                return i
        return -1


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
        obj = Solution()
        index=obj.repeatingCharacter(s)
        if(index==-1):
            print(-1)
        else:
            print(s[index])
            
        print("~")
# } Driver Code Ends