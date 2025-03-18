#User function Template for python3
class Solution:

	def convert(self,arr, n):
		# code here
		indexed_arr=[(arr[i],i) for i in range(n)]
		indexed_arr.sort()
		for rank,(_,index) in enumerate(indexed_arr):
		    arr[index]=rank
		return arr
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

        print("~")
# } Driver Code Ends