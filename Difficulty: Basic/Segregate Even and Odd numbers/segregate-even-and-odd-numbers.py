#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr):
	    evens = sorted([num for num in arr if num % 2 == 0])  # Collect and sort evens
        odds = sorted([num for num in arr if num % 2 != 0])   # Collect and sort odds
        
        # Modify arr in-place
        arr[:len(evens)] = evens  
        arr[len(evens):] = odds  
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

        print("~")

# } Driver Code Ends