
from typing import List


class Solution:
    def findPair(self, arr: List[int], x: int) -> int:
        # code here
        arr.sort()
        i,j=0,1
        while j<len(arr):
            val=abs(arr[j]-arr[i])
            if val==x:
                return True
            if val<x:
                j+=1
            else:
                i+=1
            if i==j:
                j+=1
        return False



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        x = int(input())

        obj = Solution()
        res = obj.findPair(arr, x)

        print("true" if res else "false")
        print("~")

# } Driver Code Ends