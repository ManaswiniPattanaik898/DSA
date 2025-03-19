#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
	    arr.sort()
	    left,right=0,len(arr)-1
	    while left<right:
	        curr=arr[left]+arr[right]
	        if curr==target:
	            return True
	        elif curr<target:
	            left+=1
	        else:
	            right-=1
	    return False
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends