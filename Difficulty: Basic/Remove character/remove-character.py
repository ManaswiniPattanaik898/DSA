#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        # code here 
        set2=set(string2)
        return "".join(char for char in string1 if char not in set2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends