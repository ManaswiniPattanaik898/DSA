class Solution:
    def transitionPoint(self, arr): 
        # Code here
        for i in range(len(arr)):
            if arr[i]==1:
                return i
        return -1


#{ 
 # Driver Code Starts
#driver code
if __name__ == '__main__':
    t = int(input())
    for i in range(t):

        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr))

        print("~")

# } Driver Code Ends