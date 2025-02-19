#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
	    result=S[0]
	    n=len(S)
	    for i in range(n-1):
	        if S[i]==" " and S[i+1]!=" ":
	            result+=S[i+1]
	    return result
	        
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.firstAlphabet(S)

        print(answer)
        print("~")

# } Driver Code Ends