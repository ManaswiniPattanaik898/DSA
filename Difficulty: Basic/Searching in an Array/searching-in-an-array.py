
from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # code here
        n=len(arr)
        for i in range(n):
            if arr[i]==k:
                return i+1
                break
        return -1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        k = int(input())  # Read the element to search
        arr = list(map(int, input().split()))  # Read the array elements

        obj = Solution()
        res = obj.search(k, arr)

        print(res)
        print("~")

# } Driver Code Ends