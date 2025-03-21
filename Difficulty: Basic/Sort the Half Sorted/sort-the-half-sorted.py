#User function Template for python3

class Solution:
    def sortHalves (self, arr, n):
        
    # Find the split index
        mid = 0
        while mid < n - 1 and arr[mid] <= arr[mid + 1]:
            mid += 1
        mid += 1  # Move to the start of the second half

    # Two-pointer merge approach
        i, j, k = 0, mid, 0
        temp = [0] * n

        while i < mid and j < n:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

    # Copy remaining elements
        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < n:
            temp[k] = arr[j]
            j += 1
            k += 1

    # Copy back to the original array
        arr[:] = temp

        # your code here
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    arr = list(map(int, input().split()))
    ob = Solution()
    ob.sortHalves (arr, n)
    
    for i in range (n):
        print (arr[i], end = " ")
    print ()
    
    print("~")
# Contributed By: Pranay Bansal
# } Driver Code Ends