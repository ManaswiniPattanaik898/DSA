#User function Template for python3

class Solution:
    def multiply(self, arr):
        # Code here
        n=len(arr)
        sum1,sum2=0,0
        for i in range(0,n//2):
            sum1+=arr[i]
        for j in range(n//2,n):
            sum2+=arr[j]
        return sum1*sum2
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.multiply(arr))
        print("~")

# } Driver Code Ends