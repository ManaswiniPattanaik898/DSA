#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        n = len(arr)
    
    # Arrange elements in max-min fashion
        shuffled = []
        left, right = 0, n - 1
    
        while left <= right:
            if right != left:
                shuffled.append(arr[right])
            shuffled.append(arr[left])
            left += 1
            right -= 1
    
    # Compute the sum of absolute differences
        max_sum = sum(abs(shuffled[i] - shuffled[i - 1]) for i in range(1, n))
        max_sum += abs(shuffled[-1] - shuffled[0])  # Circular sum
    
        return max_sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends