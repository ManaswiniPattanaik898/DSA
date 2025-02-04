#User function Template for python3
class Solution:
    def getMoreAndLess(self, arr, target):
		# code here
		count1=0
		count2=0
		n=len(arr)
		for i in range(0,n):
		    if arr[i]<=target:
		        count1+=1
		    if arr[i]>=target:
		        count2+=1
		return count1,count2
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input())
        ob = Solution()
        ans = ob.getMoreAndLess(arr, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

        print("~")

# } Driver Code Ends