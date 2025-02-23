#User function Template for python3

class Solution:
	def minimumDifference(self, arr):
		# Code here
		arr = sorted(arr) 
        diff = 10**20
        for i in range(n-1): 
            if arr[i+1] - arr[i] < diff: 
                diff = arr[i+1] - arr[i] 
        return diff 
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        ans = ob.minimumDifference(nums)
        print(ans)

# } Driver Code Ends