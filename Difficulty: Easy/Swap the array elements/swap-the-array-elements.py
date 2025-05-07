#User function Template for python3

class Solution:
	def swapElements(self, arr):
	    #Code here
	    for i in range(len(arr)-2):
	        arr[i],arr[i+2]=arr[i+2],arr[i]
	    return arr
	   


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.swapElements(arr)
        for i in arr:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends