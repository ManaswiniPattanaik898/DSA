
#User function Template for python3
import re
class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self, s):
        numbers = re.findall(r'\d+',s)
        return sum(map(int,numbers))
        
        
                
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


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.findSum(s))
        print("~")

# } Driver Code Ends