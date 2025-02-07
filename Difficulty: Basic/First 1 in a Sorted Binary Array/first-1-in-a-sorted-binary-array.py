#{ 
 # Driver Code Starts

# } Driver Code Ends
#User function Template for python3

class Solution:
    def firstIndex(self, arr):
        for i in range(len(arr)):
            if arr[i]==1:
                return i
                break
        return -1
    # Your code goes here
    


#{ 
 # Driver Code Starts.
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.firstIndex(arr))
        print("~")
# } Driver Code Ends