#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		l,r=l-1,r-1
		arr[l:r+1]=arr[l:r+1][::-1]
		return arr


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        l = int(input())
        r = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.reverseSubArray(arr, l, r)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends