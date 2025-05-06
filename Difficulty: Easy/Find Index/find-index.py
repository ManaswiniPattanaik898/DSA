#User function Template for python3

class Solution:
    def findIndex (self,arr, key ):
        #code here.
        start=-1
        end=-1
        for i in range(len(arr)):
            if arr[i]==key:
                if start==-1:
                    start=i
                end=i
        return [start,end]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    # n=int(input())
    a = list(map(int, input().split()))
    key = int(input())
    ob = Solution()
    ans = ob.findIndex(a, key)
    print(*ans)

    print("~")

# } Driver Code Ends