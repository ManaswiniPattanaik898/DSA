#User function Template for python3

class Solution:
    def RedOrGreen(self,N,S):
        #code here
        count1,count2=0,0
        for i in range(0,N):
            if S[i]=='R':
                count1+=1
            else:
                count2+=1
        if count1>count2:
            return count2
        else:
            return count1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        S=input()
        
        ob=Solution()
        print(ob.RedOrGreen(N,S))
        print("~")
# } Driver Code Ends