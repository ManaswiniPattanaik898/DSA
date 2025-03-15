#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    low, mid, high = 0, 0, len(arr) - 1
    
        while mid <= high:
            if arr[mid] < a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif a <= arr[mid] <= b:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
    
        return True 
	    


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        a = int(input())
        b = int(input())
        ob = Solution()
        ob.threeWayPartition(arr,a,b)
        ia = 0
        ib = 0
    
        for i in range(len(arr)):
            if arr[i] >= a:
                ia = i
                break
    
        for i in range(len(arr)):
            if arr[i] > b:
                ib = i
                break
    
        f = 0
    
        for i in range(ia):
            if arr[i] >= a:
                f = 1
                break
    
        for i in range(ia, ib):
            if arr[i] > b or arr[i] < a:
                f = 1
                break
    
        for i in range(ib, len(arr)):
            if arr[i] < b:
                f = 1
                break
    
        if f == 1:
            print("false")
        else:
            print("true")
        print("~")
        t -= 1


# } Driver Code Ends