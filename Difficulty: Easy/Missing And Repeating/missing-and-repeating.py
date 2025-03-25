#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        sum_n=n*(n+1)//2
        sum_sq_n=n*(n+1)*(2*n+1)//6
        
        sum_arr=sum(arr)
        sum_sq_arr=sum(x*x for x in arr)
        
        diff=sum_n-sum_arr
        sq_diff=sum_sq_n-sum_sq_arr
        
        sum_md=sq_diff//diff
        
        missing=(diff+sum_md)//2
        duplicate=sum_md-missing
        
        return [duplicate,missing]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends