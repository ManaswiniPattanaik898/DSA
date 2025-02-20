#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        i,j=0,0
        result=[]
        n1,n2=len(S1),len(S2)
        while i<n1 and j<n2:
            result.append(S1[i])
            result.append(S2[j])
            i+=1
            j+=1
        result.append(S1[i:])
        result.append(S2[j:])
        return "".join(result)
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
        print("~")
# } Driver Code Ends