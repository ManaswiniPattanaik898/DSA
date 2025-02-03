# Function should return an integer value
class Solution:
    def convertFive(self,n):
         n_str = str(n)
    # Replace all occurrences of '0' with '5'
         n_str = n_str.replace('0', '5')
    # Convert the modified string back to an integer
         return int(n_str)

   
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        ob = Solution()
        print(ob.convertFive(int(input().strip())))
        print("~")
# } Driver Code Ends