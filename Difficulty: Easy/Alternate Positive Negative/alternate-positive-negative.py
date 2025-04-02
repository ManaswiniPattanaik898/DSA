#User function Template for python3

class Solution:
    def rearrange(self, arr):
        # Separate positive and negative numbers while maintaining order
        pos = [num for num in arr if num >= 0]
        neg = [num for num in arr if num < 0]
        
        i, j, k = 0, 0, 0  # k is for modifying arr in-place
        
        # Alternate positive and negative numbers
        while i < len(pos) and j < len(neg):
            arr[k] = pos[i]
            k += 1
            i += 1
            arr[k] = neg[j]
            k += 1
            j += 1

        # Append remaining elements
        while i < len(pos):
            arr[k] = pos[i]
            k += 1
            i += 1
        
        while j < len(neg):
            arr[k] = neg[j]
            k += 1
            j += 1
        
        # No need to return anything if modification is in-place

        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends