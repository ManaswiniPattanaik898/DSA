#User function Template for python3

class Solution:
	def countOddEven(self, arr):
		#Code here
		n = len(arr)
		even_val,odd_val=0,0
		for i in range(0,n):
		    if arr[i]%2==0:
		        even_val+=1
		    else:
		        odd_val+=1
		return odd_val,even_val
		    


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    # Testcase input
    testcase = int(input())

    for _ in range(testcase):

        arr = list(map(int, input().split()))

        # Creating an object of the Solution class
        ob = Solution()

        # Calling the function to count even and odd
        res = ob.countOddEven(arr)

        # Printing the result
        print(*res)
        print("~")

# } Driver Code Ends