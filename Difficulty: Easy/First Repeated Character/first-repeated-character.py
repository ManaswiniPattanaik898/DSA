#User function Template for python3

class Solution:
    def firstRepChar(self, s):
        # code here
        seen=set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)
        return -1
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solObj = Solution()
        print(solObj.firstRepChar(s))
        print("~")

# } Driver Code Ends