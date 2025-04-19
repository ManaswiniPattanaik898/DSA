class Solution:
    def smallestSubWithSum(self, x, arr):
        n = len(arr)
        min_len = float('inf')
        current_sum = 0
        start = 0

        for end in range(n):
            current_sum += arr[end]  # Expand window

        # Try shrinking the window from the start as long as sum > x
            while current_sum > x:
                min_len = min(min_len, end - start + 1)
                current_sum -= arr[start]
                start += 1

        return min_len if min_len != float('inf') else 0

                
                
            
        



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends