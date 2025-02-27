#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        i,j=0,len(arr2)-1
        count=0
        while i<len(arr1) and j>=0:
            sum_val=arr1[i]+arr2[j]
            if sum_val==x:
                count+=1
                i+=1
                j-=1
            elif sum_val<x:
                i+=1
            else:
                j-=1
        return count
                    



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x = int(input())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob = Solution()
        l = ob.countPairs(arr1, arr2, x)
        print(l)
        print("~")

# } Driver Code Ends