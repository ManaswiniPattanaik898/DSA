#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxNtype(self , arr):
        #code here.
        n=len(arr)
        asc,desc=True,True
        for i in range(1,n):
            if arr[i]>arr[i-1]:
                desc=False
            elif arr[i]<arr[i-1]:
                asc=False
        if asc:
            return 1
        if desc:
            return 2
        min_index=arr.index(min(arr))
        max_index=arr.index(max(arr))
        
        if max_index+1==min_index:
            return 4
        else:
            return 3
    
    


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxNtype(arr)
        print(res)
        print("~");
        t -= 1


# } Driver Code Ends