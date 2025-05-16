#User function Template for python3


class Solution:
    
    #Function to find the minimum element in sorted and rotated array.
    def minNumber(self, arr,low,high):
        #Your code here
        low,high=0,len(arr)-1
        while(low<high):
            mid=low+(high-low)//2
            if(arr[mid]>arr[high]):
                low=mid+1
            else:
                high=mid
        return arr[low]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.minNumber(A,0,N-1))
            
            T-=1


            print("~")
if __name__ == "__main__":
    main()
# } Driver Code Ends