
from typing import List


class Solution:
    def findElementAtIndex(self, key : int, arr : List[int]) -> int:
        # code here
        for i in arr:
            return arr[key]
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        key = int(input())
        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.findElementAtIndex(key, arr)

        print(res)
        print("~")

# } Driver Code Ends