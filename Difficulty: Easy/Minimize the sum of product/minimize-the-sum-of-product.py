#User function Template for python3

class Solution:
    def minValue(self, arr1, arr2):
        #code here
        sum_val=0
        arr1.sort()
        arr2.sort(reverse=True)
        sum_val=sum(a*b for a,b in zip(arr1,arr2))
        return sum_val



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split("\n")
    t = int(data[0].strip())
    index = 1
    for _ in range(t):
        if index < len(data):
            arr1 = list(map(int, data[index].strip().split()))
            index += 1
        if index < len(data):
            arr2 = list(map(int, data[index].strip().split()))
            index += 1
        ob = Solution()
        ans = ob.minValue(arr1, arr2)
        print(ans)
        print("~")

# } Driver Code Ends