#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def immediateSmaller(self, arr):
		# code here
		n=len(arr)
		for i in range(n-1):
		    if arr[i]>arr[i+1]:
		        arr[i]=arr[i+1]
		    else:
		         arr[i]=-1
		arr[-1]=-1

#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.immediateSmaller(arr)
        for x in arr:
            print(x, end=" ")
        print()
        print("~")
        t -= 1#Initial Template for Python 3




# } Driver Code Ends