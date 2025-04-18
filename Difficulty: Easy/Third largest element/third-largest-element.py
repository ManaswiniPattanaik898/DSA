class Solution:
    def thirdLargest(self,arr):
        # code here
        n = len(arr)
        if n < 3:
            return -1

        first = second = third = float('-inf')

        for num in arr:
            if num >= first:
                third = second
                second = first
                first = num
            elif num >= second:
                third = second
                second = num
            elif num >= third:
                third = num

        return third


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))
        print("~")

# } Driver Code Ends