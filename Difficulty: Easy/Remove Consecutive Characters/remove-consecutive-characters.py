#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, s):
        result=[s[0]]
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                result.append(s[i])
        return "".join(result)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

        print("~")
# } Driver Code Ends