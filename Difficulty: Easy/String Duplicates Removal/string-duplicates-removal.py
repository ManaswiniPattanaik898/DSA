#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    seen=set()
	    result=[]
	    for char in s:
	        if char not in seen:
	            seen.add(char)
	            result.append(char)
	    return "".join(result)
	            
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends