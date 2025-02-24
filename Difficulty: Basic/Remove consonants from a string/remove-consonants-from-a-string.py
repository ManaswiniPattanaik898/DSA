#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        vowels=("aeiouAEIOU")
        result = "".join([ch for ch in s if ch in vowels])
        return result if result else "No Vowel"
            
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))
        print("~")
# } Driver Code Ends