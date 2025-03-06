#User function template for Python

class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        lo,hi=0,len(arr)-1
        first_occurrence = -1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if arr[mid]==k:
                first_occurrence = mid
                hi=mid-1
            elif arr[mid]<k:
                lo=mid+1
            else:
                hi=mid-1
        return first_occurrence



#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)
        print("~")

# } Driver Code Ends