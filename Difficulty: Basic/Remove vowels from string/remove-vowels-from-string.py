#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code 
		stri=""
		vowels=set("aeiou")
		for val in s:
		    if val not in vowels:
		        stri+=val
		return stri
		       
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeVowels(s)

        print(answer)

# } Driver Code Ends