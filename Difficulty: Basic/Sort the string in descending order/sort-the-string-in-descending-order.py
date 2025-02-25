#User function Template for python3
class Solution:
    def ReverseSort(self, s): 
        # code here
        return "".join(sorted(s,reverse=True))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.ReverseSort(s))
        print("~")

# } Driver Code Ends