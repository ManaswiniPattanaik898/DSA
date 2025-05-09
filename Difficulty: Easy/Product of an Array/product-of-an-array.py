#User function Template for python3
class Solution:
    # arr is the array
    def product(self, arr):
        # your code here
        prod=1
        for i in range(len(arr)):
            prod*=arr[i]
        if prod<1000000007:
            return prod
        else:
            return prod % 1000000007


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        ans = obj.product(arr)
        print(ans)
        print("~")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends