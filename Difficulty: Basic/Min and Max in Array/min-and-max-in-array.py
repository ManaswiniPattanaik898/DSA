#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
#User function Template for python3

class Solution:
    def get_min_max(self, arr):
        lst=[]
        min_val = float('inf')
        max_val = float('-inf')
        n=len(arr)
        for i in range(0,n):
            if arr[i]>max_val:
                max_val=arr[i]
            if arr[i]<min_val:
                min_val=arr[i]
            
        return min_val,max_val
    

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        mn, mx = ob.get_min_max(arr)
        print(mn, mx)
        t -= 1
        print("~")


# } Driver Code Ends