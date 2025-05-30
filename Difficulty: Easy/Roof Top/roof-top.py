#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps 
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        max_steps,curr_steps=0,0
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                curr_steps+=1
                max_steps=max(max_steps,curr_steps)
            else:
                curr_steps=0
        return max_steps


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.maxStep(arr))

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends