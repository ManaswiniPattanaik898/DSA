#User function Template for python3

class Solution:
    def removeDuplicate(self, arr):
        seen = set()
        unique_arr = []
        
        for num in arr:
            if num not in seen:
                seen.add(num)
                unique_arr.append(num)
        
        return unique_arr 
       


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
        ans = ob.removeDuplicate(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends