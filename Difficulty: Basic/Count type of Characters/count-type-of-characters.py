#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        count1,count2,count3,count4=0,0,0,0
        for i in s:
            if i.isupper():
                count1+=1
            elif i.islower():
                count2+=1
            elif i.isdigit():
                count3+=1
            else:
                count4+=1
        return count1,count2,count3,count4


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
    print("~")
# Contributed By: Pranay Bansal

# } Driver Code Ends