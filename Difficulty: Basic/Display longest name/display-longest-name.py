
class Solution:
    def longest(self, arr):
        # code here
        longest=arr[0]
        for name in arr:
            if len(name)>len(longest):
                longest=name
        return longest
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        names = input().split()
        obj = Solution()
        res = obj.longest(names)
        print(res)
        print("~")
# } Driver Code Ends