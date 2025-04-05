
class Solution:
    def minDist(self, arr, x, y):
        x_index=[]
        y_index=[]
        for i in range(len(arr)):
            if arr[i]==x:
                x_index.append(i)
            elif arr[i]==y:
                y_index.append(i)
        if not x_index or not y_index:
            return -1
        i,j=0,0
        min_dist=float('inf')
        while i<len(x_index) and j<len(y_index):
            min_dist=min(min_dist,abs(x_index[i]-y_index[j]))
            if x_index[i]<y_index[j]:
                i+=1
            else:
                j+=1
        return min_dist
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        x = int(input())
        y = int(input())
        print(Solution().minDist(arr, x, y))
        print("~")

# } Driver Code Ends