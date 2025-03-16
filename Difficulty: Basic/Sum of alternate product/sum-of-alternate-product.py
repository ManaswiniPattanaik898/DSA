#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def altProduct(self, arr):
       # Your code goes here
       arr.sort()
       n=len(arr)
       i,j=0,n-1
       sum_val=0
       while i<=j:
           sum_val+=arr[i]*arr[j]
           i+=1
           j-=1
       return sum_val
    


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.altProduct(arr)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends