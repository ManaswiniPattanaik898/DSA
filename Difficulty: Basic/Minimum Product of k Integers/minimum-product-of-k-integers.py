#Back-end complete function Template for Python 3


class Solution:
    # Function to find the minimum product of first k elements of array.
    def minProduct(self, arr, k):
        # Sorting the array in ascending order.
        n = len(arr)
        arr.sort()

        # Initializing the modulo.
        mod = 1000000007

        # Initializing the product.
        s = 1

        # Taking minimum of n and k.
        n = min(n, k)

        # Calculating the product of first k elements.
        for i in range(n):
            s = arr[i] * s

            # Taking the modulo.
            s = s % mod

        return s % mod



#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minProduct(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends