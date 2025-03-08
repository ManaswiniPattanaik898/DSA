#User function Template for python3
from collections import Counter
class Solution:
	def removeDups(self, str):
		# code here
		seen=set()
		result=[]
		for i in range(len(str)):
		    if str[i] not in seen:
		        seen.add(str[i])
		        result.append(str[i])
		return "".join(result)
		
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)
        print("~")

# } Driver Code Ends