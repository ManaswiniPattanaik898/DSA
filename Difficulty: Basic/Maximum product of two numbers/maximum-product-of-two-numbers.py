#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def maxProduct(self,arr):
	    max_val=float('-inf')
	    max_val_2=float('-inf')
	    for num in arr:
            if num > max_val:
                max_val_2, max_val = max_val, num
            elif num > max_val_2:
                max_val_2 = num
	    return max_val*max_val_2
	         
		# code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxProduct(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends