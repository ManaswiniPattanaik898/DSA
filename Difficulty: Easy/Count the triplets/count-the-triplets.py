#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# User function Template for python3
class Solution:
	def countTriplet(self, arr):
		# code here
		arr.sort()
		n=len(arr)
		count=0
		for k in range(n-1,1,-1):
		    i,j=0,k-1
		    while i<j:
		        if arr[i]+arr[j]==arr[k]:
		            count+=1
		            i+=1
		            j-=1
		        elif arr[i]+arr[j]<arr[k]:
		            i+=1
		        else:
		            j-=1
		return count          
		   


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countTriplet(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends