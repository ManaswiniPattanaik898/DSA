#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		max_val=0
		for i in range(len(arr)):
		    if arr[i]>max_val:
		        max_val=arr[i]
	    return max_val


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends