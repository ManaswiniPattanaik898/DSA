#User function Template for python3


class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        n=len(arr)
        sum1,sum2=0,0
        for i in range(0,n//2):
            sum1+=arr[i]
        for j in range(n//2,n):
            sum2+=arr[j]
        return abs(sum1-sum2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.min_value_to_balance(arr)
        print(ans)
        print("~")

# } Driver Code Ends