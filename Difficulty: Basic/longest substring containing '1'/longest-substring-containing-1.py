#User function Template for python3

def maxlength(s):
    n=len(s)
    count,max_val=0,0
    for i in range(0,n):
        if s[i]=='1':
            count+=1
            max_val=max(max_val,count)
        else:
            count=0
    return max_val
        
    
    
    
    #add code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
        print("~")
# } Driver Code Ends