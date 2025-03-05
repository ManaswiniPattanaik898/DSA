
class Solution:
    def findDuplicates(self, arr):
        if len(arr)<2:
            return []
        arr.sort()
        result=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                if not result or result[-1]!=arr[i]:
                    result.append(arr[i])
        return result
                
        # code here
         



#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().findDuplicates(arr)  # find the duplicates
    # Sort the result in ascending order
    s.sort()
    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print duplicates in ascending order
    else:
        print("[]")  # Print empty list if no duplicates are found
    print("~")

# } Driver Code Ends