#User function Template for python3

class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        # code here
        max_val=float('-inf')
        min_val=float('inf')
        for i in range(len(arr1)):
            if max_val<arr1[i]:
                max_val=arr1[i]
        for j in range(len(arr2)):
            if min_val>arr2[j]:
                min_val=arr2[j]
        return max_val*min_val




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.find_multiplication(arr1, arr2)
        print(ans)
        print("~")

# } Driver Code Ends