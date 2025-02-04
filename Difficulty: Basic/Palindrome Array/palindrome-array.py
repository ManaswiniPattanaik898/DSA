
from typing import List


class Solution:
    def isPerfect(self, arr : List[int]) -> bool:
        # code here
        return arr[0:]==arr[-1 : :-1]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = list(map(int, input().strip().split()))

        obj = Solution()
        res = obj.isPerfect(arr)

        if res:
            print("true")
        else:
            print('false')
        print("~")
# } Driver Code Ends