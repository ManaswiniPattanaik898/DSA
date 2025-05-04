#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3



class Solution:
    def arranged(self,arr):
        #Code here
        pos=[]
        neg=[]
        for i in arr:
            if i>=0:
                pos.append(i)
            else:
                neg.append(i)
        result=[]
        for i in range(len(pos)):
            result.append(pos[i])
            result.append(neg[i])
        return result
        
        
        
            


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.arranged(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends