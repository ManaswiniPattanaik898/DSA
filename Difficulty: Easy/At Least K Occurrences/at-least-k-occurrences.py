#User function Template for python3


class Solution:
    def firstElementKTime(self, arr,k):
        # code here
        freq = {}
    
        for i, num in enumerate(arr):
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == k:
                return num
    
        return -1
        
        
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.firstElementKTime(arr, k)
        print(res)
        # print("~")
        t -= 1

# } Driver Code Ends