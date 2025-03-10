#User function Template for python3

class Solution:
    def maxValue(self, arr): 
        # Complete the function
        arr.sort()
        n=len(arr)
        MOD = 10**9 + 7
        val=0
        sum_val=1
        for i in range(n):
            val+=i*arr[i]
        return val%MOD
    
            
      



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.maxValue(A))
        print("~")

# } Driver Code Ends