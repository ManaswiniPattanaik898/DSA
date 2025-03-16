class Solution:
    def maxProfit(self, m, arr):
        useless_laptops = sorted([-x for x in arr if x < 0], reverse=True)
        return sum(useless_laptops[:m])
        #Your code goes here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxProfit(k, arr))
        print("~")

# } Driver Code Ends