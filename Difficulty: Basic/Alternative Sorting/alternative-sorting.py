class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        arr.sort()
        result=[]
        left,right=0,len(arr)-1
        while left<right:
            result.append(arr[right])
            result.append(arr[left])
            left+=1
            right-=1
        if left==right:
            result.append(arr[left])
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends