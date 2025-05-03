#User function Template for python3


class Solution:
    def findMissing(self,a,b):
        b_set=set(b)
        result=[num for num in a if num not in b_set]
        return result
        
        
        
    # code here
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ob = Solution()
    ans = ob.findMissing(a, b)
    for each in ans:
        print(each, end=' ')
    print()
    print("~")

# } Driver Code Ends